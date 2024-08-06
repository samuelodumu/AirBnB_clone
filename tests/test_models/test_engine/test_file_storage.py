#!/usr/bin/python3
"""contains `TestFileStorage` class"""

from models.base_model import BaseModel
import models
import json
import os
import unittest


class TestFileStorage(unittest.TestCase):
    """contains test functions for `FileStorage`"""

    file_path = models.storage._FileStorage__file_path
    objects = models.storage._FileStorage__objects

    def test_class_attributes(self):
        """tests the `__file_path` and `__objects` class attributes"""
        self.assertEqual(self.file_path, 'file.json')
        self.assertIsInstance(self.file_path, str)
        self.assertIsInstance(self.objects, dict)

    def test_all(self):
        """tests the `all()` method"""
        objs_dict = models.storage.all()
        self.assertIs(objs_dict, self.objects)

    def test_new(self):
        """tests the `new()` method"""
        pass

    def test_save(self):
        """tests the `save()` method"""
        pass

    def test_reload(self):
        """tests the `reload()` method"""
        pass
