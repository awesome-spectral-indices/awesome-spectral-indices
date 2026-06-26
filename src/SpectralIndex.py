import ast
import re
import orjson

from pydantic import BaseModel, validator
from src.utils import Bands, IndexType
from datetime import date
from typing import Optional, List


def orjson_dumps(value, *, default):
    """
    orjson.dumps returns bytes, to match standard json.dumps we need to decode
    """
    return orjson.dumps(value, default=default).decode()


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
        if not isinstance(node.func, ast.Name) or node.func.id not in self.allowed_functions:
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


class SpectralIndex(BaseModel):
    """
    Python dataclass for Spectral Indices
    """

    contributor: str
    short_name: str
    reference: str
    long_name: str
    formula: str
    bands: Optional[List] = None
    platforms: Optional[List] = None
    application_domain: str
    date_of_addition: date

    class Config:
        extra = "forbid"
        json_loads = orjson.loads
        json_dumps = orjson_dumps

    @validator("short_name")
    def check_short_name(cls, value):
        """Ensure the short index identifier does not contain whitespace."""
        if re.search(r"\s+", value):
            raise ValueError("short_name must not contain spaces.")
        return value

    @validator("formula")
    def check_formula(cls, value):
        """Validate formula syntax and ensure all variables are supported bands."""
        variables = parse_formula_variables(value)  # obtain band names (e.g. ["R", "G"])

        # check if the variables are in "Bands".
        if not all(elem in Bands._value2member_map_ for elem in variables):
            band_names = ", ".join(Bands._value2member_map_.keys())
            raise ValueError(
                "Invalid variables in formula. SpectralIndex only supports the following variables: "
                + band_names
            )

        return value

    @validator("contributor")
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

    @validator("application_domain")
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
