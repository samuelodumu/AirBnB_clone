#!/usr/bin/python3
"""contains "TestBaseModel" class"""

from models.base_model import BaseModel
import datetime as dt
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

    def test_kwargs(self):
        """tests that kwargs can be used to construct a Basemodel object"""
        b1 = BaseModel(id='fe1f3a30-17e4-4d36-b8ec-c94f1ffcvr3g',
                       created_at='2024-06-25T18:44:33.783706',
                       updated_at='2024-06-25T18:44:33.783733',
                       __class__='BaseModel')
        self.assertIsInstance(b1, BaseModel)
        self.assertIsInstance(b1.created_at, dt.datetime)
        self.assertIsInstance(b1.updated_at, dt.datetime)

    def test_str(self):
        """tests for __str__ function"""
        str_rep = str(self.bm1)
        expected_str_rep = \
            f"[BaseModel] ({self.bm1.id}) {self.bm1.__dict__}"
        self.assertEqual(str_rep, expected_str_rep)

    def test_save(self):
        """tests the save function"""
        updated_at = self.bm1.save()
        self.assertEqual(updated_at, self.bm1.updated_at)
        self.assertIsNotNone(self.bm1.save())
        self.assertIsInstance(self.bm1.updated_at, dt.datetime)

    def test_to_dict(self):
        """tests the to_dict function"""
        instance_dict_rep = self.bm1.to_dict()
        self.assertIsInstance(instance_dict_rep, dict)
        self.assertIsInstance(instance_dict_rep["created_at"], str)
        self.assertIsInstance(instance_dict_rep["updated_at"], str)
        self.assertIsNotNone(self.bm1.to_dict())
