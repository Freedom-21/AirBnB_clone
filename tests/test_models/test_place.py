#!/usr/bin/python3
"""
Unittest for Place class
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def test_instance_creation(self):
        """Test if an instance of Place is created correctly"""
        obj = Place()
        self.assertIsInstance(obj, Place)
        self.assertEqual(obj.name, "")
        self.assertEqual(obj.city_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.description, "")
        self.assertEqual(obj.number_rooms, 0)
        self.assertEqual(obj.number_bathrooms, 0)
        self.assertEqual(obj.max_guest, 0)
        self.assertEqual(obj.price_by_night, 0)
        self.assertEqual(obj.latitude, 0.0)
        self.assertEqual(obj.longitude, 0.0)


if __name__ == "__main__":
    unittest.main()
