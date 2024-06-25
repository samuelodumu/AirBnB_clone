#!/usr/bin/python3
"""contains "TestBaseModel" class"""

from models.base_model import BaseModel
import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """contains test functions for `BaseModel`"""
    def test_uuid(self):
        """tests the uniqueness of instance ids"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertNotEqual(b1.id, b2.id)
        self.assertTrue(hasattr(b1, "id"))
        self.assertIsInstance(b1.id, str)

    def test_str(self):
        """tests for __str__ function"""
        b1 = BaseModel()
        str_rep = b1.__str__()
        self.assertEqual(str_rep, b1.__str__())
        self.assertIsNotNone(b1.__str__())
        self.assertIsInstance(b1.__str__(), str)

    def test_save(self):
        """tests the save function"""
        b1 = BaseModel()
        updated_at = b1.save()
        self.assertEqual(updated_at, b1.updated_at)
        self.assertIsNotNone(b1.save())
        self.assertIsInstance(b1.updated_at, datetime.datetime)

    def test_to_dict(self):
        """tests the to_dict function"""
        b1 = BaseModel()
        instance_dict_rep = b1.to_dict()
        self.assertIsInstance(instance_dict_rep, dict)
        self.assertIsInstance(instance_dict_rep["created_at"], str)
        self.assertIsInstance(instance_dict_rep["updated_at"], str)
        self.assertIsNotNone(b1.to_dict())
