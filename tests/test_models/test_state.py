#!/usr/bin/python3
"""
unittest for State class
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """test cases for the State class"""

    def test_instance_creation(self):
        """test if an instance of State is created correctly"""
        obj = State()
        self.assertIsInstance(obj, State)
        self.assertEqual(obj.name, "")


if __name__ == "__main__":
    unittest.main()
