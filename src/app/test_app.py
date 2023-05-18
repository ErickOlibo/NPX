"""This module tests App using unittest."""
import unittest
from app import App
from customtkinter import CTkFrame
from helpers import SessionData, StartUp, View
from gui.journal_view import JournalView
from gui.entries_view import EntriesView
from gui.login_view import LoginView

class TestApp(unittest.TestCase):
    """Test classes and methods using UnitTest."""

    def setUp(self):
        self.app = App()

    def tearDown(self):
        self.app.destroy()

    def test_app(self):
        self.assertIsInstance(self.app, App)
        self.assertTupleEqual(self.app.login_view_size, (500, 500))
        self.assertTupleEqual(self.app.main_view_size, (840, 600))
        self.assertTupleEqual(self.app.resizable(), (False, False))

    def test_show_main_view(self):
        # self.app._show_main_view()
        # title = "Secret"
        # self.assertIn(title, self.app.title())
        # self.assertNotEqual(self.app.resizable(), (True, True))
        pass

    def test_set_current_view(self):
        # title = "Test"
        # self.app._set_current_view(title)
        # self.assertIsInstance(self.app.current_view, CTkFrame)
        pass

    def test_show_login_view(self):
        self.app._show_login_view()
        title = "Login Screen"
        self.assertIn(title, self.app.title())

    def test_navigation_button_pressed(self):
        self.app._navigation_button_pressed(View.JOURNAL)
        self.assertIsInstance(self.app._journal_view, JournalView)
        self.app._navigation_button_pressed(View.ENTRIES)
        self.assertIsInstance(self.app._entries_view, EntriesView)
        self.app._navigation_button_pressed(View.LOGOUT)
        self.assertIsInstance(self.app.login_view, LoginView)
        pass


if __name__ == '__main__':
    unittest.main()
