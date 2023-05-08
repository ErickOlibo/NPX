"""This module tests App using unittest."""
import unittest
from app import App
from customtkinter import CTkFrame
from helpers import SessionData, StartUp, View

class TestApp(unittest.TestCase):
    """Test classes and methods using UnitTest."""

    def setUp(self):
        self.app = App()

    def tearDown(self):
        self.app.destroy()

    def test_app(self):
        self.assertIsInstance(self.app, App)
        self.assertTupleEqual(self.app.login_view_size, (500, 500))
        self.assertTupleEqual(self.app.main_view_size, (800, 600))
        self.assertTupleEqual(self.app.resizable(), (False, False))

    def test_show_main_view(self):
        self.app._show_main_view()
        title = "Secret"
        self.assertIn(title, self.app.title())
        self.assertNotEqual(self.app.resizable(), (True, True))

    def test_set_current_view(self):
        title = "Test"
        self.app._set_current_view(title)
        self.assertIsInstance(self.app.current_view, CTkFrame)

    def test_show_login_view(self):
        self.app._show_login_view()
        title = "Login Screen"
        self.assertIn(title, self.app.title())

    def test_login_signin_pressed(self):
        data = SessionData("", "", StartUp.LOG_IN)
        self.app._login_signin_pressed(data)

        data = SessionData("Erick", "", StartUp.LOG_IN)
        self.app._login_signin_pressed(data)

        data = SessionData("Erick", "1234", StartUp.LOG_IN)
        self.app._login_signin_pressed(data)

        data = SessionData("Erick", "1234", StartUp.SIGN_IN)
        self.app._login_signin_pressed(data)

        data = SessionData("AC9", "Password", StartUp.SIGN_IN)
        self.app._login_signin_pressed(data)
    
        data = SessionData("AC9", "Password1", StartUp.SIGN_IN)
        self.app._login_signin_pressed(data)
    
        data = SessionData("AC9", "Pass1!", StartUp.SIGN_IN)
        self.app._login_signin_pressed(data)
    
        data = SessionData("AC9", "password1!", StartUp.SIGN_IN)
        self.app._login_signin_pressed(data)
    
        data = SessionData("AC9", "PASSWORD1!", StartUp.SIGN_IN)
        self.app._login_signin_pressed(data)
    
        data = SessionData("AC9", "Password!", StartUp.SIGN_IN)
        self.app._login_signin_pressed(data)

        data = SessionData("AC", "Password!2", StartUp.SIGN_IN)
        self.app._login_signing_pressed(data)

        data = SessionData("ACCCCCCCCCCCCCCC", "Password!2", StartUp.SIGN_IN)
        self.app._login_signing_pressed(data)

        data = SessionData("ACCCC", "Password!1", StartUp.SIGN_IN)
        self.app._login_signin_pressed(data)


if __name__ == '__main__':
    unittest.main()
