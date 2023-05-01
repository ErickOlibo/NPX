import unittest
import customtkinter
from collections.abc import Callable
from buttons import Buttons

class TestButtons(unittest.TestCase):

    def setUp(self):
        self.root = customtkinter.CTk()
        self.state = 0

    def test_add_pressed(self):
        action = lambda value: self.assertEqual(value, 'ADD')
        buttons = Buttons(self.root, action, self.state)
        buttons.add_pressed()

    def test_delete_pressed(self):
        action = lambda value: self.assertEqual(value, 'DELETE')
        buttons = Buttons(self.root, action, self.state)
        buttons.delete_pressed()

    def test_edit_pressed(self):
        action = lambda value: self.assertEqual(value, 'EDIT')
        buttons = Buttons(self.root, action, self.state)
        buttons.edit_pressed()

    def test_clear_pressed(self):
        action = lambda value: self.assertEqual(value, 'CLEAR')
        buttons = Buttons(self.root, action, self.state)
        buttons.clear_pressed()


if __name__ == '__main__':
    unittest.main()
