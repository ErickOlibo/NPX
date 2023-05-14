import customtkinter
import textwrap
from collections.abc import Callable
from datetime import datetime
from custom_button import CustomButton
from helpers import JournalButton, ViewState, EntriesData
from sql_handler import SQLHandler
# from quick_access import JournalEachEntry

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
        
        # Setting journal entries
        # self.entries_frame = customtkinter.CTkScrollableFrame(master=self, width=160, height=390)
        # self.entries_frame.grid(row=1, column=3, rowspan=3, padx=24, pady=20, sticky='n')
        # self.recent_posts = customtkinter.CTkLabel(self.entries_frame,
        #                                            text="Recent posts",
        #                                            font=("Helvetica", 17, "bold"),)
        # self.recent_posts.grid(row=0, sticky="w", pady=2, padx=5)
        # self._add_data_to_quick_access(self._username)

    # ##### PUBLIC METHODS ##### #
    def state(self, state: ViewState):
        if state == ViewState.JOURNAL_INSERT:
            self.delete_button.hidden
            self.edit_button.hidden

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
        print("DELETE selected ENTRY")

    def _clear(self):
        if self.entry_box.get('1.0', 'end-1c') != '':
            self.entry_box.delete('1.0', 'end')
        self.title_entry.delete(0, 'end')
        self.tags_entry.delete(0, 'end')
        self.tags_entry.configure(placeholder_text="Tags")
        self.focus()

    def _edit(self):
        print("EDIT selected ENTRY")

    def _add_data_to_quick_access(self, username):
        data_for_entries = self._handler.get_data_desc(username)
        # print(f"[{username}] - add_data_to_quick_access: {data_for_entries}")
        # for i, entry in enumerate(data_for_entries):
        #     self.entry_widget = JournalEachEntry(
        #         self.entries_frame,
        #         id=entry['id'],
        #         title=entry['title'],
        #         date=entry['date'],
        #         first_sentence=entry['first_sentence'],
        #         time=entry['time'],
        #         tag=entry['tag']
        #     )
        #     self.entry_widget.grid(row=i+1, padx=3, pady=3)

    # ##### DISPLAY ENTRIES and LOAD SELECTED ENTRY DATA ##### #
    def _add_recent_entries_to_scrollview(self, username):
        self._recent_entries = self._handler.get_recent_entries(username, 10)
        for i, (key, value) in enumerate(self._recent_entries.items()):
            row = RecentPostRow(self.entries_frame, key, value, self.row_clicked_at_id)
            row.configure(fg_color=("gray80", "gray20") if i % 2 == 0 else ("gray75", "gray15"))
            row.grid(row=i, column=0, sticky="ew")

    def row_clicked_at_id(self, id: int):
        print(f"Selected Entry ID: {id}")
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


    '''_journal_entry_get_content was used for on_click function in "quick_access" CIRCULAR IMPORTING '''
    # def _journal_entry_get_content(self, journal_id):
    #     title, text, tags = self._handler.get_data_on_click(journal_id)
    #     self.title_entry.insert(0, title)
    #     self.entry_box.insert(0, text)
    #     self.tags_entry.insert(0, tags)



# #############  RECENT POST ROW  ############## #
class RecentPostRow(customtkinter.CTkFrame):
    def __init__(self, master, id: int, entry: EntriesData, action: Callable[[], int]):
        super().__init__(master, fg_color="transparent", corner_radius=0)
        self._master = master
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self._id = id
        self._handler = SQLHandler()
        self._action = action
        self._entry = entry
        self.create_date_frame()
        self.create_title_frame()

    def create_date_frame(self):
        date_obj = datetime.strptime(self._entry.datenow, "%Y/%m/%d")
        date_text = date_obj.strftime("%e\n%b")
        self.date_frame = customtkinter.CTkButton(
            self, fg_color="transparent", text_color=("gray10", "gray90"), anchor="w",
            text=date_text, width=35, height=40, font=("Helvetica", 15, "bold"), 
            command=self._row_pressed, corner_radius=0, hover_color=("gray70", "gray30"))
        self.date_frame.grid(row=0, column=0, rowspan=3, padx=2, pady=2, sticky='ew')
    
    def create_title_frame(self):
        title_text = self._wrap_title()
        self.title_frame = customtkinter.CTkButton(
            self, fg_color="transparent", text_color=("gray10", "gray90"), anchor="w",
            text=title_text, width=150, height=40, font=("Helvetica", 12), compound="right",
            command=self._row_pressed, corner_radius=0, hover_color=("gray70", "gray30"))
        self.title_frame.grid(row=0, column=1, rowspan=3, columnspan=3, padx=2, pady=2, sticky='w')
    
    def _wrap_title(self) -> str:
        lines = textwrap.wrap(self._entry.title, width=28)
        if len(lines) > 2:
            lines = lines[:2]
            last_line = lines[-1] + "..."
            lines = lines[:-1] + [last_line]
        return "\n".join(lines)
    
    def _row_pressed(self):
        self._action(self._id)
