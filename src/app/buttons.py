import customtkinter
from collections.abc import Callable


class Buttons:
    
    def __init__(self,root, action: Callable[[], str], state):
        self._root = root
        self._action = action
        self.state = state
        self.add_button = customtkinter.CTkButton(
            root, text='Add', command= self.add_pressed, state= self.state)

        self._delete_button = customtkinter.CTkButton(
            root, text='Delete', command= self.delete_pressed, state= self.state)

        self._edit_button = customtkinter.CTkButton(
            root, text='Edit', command= self.edit_pressed, state= self.state)

        self._clear_button = customtkinter.CTkButton(
            root, text='Clear', command= self.clear_pressed, state= self.state)



    def add_pressed(self):
        self._action("ADD")

    def delete_pressed(self):
        self._action("DELETE")

    def edit_pressed(self):
        self._action("EDIT")

    def clear_pressed(self):
        self._action("CLEAR")