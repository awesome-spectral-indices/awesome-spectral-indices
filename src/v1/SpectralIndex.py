import ast
import re
from datetime import date
from typing import Annotated, Dict, List, Literal, Optional, Union
from urllib.parse import urlsplit

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    PrivateAttr,
    StrictFloat,
    StrictInt,
    StrictStr,
    computed_field,
    field_validator,
    model_serializer,
    model_validator,
)

from src.v1.utils import (
    ApplicationDomain,
    Bands,
    Constants,
    External,
    IndexFamily,
    Polarizations,
    SensingModality,
    is_hyperspectral_band,
)


StrictNumber = Union[StrictInt, StrictFloat]
NumericRange = Annotated[
    List[StrictNumber],
    Field(min_length=2, max_length=2),
]
SuggestedValues = Dict[StrictStr, Union[StrictInt, StrictFloat, NumericRange]]


class FormulaVisitor(ast.NodeVisitor):
    """
    Validate a spectral-index formula and collect its variable names.

    The visitor accepts only the small expression language used by the
    catalogue: arithmetic operations, numeric constants, variable names, and
    explicitly allowed functions. It never evaluates the formula.
    """

    allowed_functions = (
        "max",
        "min",
        "tanh",
        "log",
        "kernel",
        "spatial_max",
        "spatial_min",
        "spatial_mean",
    )
    spatial_reduction_functions = (
        "spatial_max",
        "spatial_min",
        "spatial_mean",
    )
    allowed_binary_operators = (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow)
    allowed_unary_operators = (ast.UAdd, ast.USub)

    def __init__(self):
        """Create an empty collector that preserves first-seen variable order."""
        self.variables = []
        self._seen_variables = set()
        self.reduction_dimensions = []
        self._seen_reduction_dimensions = set()

    def visit_Expression(self, node):
        """Visit the root expression body produced by ast.parse(..., mode='eval')."""
        self.visit(node.body)

    def visit_BinOp(self, node):
        """Validate binary arithmetic operators and visit both operands."""
        if not isinstance(node.op, self.allowed_binary_operators):
            raise ValueError("Invalid formula.")
        self.visit(node.left)
        self.visit(node.right)

    def visit_UnaryOp(self, node):
        """Validate unary plus/minus operators and visit their operand."""
        if not isinstance(node.op, self.allowed_unary_operators):
            raise ValueError("Invalid formula.")
        self.visit(node.operand)

    def visit_Name(self, node):
        """Record a variable name once, in the order it first appears."""
        if not isinstance(node.ctx, ast.Load):
            raise ValueError("Invalid formula.")
        if node.id not in self._seen_variables:
            self.variables.append(node.id)
            self._seen_variables.add(node.id)

    def visit_Call(self, node):
        """Validate allowed function calls and visit their positional arguments."""
        if (
            not isinstance(node.func, ast.Name)
            or node.func.id not in self.allowed_functions
        ):
            raise ValueError("Invalid formula.")
        if node.keywords:
            raise ValueError("Invalid formula.")
        if node.func.id in ("tanh", "log") and len(node.args) != 1:
            raise ValueError("Invalid formula.")
        if node.func.id == "kernel" and len(node.args) != 2:
            raise ValueError("Invalid formula.")
        if node.func.id in self.spatial_reduction_functions:
            if len(node.args) != 1:
                raise ValueError("Invalid formula.")
            if "space" not in self._seen_reduction_dimensions:
                self.reduction_dimensions.append("space")
                self._seen_reduction_dimensions.add("space")
        for arg in node.args:
            self.visit(arg)

    def visit_Constant(self, node):
        """Allow numeric constants while rejecting strings, booleans, and None."""
        if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
            raise ValueError("Invalid formula.")

    def generic_visit(self, node):
        """Reject any syntax that is not explicitly supported above."""
        raise ValueError("Invalid formula.")


def parse_formula_variables(value):
    """
    Return the variables used by a spectral-index formula.

    The formula is parsed with Python's AST in expression mode, then validated
    by FormulaVisitor. The returned list preserves first-seen order and excludes
    allowed function names such as ``max``, ``tanh``, ``log``, and ``kernel``.
    """
    try:
        tree = ast.parse(value, mode="eval")
    except SyntaxError as exc:
        raise ValueError("Invalid formula.") from exc

    visitor = FormulaVisitor()
    visitor.visit(tree)
    return visitor.variables


def parse_formula_reduction_dimensions(value):
    """Return contextual-reduction dimensions used by a validated formula."""
    try:
        tree = ast.parse(value, mode="eval")
    except SyntaxError as exc:
        raise ValueError("Invalid formula.") from exc

    visitor = FormulaVisitor()
    visitor.visit(tree)
    return visitor.reduction_dimensions


class Source(BaseModel):
    """Scientific source metadata for a spectral index."""

    source_link: str
    source_type: Optional[
        Literal[
            "article",
            "book",
            "book_chapter",
            "conference_paper",
            "poster",
            "report",
            "preprint",
        ]
    ] = None

    _source_link_status: Optional[Literal["operational", "down"]] = PrivateAttr(
        default=None
    )
    _source_companions: List[str] = PrivateAttr(default_factory=list)

    model_config = ConfigDict(extra="forbid")

    @field_validator("source_link")
    @classmethod
    def check_source_link(cls, value):
        """Require an HTTP(S) source link while preserving its original form."""
        parsed = urlsplit(value)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("source_link must be a valid HTTP(S) URL.")
        return value

    @computed_field
    @property
    def source_link_status(self) -> Optional[Literal["operational", "down"]]:
        """Return the availability status populated by the v1 generator."""
        return self._source_link_status

    @computed_field
    @property
    def source_link_type(self) -> Literal["doi", "other"]:
        """Classify DOI resolver links separately from other source URLs."""
        hostname = (urlsplit(self.source_link).hostname or "").lower()
        if hostname in {"doi.org", "dx.doi.org", "www.doi.org"}:
            return "doi"
        return "other"

    @computed_field
    @property
    def source_companions(self) -> List[str]:
        """Return keys of other indices generated from the same source link."""
        return list(self._source_companions)

    def set_source_link_status(self, status):
        """Set the generated availability status after checking the URL."""
        if status not in {"operational", "down"}:
            raise ValueError("Invalid source_link_status.")
        self._source_link_status = status

    def set_source_companions(self, companions):
        """Set the generated catalogue keys that share this source link."""
        if not all(isinstance(companion, str) for companion in companions):
            raise ValueError("Invalid source_companions.")
        self._source_companions = list(companions)


class ConstantDefinition(BaseModel):
    """Contributor-provided metadata for one formula constant."""

    description: StrictStr
    default_value: Optional[StrictNumber] = None
    suggested_values: Optional[SuggestedValues] = None
    suggested_range: Optional[NumericRange] = None

    model_config = ConfigDict(extra="forbid")

    @model_serializer
    def serialize_definition(self):
        """Omit the optional default when the contributor did not provide one."""
        definition = {"description": self.description}
        if self.default_value is not None:
            definition["default_value"] = self.default_value
        if self.suggested_values is not None:
            definition["suggested_values"] = self.suggested_values
        if self.suggested_range is not None:
            definition["suggested_range"] = self.suggested_range
        return definition


class ExternalVariableDefinition(BaseModel):
    """Contributor-provided description for one external formula variable."""

    description: StrictStr

    model_config = ConfigDict(extra="forbid")


class ReductionDefinition(BaseModel):
    """Execution context shared by reductions over one formula dimension."""

    scope: Literal["aoi", "scene"]

    model_config = ConfigDict(extra="forbid")


class Classification(BaseModel):
    """Authored and generated classification metadata for one index."""

    application_domain: str
    sensing_modalities: Optional[List[str]] = None
    family: Optional[List[str]] = None

    model_config = ConfigDict(extra="forbid")

    @field_validator("application_domain")
    @classmethod
    def check_application_domain(cls, value):
        """Require one supported contributor-provided application domain."""
        supported = set(ApplicationDomain._value2member_map_)
        if value not in supported:
            raise ValueError(
                "Invalid application_domain. Supported values: "
                + ", ".join(sorted(supported))
            )
        return value

    @field_validator("sensing_modalities")
    @classmethod
    def check_sensing_modalities(cls, value):
        """Validate generated sensing modalities when they are populated."""
        if value is None:
            return value
        supported = set(SensingModality._value2member_map_)
        if not value or len(value) != len(set(value)):
            raise ValueError("sensing_modalities must be a non-empty unique list.")
        if not set(value) <= supported:
            raise ValueError(
                "Invalid sensing_modalities. Supported values: "
                + ", ".join(sorted(supported))
            )
        return value

    @field_validator("family")
    @classmethod
    def check_family(cls, value):
        """Validate optional contributor-provided index families."""
        if value is None:
            return value
        supported = set(IndexFamily._value2member_map_)
        if not value or len(value) != len(set(value)):
            raise ValueError("family must be a non-empty unique list.")
        if not set(value) <= supported:
            raise ValueError(
                "Invalid family. Supported values: "
                + ", ".join(sorted(supported))
            )
        return value


class SpectralIndex(BaseModel):
    """
    Python dataclass for Spectral Indices
    """

    contributor: str
    acronym: str
    source: Source
    name: str
    formula: str
    bands: Optional[List[str]] = None
    polarizations: Optional[List[str]] = None
    constants: Optional[Dict[str, ConstantDefinition]] = None
    external_variables: Optional[Dict[str, ExternalVariableDefinition]] = None
    reductions: Optional[Dict[Literal["space"], ReductionDefinition]] = None
    classification: Classification
    date_of_addition: date

    model_config = ConfigDict(extra="forbid")

    @field_validator("acronym")
    @classmethod
    def check_acronym(cls, value):
        """Ensure the index acronym does not contain whitespace."""
        if re.search(r"\s+", value):
            raise ValueError("acronym must not contain spaces.")
        return value

    @field_validator("formula")
    @classmethod
    def check_formula(cls, value):
        """Validate formula syntax and ensure every variable is registered."""
        variables = parse_formula_variables(value)

        supported_variables = {
            *Bands._value2member_map_.keys(),
            *Polarizations._value2member_map_.keys(),
            *Constants._value2member_map_.keys(),
            *External._value2member_map_.keys(),
        }
        unsupported_variables = [
            variable
            for variable in variables
            if variable not in supported_variables
            and not is_hyperspectral_band(variable)
        ]
        if unsupported_variables:
            variable_names = ", ".join(sorted(supported_variables))
            raise ValueError(
                "Invalid variables in formula: "
                + ", ".join(unsupported_variables)
                + ". SpectralIndex supports registered variables ("
                + variable_names
                + ") and hyperspectral reflectance bands R300 through R2500 "
                + "or inclusive wavelength ranges such as R750_800."
            )

        return value

    @model_validator(mode="after")
    def check_constants_match_formula(self):
        """Require definitions for exactly the constants used by the formula."""
        formula_constants = {
            variable
            for variable in parse_formula_variables(self.formula)
            if variable in Constants._value2member_map_
        }
        provided_constants = set(self.constants or {})
        missing_constants = sorted(formula_constants - provided_constants)
        extra_constants = sorted(provided_constants - formula_constants)

        errors = []
        if missing_constants:
            errors.append("missing: " + ", ".join(missing_constants))
        if extra_constants:
            errors.append("not used by formula: " + ", ".join(extra_constants))
        if errors:
            raise ValueError(
                "Invalid constants definitions (" + "; ".join(errors) + ")."
            )

        return self

    @model_validator(mode="after")
    def check_external_variables_match_formula(self):
        """Require definitions for exactly the externals used by the formula."""
        formula_externals = {
            variable
            for variable in parse_formula_variables(self.formula)
            if variable in External._value2member_map_
        }
        provided_externals = set(self.external_variables or {})
        missing_externals = sorted(formula_externals - provided_externals)
        extra_externals = sorted(provided_externals - formula_externals)

        errors = []
        if missing_externals:
            errors.append("missing: " + ", ".join(missing_externals))
        if extra_externals:
            errors.append("not used by formula: " + ", ".join(extra_externals))
        if errors:
            raise ValueError(
                "Invalid external variable definitions (" + "; ".join(errors) + ")."
            )

        return self

    @model_validator(mode="after")
    def check_reductions_match_formula(self):
        """Require contexts for exactly the reduction dimensions in the formula."""
        formula_dimensions = set(
            parse_formula_reduction_dimensions(self.formula)
        )
        provided_dimensions = set(self.reductions or {})
        missing_dimensions = sorted(formula_dimensions - provided_dimensions)
        extra_dimensions = sorted(provided_dimensions - formula_dimensions)

        errors = []
        if missing_dimensions:
            errors.append("missing: " + ", ".join(missing_dimensions))
        if extra_dimensions:
            errors.append("not used by formula: " + ", ".join(extra_dimensions))
        if errors:
            raise ValueError(
                "Invalid reduction definitions (" + "; ".join(errors) + ")."
            )

        return self

    @field_validator("contributor")
    @classmethod
    def check_contributor(cls, value):
        """Ensure the contributor is provided as an email or GitHub profile URL."""
        # regex to detect emails or github profiles.
        email_regex = r"^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"
        github_regex = r"(?:https?://)?(?:www[.])?github[.]com/[\w-]+/?"
        full_regex = "%s|%s" % (email_regex, github_regex)
        # Check if it is a correct email address or GitHub profile.
        if not re.match(full_regex, value):
            raise ValueError("contributor is neither a GitHub profile nor an email.")
        return value
