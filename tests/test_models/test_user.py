#!/usr/bin/python3
"""
unittest for User class
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """test cases for the User class"""

    def test_instance_creation(self):
        """test if an instance of User is created correctly"""
        obj = User()
        self.assertIsInstance(obj, User)
        self.assertEqual(obj.email, "")
        self.assertEqual(obj.password, "")
        self.assertEqual(obj.first_name, "")
        self.assertEqual(obj.last_name, "")


if __name__ == "__main__":
    unittest.main()
