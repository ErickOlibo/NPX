"""This module tests Login View using unittest."""
import unittest
from gui.login_view import LoginView
from customtkinter import CTkButton
from app import App

class TestLoginView(unittest.TestCase):
    """Test classes and methods using UnitTest."""
    def setUp(self):
        
        def test():
            pass
        self.app = App()
        self.view = LoginView(self.app, test)

    def tearDown(self):
        self.view.destroy()
    
    
    def test_login_view(self):
        self.assertIsInstance(self.view._login_button, CTkButton)
        cred = ("Erick", "This")
        self.assertEqual("Login", self.view._login_button._text)


    # def test_atach_logo_to_login_view(self):
    #     #self.view._attach_logo_to_login_view()
    #     self.assertIsInstance(self.view._logo_label, CTkLabel)
    
    # def test_atach_title_credentials(self):
    #     pass


if __name__ == '__main__':
    unittest.main()
