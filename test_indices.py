import unittest
from indices import indices

class Test(unittest.TestCase):
    """Tests for the Awesome List of Spectral Indices for Google Earth Engine."""
    
    def test_Indices(self):
        """Test the indices list"""        
        self.assertIsInstance(indices, list)
        
if __name__ == '__main__':
    unittest.main()