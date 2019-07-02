#!/usr/bin/python3
import unittest
import pep8
import os
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
        """ """
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def test_models_name(self):
        self.my_model.name = 'Holberton'
        self.assertEqual(self.my_model.name, 'Holberton')

    def test_models_number(self):
        self.my_model.my_number = 55
        self.assertEqual(self.my_model.my_number, 55)

    def test_models_exist(self):
        self.assertTrue(os.path.isfile('my_file.json'))

if __name__ == '__main__':
    unittest.main()
