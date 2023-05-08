"""This module tests Helpers.py using unittest."""
import unittest
from helpers import *
from customtkinter import CTkFrame, CTkImage

class TestHelpers(unittest.TestCase):
    
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_assets(self):
        self.assertIn(Assets.DARK_JOURNAL.name, Assets.list("name"))
        self.assertIn("icons", str(Assets.NPX_LOGO))
    
    def test_custom_image(self):
        pass
    
    def test_custom_tab_button(self):
        pass
    
    def test_session_data(self):
        data = SessionData(username="Erick", password="1234", type=StartUp.LOG_IN)
        self.assertIsInstance(data.cookie, tuple)
        self.assertEqual(data.password, "1234")


if __name__ == '__main__':
    unittest.main()
