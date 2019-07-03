#!/usr/bin/python3
import unittest
import pep8
import os
from models.__init__ import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


def setUpModule():
    """ """
    pass


def tearDownModule():
    """ """
    pass


class TestStringMethods(unittest.TestCase):
    """ Check the pep8 """
    def testpep8(self):
        style = pep8.StyleGuide(quiet=True)
        file1 = "models/base_model.py"
        file2 = "tests/test_models/test_base_model.py"
        check = style.check_files([file1, file2])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")


class TestModels(unittest.TestCase):

    def setUp(self):
        """ Set a variable """
        self.my_model = BaseModel()
        print("setUp")

    def tearDown(self):
        """ End variable """
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """ Set a Class """
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """ Del a Class"""
        print("tearDownClass")

    def test_models_doc(self):
        """ Check the documentation """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_models_name(self):
        """ Check if name is create"""
        self.my_model.name = 'Holberton'
        self.assertEqual(self.my_model.name, 'Holberton')

    def test_models_number(self):
        """ Check if the number is create """
        self.my_model.my_number = 55
        self.assertEqual(self.my_model.my_number, 55)

    def test_models_exist(self):
        """ Check if the json file and methods exists """
        self.assertTrue(os.path.isfile('my_file.json'))
        self.assertTrue(hasattr(self.my_model, "__init__"))
        self.assertTrue(hasattr(self.my_model, "__str__"))
        self.assertTrue(hasattr(self.my_model, "save"))
        self.assertTrue(hasattr(self.my_model, "to_dict"))

    def test_models_not_empty(self):
        """ Check if the json file is not empty """
        self.assertTrue('my_file.json')

    def test_models_save(self):
        """ Check if the save function works """
        self.my_model.name = "Halo"
        self.my_model.save()
        storage.reload()
        storage.all()
        self.assertTrue(storage.all(), "Halo")
        self.assertTrue(hasattr(self.my_model, 'save'))
        self.assertNotEqual(self.my_model.created_at,
                            self.my_model.updated_at)

if __name__ == '__main__':
    unittest.main()
