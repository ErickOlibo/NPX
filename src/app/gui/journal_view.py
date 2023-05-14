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
        self._editing = False
        self._post_id = None
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
            self.delete_button.hidden
            # self.edit_button.hidden

        if state == ViewState.JOURNAL_UPDATE:
            self.delete_button.visible
            # self.edit_button.visible

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

        # self.edit_button = CustomButton(
        #     self, JournalButton.EDIT, lambda: self._button_pressed(JournalButton.EDIT))
        # self.edit_button.grid(row=3, column=2, padx=(20, 0), pady=(60, 20), sticky="e")

        self.clear_button = CustomButton(
            self, JournalButton.CLEAR, lambda: self._button_pressed(JournalButton.CLEAR))
        self.clear_button.grid(row=3, column=3, padx=(40, 40), pady=(60, 20), sticky="nsew")

    def _button_pressed(self, type: JournalButton):
        """Respond to a button being pressed in the GUI"""
        print(type)
        if type == JournalButton.SAVE:
            self._save()
        if type == JournalButton.DELETE:
            self._delete()
        if type == JournalButton.CLEAR:
            self._clear()

    def _save(self):
        title = self.title_entry.get().strip()
        tags = self.tags_entry.get().strip()
        text = self.entry_box.get('1.0', 'end').strip()
        if self._editing:
            self._update(title, text, tags)
        else:
            self._insert(title, text, tags)
        self._reload_recent_entries()

    def _update(self, title: str, text: str, tags: str):
        entry = self._recent_entries[self._post_id]
        if [len(title), len(text)] == [0, 0]:
            self._delete_entry_on_empty(self._post_id)
        else:
            (title, text) = self._process_empty_title_text(title, text)
            data = EntriesData(entry.user, title, text, entry.datenow, entry.timenow, tags)
            self._handler.update_entry_with_id(self._post_id, data)
        self._reload_recent_entries()

    def _insert(self, title: str, text: str, tags: str):
        current_date = datetime.now().strftime('%Y/%m/%d')
        current_time = datetime.now().strftime("%H:%M:%S")
        if [len(title), len(text)] != [0, 0]:
            (title, text) = self._process_empty_title_text(title, text)
            data = EntriesData(self._username, title, text, current_date, current_time, tags)
            self._handler.insert_into_entries(data)
        self._reload_recent_entries()

    def _reload_recent_entries(self):
        self._clear()
        self._add_recent_entries_to_scrollview(self._username)
        self._post_id = 0
        self._editing = False
        self.delete_button.hidden
        pass

    def _process_empty_title_text(self, title: str, text: str) -> tuple[str, str]:
        print(f"B4 - Length [{len(title)}, {len(text)}]")
        title = title.strip()
        text = text.strip()
        print(f"AF - Length [{len(title)}, {len(text)}]")
        processed_title = "_Untitled_" if not title else title
        processed_text = "_Empty_" if not text else text
        print(f"Title: {processed_title}\nText: {processed_text}")
        return (processed_title, processed_text)

    def _delete(self):
        # Warning MESSAGE BOX for DELETING ENTRY
        print("DELETE selected ENTRY")

        """Deletes the selected entry of the current user from the journal and clears the input fields."""
        entry_id = self._handler.get_entry_id(self._username, self.selected_entry_id)
        if entry_id:
            self._handler.delete_entry(entry_id)
            self._add_recent_entries_to_scrollview(self._username)
            self._clear()
        self.selected_entry_id = None

    def _delete_entry_on_empty(self, id: int):
        print("Delete from Update empty Title and Text")

    def _clear(self):
        if self.entry_box.get('1.0', 'end-1c') != '':
            self.entry_box.delete('1.0', 'end')
        self.title_entry.delete(0, 'end')
        self.tags_entry.delete(0, 'end')
        self.tags_entry.configure(placeholder_text="Tags")
        self.title_entry.configure(placeholder_text="Title")
        self.focus()

    # def _edit(self):
    #     print("EDIT selected ENTRY")

    # ##### DISPLAY ENTRIES and LOAD SELECTED ENTRY DATA ##### #
    def _add_recent_entries_to_scrollview(self, username):
        self._recent_entries = self._handler.get_recent_entries(username, 10)
        for i, (key, value) in enumerate(self._recent_entries.items()):
            row = RecentPostRow(self.entries_frame, key, value, self.row_clicked_at_id)
            row.configure(fg_color=("gray80", "gray20") if i % 2 == 0 else ("gray75", "gray15"))
            row.grid(row=i, column=0, sticky="ew")

    def row_clicked_at_id(self, id: int):
        self._editing = True
        self._post_id = id
        self.delete_button.visible
        print(f"Selected Entry ID: {id} -- {self._post_id}")
        self.selected_entry_id = id

        data = self._recent_entries[id]
        self._clear()

        self.title_entry.insert(0, data.title)
        self.tags_entry.insert(0, data.tags)
        self.entry_box.insert("1.0", data.text)
