"""This module tests Login View using unittest."""
import unittest
from gui.navigation_bar import NavigationBar
from customtkinter import CTkButton, CTkLabel
from app import App
from helpers import View

class TestNavigationBar(unittest.TestCase):
    """Test classes and methods using UnitTest."""
    def setUp(self):
        
        def test():
            pass
        self.app = App()
        self.nav_bar = NavigationBar(self.app, test, test, test, test)

    def tearDown(self):
        self.nav_bar.destroy()
    
    # Did not managed to implement this testing
    # def test_navigation_bar(self):
    #     self.nav_bar._navigation_icons()
    #     self.nav_bar.set_active_button(View.JOURNAL)
    #     self.assertIsNone(self.nav_bar.journal_button.grid())
    #     self.assertIn("USUKU", self.nav_bar.top_logo._text)
    #     values = ['Light', 'System', 'Dark']
    #     self.assertEqual(self.nav_bar.mode_menu._value_list, values)
    #     pass



if __name__ == '__main__':
    unittest.main()
