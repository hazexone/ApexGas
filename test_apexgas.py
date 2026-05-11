# test_apexgas.py
"""
Tests for ApexGas module.
"""

import unittest
from apexgas import ApexGas

class TestApexGas(unittest.TestCase):
    """Test cases for ApexGas class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ApexGas()
        self.assertIsInstance(instance, ApexGas)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ApexGas()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
