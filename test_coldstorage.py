# test_coldstorage.py
"""
Tests for ColdStorage module.
"""

import unittest
from coldstorage import ColdStorage

class TestColdStorage(unittest.TestCase):
    """Test cases for ColdStorage class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ColdStorage()
        self.assertIsInstance(instance, ColdStorage)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ColdStorage()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
