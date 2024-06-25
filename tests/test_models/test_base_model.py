#!/usr/bin/python3
"""contains "TestBaseModel" class"""

from models.base_model import BaseModel
import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """contains test functions for `BaseModel`"""

    def setUp(self):
        self.bm1 = BaseModel()
        self.bm1.name = "Model 1"
        self.bm2 = BaseModel()
        self.bm2.name = "Model 2"

    def tearDown(self):
        del self.bm1
        del self.bm2

    def test_uuid(self):
        """tests the uniqueness of instance ids"""
        self.assertIsInstance(self.bm1, BaseModel)
        self.assertTrue(hasattr(self.bm1, "id"))
        self.assertNotEqual(self.bm1.id, self.bm2.id)
        self.assertIsInstance(self.bm1.id, str)

    def test_str(self):
        """tests for __str__ function"""
        str_rep = str(self.bm1)
        expected_str_rep = \
            f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        self.assertEqual(str_rep, str(self.bm1))

    def test_save(self):
        """tests the save function"""
        updated_at = self.bm1.save()
        self.assertEqual(updated_at, self.bm1.updated_at)
        self.assertIsNotNone(self.bm1.save())
        self.assertIsInstance(self.bm1.updated_at, datetime.datetime)

    def test_to_dict(self):
        """tests the to_dict function"""
        instance_dict_rep = self.bm1.to_dict()
        self.assertIsInstance(instance_dict_rep, dict)
        self.assertIsInstance(instance_dict_rep["created_at"], str)
        self.assertIsInstance(instance_dict_rep["updated_at"], str)
        self.assertIsNotNone(self.bm1.to_dict())
