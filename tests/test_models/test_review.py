#!/usr/bin/python3
"""
Unittest for Review class
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def test_instance_creation(self):
        """Test if an instance of Review is created correctly"""
        obj = Review()
        self.assertIsInstance(obj, Review)
        self.assertEqual(obj.place_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.text, "")


if __name__ == "__main__":
    unittest.main()
