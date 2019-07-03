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
        file1 = "models/user.py"
        file2 = "tests/test_models/test_user.py"
        check = style.check_files([file1, file2])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")


class TestModels(unittest.TestCase):
    """ Funtion to test the BaseModel"""

    def setUp(self):
        """ Set a variable """

        self.user_1 = User()
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

    def test_user_name(self):
        """ check if the name is create """

        self.user_1.name = 'Jeniffer'
        self.assertEqual(self.user_1.name, 'Jeniffer')

    def test_user_lastname(self):
        """ chaeck if the lastname is create """

        self.user_1.lastname = "Vanegas"
        self.assertEqual(self.user_1.lastname, "Vanegas")

    def test_user_email(self):
        """ chaeck if the email is create """

        self.user_1.email = 'airbnb@holbertonshool.com'
        self.assertEqual(self.user_1.email, 'airbnb@holbertonshool.com')

    def test_user_password(self):
        """ chaeck if the password is create """

        self.user_1.password = "root"
        self.assertEqual(self.user_1.password, "root")

    def test_user_instance(self):
        """ check if user_1 is instance of User """

        self.assertIsInstance(self.user_1, User)

if __name__ == '__main__':
    unittest.main()