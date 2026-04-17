# test_wasabimixer.py
"""
Tests for WasabiMixer module.
"""

import unittest
from wasabimixer import WasabiMixer

class TestWasabiMixer(unittest.TestCase):
    """Test cases for WasabiMixer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WasabiMixer()
        self.assertIsInstance(instance, WasabiMixer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WasabiMixer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
