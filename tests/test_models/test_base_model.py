#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_instance_creation(self):
        """Test if an instance of BaseModel is created correctly"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str_method(self):
        """Test the __str__ method"""
        obj = BaseModel()
        expected_str = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_str)

    def test_save_method(self):
        """Test the save method updates updated_at attribute"""
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_kwargs_init(self):
        """Test initialization with kwargs"""
        obj = BaseModel()
        obj.name = "Test"
        obj.number = 42
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertEqual(new_obj.id, obj.id)
        self.assertEqual(new_obj.created_at, obj.created_at)
        self.assertEqual(new_obj.updated_at, obj.updated_at)
        self.assertEqual(new_obj.name, obj.name)
        self.assertEqual(new_obj.number, obj.number)


if __name__ == "__main__":
    unittest.main()
