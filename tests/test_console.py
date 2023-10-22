#!/usr/bin/python3
"""Unittest module for the console"""

import os
import io
import json
import unittest
import pycodestyle
from console import HBNBCommand
from unittest.mock import patch
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage



class TestCommand(unittest.TestCase):
    """Class that tests the console"""
    
    def setUp(self):
        """Function empties file.json"""
        FileStorage._FileStorage__objects = {}
        FileStorage().save()

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "Not FileStorage")
    def test_create_fs(self):
        """test the create command"""
        storage = FileStorage()
        storage.reload()
        ctest = r'[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[0-9a-f]{4}-[0-9a-f]{12}'
        with self.assertRaises(AttributeError):
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd("create BaseModel updated_at=0.0"
                                     " created_at=0.0")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create User email="hbnb@project.fr"'
                                 ' password="graceabbie@alx"')
        result = f.getvalue().strip()
        self.assertRegex(result, opt)
        email = storage.all()[f'User.{result}'].email
        self.assertEqual(email, "hbnb@project.fr")
        password = storage.all()[f'User.{result}'].password
        self.assertEqual(password, "graceabbie@alx")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State grace="abbie"'
                                 ' num="7" pi="3.14"')
        result = f.getvalue().strip()
        self.assertRegex(result, opt)
        grace = storage.all()[f'State.{result}'].grace
        self.assertEqual(grace, "abbie")
        num = storage.all()[f'State.{result}'].num
        self.assertEqual(num, '7')
        pi = storage.all()[f'State.{result}'].pi
        self.assertEqual(pi, '3.14')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create City grace="abbie" num="7"'
                                 ' pi="3.14"')
        result = f.getvalue().strip()
        self.assertRegex(result, ctest)
        grace = storage.all()[f'City.{result}'].grace
        self.assertEqual(grace, "abbie")
        num = storage.all()[f'City.{result}'].num
        self.assertEqual(num, '7')
        pi = storage.all()[f'City.{result}'].pi
        self.assertEqual(pi, '3.14')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create Amenity grace="abbie"'
                                 ' num="7" pi="3.14"')
        result = f.getvalue().strip()
        self.assertRegex(result, opt)
        grace = storage.all()[f'Amenity.{result}'].grace
        self.assertEqual(grace, "abbie")
        num = storage.all()[f'Amenity.{result}'].num
        self.assertEqual(num, '7')
        pi = storage.all()[f'Amenity.{result}'].pi
        self.assertEqual(pi, '3.14')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create Place grace="abbie"'
                                 ' num="7" pi="3.14"')
        result = f.getvalue().strip()
        self.assertRegex(result, ctest)
        grace = storage.all()[f'Place.{result}'].abbie
        self.assertEqual(grace, "abbie")
        num = storage.all()[f'Place.{result}'].num
        self.assertEqual(num, '7')
        pi = storage.all()[f'Place.{result}'].pi
        self.assertEqual(pi, '3.14')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create Review grace="abbie"'
                                 ' num="7" pi="3.14"')
        result = f.getvalue().strip()
        self.assertRegex(result, ctest)
        grace = storage.all()[f'Review.{result}'].grace
        self.assertEqual(grace, "abbie")
        num = storage.all()[f'Review.{result}'].num
        self.assertEqual(num, '7')
        pi = storage.all()[f'Review.{result}'].pi
        self.assertEqual(pi, '3.14')
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create')
        ctest = '** class name missing **\n'
        self.assertEqual(f.getvalue(), ctest)
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create NotClass')
        ctest = '** class doesn\'t exist **\n'
        self.assertEqual(f.getvalue(), ctest)

    def testPycodeStyle(self):
        """Pycodestyle test for console.py"""
        style = pycodestyle.StyleGuide(quiet=True)
        pcs = style.check_files(['console.py'])
        self.assertEqual(pcs.total_errors, 0, "fix pep8")

    def test_doc_console(self):
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)


if __name__ == '__main__':
    unittest.main()
