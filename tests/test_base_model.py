#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import time


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_instance_creation(self):
        """Test creation of BaseModel instance."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertEqual(my_model.created_at, my_model.updated_at)

    def test_str_method(self):
        """Test the __str__ method."""
        my_model = BaseModel()
        expected_output = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(str(my_model), expected_output)

    def test_save_method(self):
        """Test the save method."""
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        time.sleep(1)  # Sleep to ensure a time difference
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method."""
        my_model = BaseModel()
        obj_dict = my_model.to_dict()
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["id"], my_model.id)
        self.assertEqual(obj_dict["created_at"], my_model.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"], my_model.updated_at.isoformat())

if __name__ == "__main__":
    unittest.main()

