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
        ("tanh((N - R) / (N + R))", ["N", "R"]),
        ("max(tanh(N), R)", ["N", "R"]),
        ("log(N)", ["N"]),
        ("log(N / R)", ["N", "R"]),
        ("log(max(N, R))", ["N", "R"]),
        ("kernel(N, N) - kernel(N, R)", ["N", "R"]),
        (
            "spatial_max(S2) * B / (spatial_min(B) + spatial_mean(S2))",
            ["S2", "B"],
        ),
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
        "tanh()",
        "tanh(N, R)",
        "log()",
        "log(N, R)",
        "kernel()",
        "kernel(N)",
        "kernel(N, R, B)",
        "kernel(N, other=R)",
        "spatial_max()",
        "spatial_min(N, R)",
        "spatial_mean(N, scope)",
        "spatial_max(N, scope='aoi')",
        "math.tanh(N)",
        "math.log(N)",
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
