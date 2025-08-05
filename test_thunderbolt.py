# test_thunderbolt.py
"""
Tests for ThunderBolt module.
"""

import unittest
from thunderbolt import ThunderBolt

class TestThunderBolt(unittest.TestCase):
    """Test cases for ThunderBolt class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ThunderBolt()
        self.assertIsInstance(instance, ThunderBolt)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ThunderBolt()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
