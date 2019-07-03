#!/usr/bin/python3
import unittest
import pep8
from models.user import User
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
        file1 = "models/review.py"
        file2 = "tests/test_models/test_review.py"
        check = style.check_files([file1, file2])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")


class TestModels(unittest.TestCase):
    """ Funtion to test the BaseModel"""

    def setUp(self):
        """ Set a variable """
        self.review_1 = Review()
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

    def test_user_doc(self):
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.__init__.__doc__)

    def test_place_city(self):
        """ check if the methods exists """
        self.assertTrue(hasattr(self.place_1, "__init__"))
        self.assertTrue(hasattr(self.place_1, "text"))
        self.assertTrue(hasattr(self.place_1, "user_id"))
        self.assertTrue(hasattr(self.place_1, "place_id"))

    def test_user_instance(self):
        """ check if user_1 is instance of User """
        self.assertIsInstance(self.review_1, Review)

if __name__ == '__main__':
    unittest.main()
