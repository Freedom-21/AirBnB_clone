#!/usr/bin/python3
"""
Unittest for City class
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """test cases for the City class"""

    def test_instance_creation(self):
        """test if an instance of City is created correctly"""
        obj = City()
        self.assertIsInstance(obj, City)
        self.assertEqual(obj.state_id, "")
        self.assertEqual(obj.name, "")


if __name__ == "__main__":
    unittest.main()
