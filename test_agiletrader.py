# test_agiletrader.py
"""
Tests for AgileTrader module.
"""

import unittest
from agiletrader import AgileTrader

class TestAgileTrader(unittest.TestCase):
    """Test cases for AgileTrader class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AgileTrader()
        self.assertIsInstance(instance, AgileTrader)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AgileTrader()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
