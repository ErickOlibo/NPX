from datetime import datetime
import customtkinter
from custom_button import CustomButton
from helpers import JournalButton, ViewState, EntriesData
from sql_handler import SQLHandler

class JournalView(customtkinter.CTkFrame):

    def __init__(self, master: customtkinter.CTk, username: str):
        super().__init__(master)
        self._username = username
        self._master = master
        self._handler = SQLHandler()
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure(0, weight=1)
        self.configure(fg_color="transparent")
        
        # Set the view UI elements
        self._entry_title()
        self._entry_text_box()
        self._entry_tags()
        self._recent_entries()
        self._buttons()

    # ##### PUBLIC METHODS ##### #
    def forget_view(self):
        pass

    def state(self, state: ViewState):
        if state == ViewState.JOURNAL_INSERT:
            self.delete_button.hidden
            self.edit_button.hidden

        if state == ViewState.JOURNAL_UPDATE:
            self.delete_button.visible
            self.edit_button.visible

    # ##### PRIVATE METHODS ##### #
    # TO IMPLEMENT
    def _entry_title(self):
        pass

    def _entry_text_box(self):
        self.entry_box = customtkinter.CTkTextbox(self, width=350, wrap="word")
        self.entry_box.grid(row=0, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

    def _entry_tags(self):
        self.tags_entry = customtkinter.CTkEntry(self, placeholder_text="Tags")
        self.tags_entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(0, 80), sticky="nsew")

    # TO IMPLEMENT
    def _recent_entries(self):
        pass

    def _buttons(self):
        self.save_button = CustomButton(
            self, JournalButton.SAVE, lambda: self._button_pressed(JournalButton.SAVE))
        self.save_button.grid(row=3, column=3, padx=(40, 20), pady=(0, 80), sticky="nsew")

        self.delete_button = CustomButton(
            self, JournalButton.DELETE, lambda: self._button_pressed(JournalButton.DELETE))
        self.delete_button.grid(row=3, column=1, padx=(20, 20), pady=(60, 20), sticky="w")

        self.edit_button = CustomButton(
            self, JournalButton.EDIT, lambda: self._button_pressed(JournalButton.EDIT))
        self.edit_button.grid(row=3, column=2, padx=(20, 0), pady=(60, 20), sticky="e")

        self.clear_button = CustomButton(
            self, JournalButton.CLEAR, lambda: self._button_pressed(JournalButton.CLEAR))
        self.clear_button.grid(row=3, column=3, padx=(40, 20), pady=(60, 20), sticky="nsew")



    def _button_pressed(self, type: JournalButton):
        """Respond to a button being pressed in the GUI"""
        print(type)
        if type == JournalButton.SAVE:
            self._insert_update()
        if type == JournalButton.DELETE:
            self._delete()
        if type == JournalButton.CLEAR:
            self._clear()
        if type == JournalButton.EDIT:
            self._edit()
    
    def _insert_update(self):
        tags = self.tags_entry.get()
        entry = self.entry_box.get('1.0', 'end')
        now = datetime.now().strftime('%Y/%m/%d')
        timenow = datetime.now().strftime("%H:%M:%S")
        if len(entry.rstrip()) > 0:
            data = EntriesData(self._username, entry, now, timenow, tags)
            self._handler.insert_into_entries(data)
        self._clear()

    def _delete(self):
        print("DELETE selected ENTRY")
    
    def _clear(self):
        if self.entry_box.get('1.0', 'end-1c') != '':
            self.entry_box.delete('1.0', 'end')
        self.tags_entry.delete(0, 'end')
        self.tags_entry.configure(placeholder_text="Tags")
        self.focus()

    
    def _edit(self):
        print("EDIT selected ENTRY")