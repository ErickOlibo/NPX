"""This module tests Entries View using unittest."""
import unittest
import customtkinter
from gui.entries_view import EntriesView
from helpers import EntriesData

class TestApp(unittest.TestCase):
    """Test classes and methods using UnitTest."""
    
    def setUp(self):
        self.master = customtkinter.CTk()
        pass
    
    def tearDown(self):
        self.master.destroy()
    
    def test_entries_view(self):
        entries_view = EntriesView(self.master, "Erick")
        self.assertIsInstance(entries_view, customtkinter.CTkFrame)
        response = entries_view.row_pressed(2)
        self.assertIsNone(response)
        changed = entries_view.search_text_changed()
        self.assertIsNone(changed)
    
    def text_search_text_changed(self):
        pass


if __name__ == '__main__':
    unittest.main()
