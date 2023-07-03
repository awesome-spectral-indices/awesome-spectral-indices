import sys
import unittest

sys.path.append("./")
from src.indices import spindex, SpectralIndices


class Test(unittest.TestCase):
    """Tests for the Awesome List of Spectral Indices for Google Earth Engine."""

    def test_Indices(self):
        """Test the indices list"""
        self.assertIsInstance(spindex, SpectralIndices)


if __name__ == "__main__":
    unittest.main()
