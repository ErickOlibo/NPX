"""This module tests sql_handler.py using unittest."""
import unittest
from sqlite3 import Connection, Error
from helpers import *
from sql_handler import SQLHandler


class TestSQLHandler(unittest.TestCase):

    def setUp(self):
        self.handler = SQLHandler()

    def tearDown(self):
        self.handler.close_connection()
    
    def test_create_connection(self):
        self.assertIsInstance(self.handler._conn, Connection)
    
    def test_verified_user(self):
        data = SessionData("Thomas", "12345", StartUp.LOG_IN)
        self.handler.insert_into_userdata(data)
        self.assertFalse(self.handler.verified_user("Erick", "fake"))
        self.assertTrue(self.handler.verified_user("Thomas", "12345"))
    
    def test_username_taken(self):
        self.assertTrue(self.handler.username_taken("Thomas"))
        self.assertFalse(self.handler.username_taken("Mario"))


if __name__ == '__main__':
    unittest.main()
