"""This module tests App using unittest."""
import unittest
from app import App
from customtkinter import CTkFrame
from helpers import View, SessionData, SessionIssue, StartUp, SQLTable

class TestApp(unittest.TestCase):
    """Test classes and methods using UnitTest."""

    def setUp(self):
        self.app = App()

    def tearDown(self):
        self.app.destroy()

    def test_app(self):
        self.assertIsInstance(self.app, App)
        self.assertTupleEqual(self.app.login_view_size, (500, 500))
        self.assertTupleEqual(self.app.main_view_size, (1080, 720))
        self.assertTupleEqual(self.app.resizable(), (False, False))

    def test_show_main_view(self):
        self.app._show_main_view()
        title = "Secret"
        self.assertIn(title, self.app.title())
        self.assertNotEqual(self.app.resizable(), (False, False))

    def test_set_current_view(self):
        title = "Test"
        self.app._set_current_view(title)
        self.assertIsInstance(self.app.current_view, CTkFrame)

    def test_show_login_view(self):
        self.app._show_login_view()
        title = "Login Screen"
        self.assertIn(title, self.app.title())
        pass

    def test_buttons_pressed(self):
        self.app._show_main_view()
        self.app._journal_tab_pressed()
        self.app._planning_tab_pressed()
        self.app._challenges_tab_pressed()
        self.assertIsInstance(self.app.current_view, CTkFrame)

    def test_processed_data_issue(self):
        data = SessionData("Erick", "", StartUp.LOG_IN)
        self.assertEqual(self.app._processed_data_issue(data), SessionIssue.EMPTY_PASSWORD)
        data = SessionData("", "1234", StartUp.LOG_IN)
        self.assertEqual(self.app._processed_data_issue(data), SessionIssue.EMPTY_USERNAME)
        data = SessionData("Erick", "1234", StartUp.SIGN_IN)
        self.assertIs(self.app._processed_data_issue(data), SessionIssue.USERNAME_TAKEN)

        data = SessionData("AC", "Password", StartUp.SIGN_IN)
        self.assertEqual(self.app._processed_data_issue(data), SessionIssue.MISSING_SPECIAL)
        data = SessionData("AC", "Password1", StartUp.SIGN_IN)
        self.assertEqual(self.app._processed_data_issue(data), SessionIssue.MISSING_SPECIAL)

    def test_login_signin_pressed(self):
        data = SessionData("", "", StartUp.LOG_IN)
        self.app._login_signin_pressed(data)
        
        data = SessionData("Erick", "", StartUp.LOG_IN)
        self.app._login_signin_pressed(data)
        
        data = SessionData("Erick", "1234", StartUp.LOG_IN)
        self.app._login_signin_pressed(data)
        
        data = SessionData("Erick", "1234", StartUp.SIGN_IN)
        self.app._login_signin_pressed(data)

if __name__ == '__main__':
    unittest.main()
