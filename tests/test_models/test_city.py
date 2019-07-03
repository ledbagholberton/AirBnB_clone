#!/usr/bin/python3
import unittest
import pep8
from models.city import City
from models.engine.file_storage import FileStorage


def setUpModule():
    """ Funtion to set a Module"""
    pass


def tearDownModule():
    """ Function to delete a Module"""
    pass


class TestStringMethods(unittest.TestCase):
    """ Check the pep8 """
    def testpep8(self):
        style = pep8.StyleGuide(quiet=True)
        file1 = "models/city.py"
        file2 = "tests/test_models/test_city.py"
        check = style.check_files([file1, file2])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")


class TestModels(unittest.TestCase):
    """ Funtion to test the BaseModel"""

    def setUp(self):
        """ Set a variable """

        self.city_1 = City()
        print("setUp")

    def tearDown(self):
        """ End variable """

        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """ define class """

        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """ close the class """

        print("tearDownClass")

    def test_city_name(self):
        """ check if the name is create """

        self.city_1.name = 'Paris'
        self.assertEqual(self.city_1.name, 'Paris')


    def test_user_instance(self):
        """ check if user_1 is instance of User """

        self.assertIsInstance(self.city_1, City)

if __name__ == '__main__':
    unittest.main()