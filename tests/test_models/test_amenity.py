#!/usr/bin/python3
"""
Unittest for Amenity class
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def test_instance_creation(self):
        """Test if an instance of Amenity is created correctly"""
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)
        self.assertEqual(obj.name, "")


if __name__ == "__main__":
    unittest.main()
