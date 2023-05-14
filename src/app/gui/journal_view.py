import customtkinter
from datetime import datetime
from custom_button import CustomButton
from helpers import JournalButton, ViewState, EntriesData
from sql_handler import SQLHandler
from recent_post import RecentPostRow


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
        self._buttons()

        # Setting Recent Post Scrollview
        self.entries_frame = customtkinter.CTkScrollableFrame(
            self, width=200, height=400, label_text="Recent Posts",
            label_font=("Helvetica", 15, "bold"))
        self.entries_frame.grid(row=0, column=3, rowspan=3, padx=24, pady=20, sticky='n')
        self._add_recent_entries_to_scrollview(self._username)

    # ##### PUBLIC METHODS ##### #
    def state(self, state: ViewState):
        if state == ViewState.JOURNAL_INSERT:
            self.delete_button.visible
            self.edit_button.visible

        if state == ViewState.JOURNAL_UPDATE:
            self.delete_button.visible
            self.edit_button.visible

    # ##### PRIVATE METHODS ##### #
    def _entry_title(self):
        self.title_entry = customtkinter.CTkEntry(self, placeholder_text="Title")
        self.title_entry.grid(row=0, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

    def _entry_text_box(self):
        self.entry_box = customtkinter.CTkTextbox(self, width=350, height=400, wrap="word")
        self.entry_box.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

    def _entry_tags(self):
        self.tags_entry = customtkinter.CTkEntry(self, placeholder_text="Tags")
        self.tags_entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(0, 80), sticky="nsew")

    def _buttons(self):
        self.save_button = CustomButton(
            self, JournalButton.SAVE, lambda: self._button_pressed(JournalButton.SAVE))
        self.save_button.grid(row=3, column=3, padx=(40, 40), pady=(0, 80), sticky="nsew")

        self.delete_button = CustomButton(
            self, JournalButton.DELETE, lambda: self._button_pressed(JournalButton.DELETE))
        self.delete_button.grid(row=3, column=1, padx=(20, 20), pady=(60, 20), sticky="w")

        self.edit_button = CustomButton(
            self, JournalButton.EDIT, lambda: self._button_pressed(JournalButton.EDIT))
        self.edit_button.grid(row=3, column=2, padx=(20, 0), pady=(60, 20), sticky="e")

        self.clear_button = CustomButton(
            self, JournalButton.CLEAR, lambda: self._button_pressed(JournalButton.CLEAR))
        self.clear_button.grid(row=3, column=3, padx=(40, 40), pady=(60, 20), sticky="nsew")

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
        title = self.title_entry.get()
        tags = self.tags_entry.get()
        entry = self.entry_box.get('1.0', 'end')
        now = datetime.now().strftime('%Y/%m/%d')
        timenow = datetime.now().strftime("%H:%M:%S")
        if len(entry.rstrip()) > 0:
            data = EntriesData(self._username, title, entry, now, timenow, tags)
            self._handler.insert_into_entries(data)
        self._clear()

    def _delete(self):
        """Deletes the selected entry of the current user from the journal and clears the input fields."""
        entry_id = self._handler.get_entry_id(self._username, self.selected_entry_id)
        if entry_id:
            self._handler.delete_entry(entry_id)
            self._add_recent_entries_to_scrollview(self._username)
            self._clear()
        self.selected_entry_id = None

    def _clear(self):
        if self.entry_box.get('1.0', 'end-1c') != '':
            self.entry_box.delete('1.0', 'end')
        self.title_entry.delete(0, 'end')
        self.tags_entry.delete(0, 'end')
        self.tags_entry.configure(placeholder_text="Tags")
        self.focus()

    def _edit(self):
        print("EDIT selected ENTRY")

    # ##### DISPLAY ENTRIES and LOAD SELECTED ENTRY DATA ##### #
    def _add_recent_entries_to_scrollview(self, username):
        self._recent_entries = self._handler.get_recent_entries(username, 10)
        for i, (key, value) in enumerate(self._recent_entries.items()):
            row = RecentPostRow(self.entries_frame, key, value, self.row_clicked_at_id)
            row.configure(fg_color=("gray80", "gray20") if i % 2 == 0 else ("gray75", "gray15"))
            row.grid(row=i, column=0, sticky="ew")

    def row_clicked_at_id(self, id: int):
        print(f"Selected Entry ID: {id}")
        self.selected_entry_id = id
        data = self._recent_entries[id]

        # clear content from text fields
        self.title_entry.delete(0, "end")
        self.tags_entry.delete(0, "end")
        if self.entry_box.get('1.0', 'end-1c') != '':
            self.entry_box.delete('1.0', 'end')

        # Insert new content to text fields
        self.title_entry.insert(0, data.title)
        self.tags_entry.insert(0, data.tags)
        self.entry_box.insert("1.0", data.text)
