"""This module tests Journal View using unittest."""
import unittest
import customtkinter
from gui.journal_view import JournalView
from helpers import JournalButton, EntriesData

class TestApp(unittest.TestCase):
    """Test classes and methods using UnitTest."""
    
    def setUp(self):
        self.master = customtkinter.CTk()
        self.journal_view = JournalView(self.master, "Erick")
        self.journal_view._add_recent_entries_to_scrollview("Erick")
    
    def tearDown(self):
        self.master.destroy()
    
    def test_journal_view(self):
        self.assertIsInstance(self.journal_view, customtkinter.CTkFrame)
        response = self.journal_view._button_pressed(JournalButton.SAVE)
        self.assertIsNone(response)
        response = self.journal_view._button_pressed(JournalButton.CLEAR)
        self.assertIsNone(response)
        
    def test_row_clicked_at_id(self):
        keys = self.journal_view._recent_entries.keys()
        # print(keys)
        resp = self.journal_view.row_clicked_at_id(list(keys)[0])
        self.assertIsNone(resp, JournalButton)

    def test_update(self):
        entries = self.journal_view._recent_entries
        # print(entries.keys())
        post_id = list(entries.keys())[0]
        entry = entries[post_id]
        self.journal_view._post_id = post_id
        title = "Testing-Title"
        text = "Testing-Text"
        tags = "Testing-Tags"
        self.journal_view._update(title, text, tags)
        self.assertNotEqual(entry.title, title)
        self.journal_view._post_id = post_id
        self.journal_view._update("", "", "")
        entries = self.journal_view._recent_entries
        self.assertNotIn(post_id, list(entries.keys()))
    
    def test_insert_delete(self):
        title = "Current Title"
        text = "Current Text"
        tags = "Current Tags"
        self.journal_view._insert(title, text, tags)
        entries = self.journal_view._recent_entries
        entry_id = list(entries.keys())[0]
        latest_entry = entries[entry_id]
        self.assertIsInstance(latest_entry, EntriesData)
        self.assertEqual(title, latest_entry.title)
        self.journal_view.selected_entry_id = entry_id
        self.journal_view._delete()
        entries = self.journal_view._recent_entries
        


if __name__ == '__main__':
    unittest.main()
