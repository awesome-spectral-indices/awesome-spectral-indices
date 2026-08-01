import ast
import re
from datetime import date
from typing import List, Literal, Optional
from urllib.parse import urlsplit

from pydantic import (
    BaseModel,
    ConfigDict,
    PrivateAttr,
    computed_field,
    field_validator,
)

from src.v1.utils import Bands, IndexType


class FormulaVisitor(ast.NodeVisitor):
    """
    Validate a spectral-index formula and collect its variable names.

    The visitor accepts only the small expression language used by the
    catalogue: arithmetic operations, numeric constants, variable names, and
    explicitly allowed functions. It never evaluates the formula.
    """

    allowed_functions = ("max", "min")
    allowed_binary_operators = (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow)
    allowed_unary_operators = (ast.UAdd, ast.USub)

    def __init__(self):
        """Create an empty collector that preserves first-seen variable order."""
        self.variables = []
        self._seen_variables = set()

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
    allowed function names such as ``max`` and ``min``.
    """
    try:
        tree = ast.parse(value, mode="eval")
    except SyntaxError as exc:
        raise ValueError("Invalid formula.") from exc

    visitor = FormulaVisitor()
    visitor.visit(tree)
    return visitor.variables


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

    def set_source_link_status(self, status):
        """Set the generated availability status after checking the URL."""
        if status not in {"operational", "down"}:
            raise ValueError("Invalid source_link_status.")
        self._source_link_status = status


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
    application_domain: str
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
        """Validate formula syntax and ensure all variables are supported bands."""
        variables = parse_formula_variables(
            value
        )  # obtain band names (e.g. ["R", "G"])

        # check if the variables are in "Bands".
        if not all(elem in Bands._value2member_map_ for elem in variables):
            band_names = ", ".join(Bands._value2member_map_.keys())
            raise ValueError(
                "Invalid variables in formula. SpectralIndex only supports the following variables: "
                + band_names
            )

        return value

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

    @field_validator("application_domain")
    @classmethod
    def check_type(cls, value):
        """Ensure the application domain is one of the supported index types."""
        # Obtain names of IndexType enum.
        IndexTypeNames = ", ".join(IndexType._value2member_map_.keys())

        # Check if IndexTtpe is supported.
        if not value in IndexType._value2member_map_:
            raise ValueError(
                "Invalid IndexType. SpectralIndex only supports the following IndexType: "
                + IndexTypeNames
            )
        return value
