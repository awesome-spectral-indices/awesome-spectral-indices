import sys
import unittest

sys.path.append("./")
from src.indices import spindex, SpectralIndices
from src.SpectralIndex import parse_formula_variables


class Test(unittest.TestCase):
    """Tests for the Awesome List of Spectral Indices for Google Earth Engine."""

    def test_Indices(self):
        """Test the indices list"""
        self.assertIsInstance(spindex, SpectralIndices)

    def test_formula_variables(self):
        """Test formula variable extraction"""
        self.assertEqual(
            parse_formula_variables("g * (N - R) / (N + C1 * R - C2 * B + L)"),
            ["g", "N", "R", "C1", "C2", "B", "L"],
        )
        self.assertEqual(parse_formula_variables("max(N, R)"), ["N", "R"])


if __name__ == "__main__":
    unittest.main()
