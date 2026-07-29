import pytest

from src.v1.SpectralIndex import parse_formula_variables


@pytest.mark.parametrize(
    ("formula", "variables"),
    [
        ("(N - R) / (N + R)", ["N", "R"]),
        (
            "g * (N - R) / (N + C1 * R - C2 * B + L)",
            ["g", "N", "R", "C1", "C2", "B", "L"],
        ),
        ("max(N, R) - min(G, B)", ["N", "R", "G", "B"]),
        ("-(N ** 2.0) + +R", ["N", "R"]),
        ("N + N + R + N", ["N", "R"]),
    ],
)
def test_parse_formula_variables_accepts_catalogue_expression_language(
    formula, variables
):
    assert parse_formula_variables(formula) == variables


@pytest.mark.parametrize(
    "formula",
    [
        "N +",
        "N % R",
        "N // R",
        "N < R",
        "N and R",
        "abs(N)",
        "max(N, key=R)",
        "N.real",
        "[N, R]",
        "'N'",
        "True",
        "lambda: N",
    ],
)
def test_parse_formula_variables_rejects_unsupported_syntax(formula):
    with pytest.raises(ValueError, match="Invalid formula"):
        parse_formula_variables(formula)
