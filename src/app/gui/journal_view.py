import customtkinter
from datetime import datetime
from custom_button import CustomButton
from helpers import JournalButton, ViewState, EntriesData
from sql_handler import SQLHandler
#from quick_access import JournalEachEntry
#from app.gui.quick import JournalEachEntry

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

        # setting journal entries
        self.entries_frame = customtkinter.CTkScrollableFrame(master=self, width=180, height=300)
        self.entries_frame.grid(row=1, column=3, rowspan=3, padx=24, pady=20, sticky='n')
        self._add_data_to_quick_access(self._username)

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
        #print(f"[{username}] - add_data_to_quick_access: {data_for_entries}")
        for entry in data_for_entries:
            self.entry_widget = JournalEachEntry(
                self.entries_frame,
                id=entry['id'],
                title=entry['title'],
                date=entry['date'],
                first_sentence=entry['first_sentence'],
                tag=entry['tag']
            )
            self.entry_widget.grid(padx=3, pady=3)

    '''_journal_entry_get_content was used for on_click function in "quick_access" '''
    # def _journal_entry_get_content(self, journal_id):
    #     title, text, tags = self._handler.get_data_on_click(journal_id)
    #     self.title_entry.insert(0, title)
    #     self.entry_box.insert(0, text)
    #     self.tags_entry.insert(0, tags)


# ##### ISSUE WITH IMPORTING from quick_access.py ##### #
class JournalEachEntry(customtkinter.CTkButton):
    def __init__(self, master=None, id="", title="", date="", first_sentence="", tag="", **kwargs):
        super().__init__(master, fg_color="transparent", hover_color="gray70", **kwargs)
        self._handler = SQLHandler()
        self.create_left_frame(date)
        self.create_right_frame(title, first_sentence, tag)
        self.bind("<Button-1>", lambda event: self.on_click(id))

    def create_left_frame(self, date):
        # convert date string to datetime object
        date_obj = datetime.strptime(date, "%Y/%m/%d")

        # create left part of entry
        self.left_frame = customtkinter.CTkFrame(self, fg_color="lightgray")
        self.left_frame.grid(row=0, column=0, rowspan=3, padx=3, pady=3, sticky='w')

        self.day_label = customtkinter.CTkLabel(self.left_frame, height=30, text=date_obj.strftime("%a"),
                                                font=("Helvetica", 12, "bold"))
        self.day_label.grid(row=0, column=0, sticky='nsew', padx=5)

        self.date_label = customtkinter.CTkLabel(self.left_frame, height=30, text=date_obj.strftime("%d"),
                                                 font=("Helvetica", 30, "bold"))
        self.date_label.grid(row=1, column=0, sticky='nsew', padx=5)

        self.month_label = customtkinter.CTkLabel(self.left_frame, height=30, text=date_obj.strftime("%B %Y"),
                                                  font=("Helvetica", 10, "bold"))
        self.month_label.grid(row=2, column=0, sticky='nsew', padx=5)

    def create_right_frame(self, title, first_sentence, tag):
        # get limited text
        text_obj = first_sentence[:69] if len(first_sentence) > 300 else first_sentence

        # create right part of entry
        self.right_frame = customtkinter.CTkFrame(self, fg_color="lightgray")
        self.right_frame.grid(row=0, column=1, rowspan=3, columnspan=3, padx=3, pady=3, sticky='nsew')

        self.title_label = customtkinter.CTkLabel(self.right_frame, text=title, font=("Helvetica", 12, "bold"))
        self.title_label.grid(row=0, column=1, sticky='nsew')

        self.first_sentence_label = customtkinter.CTkLabel(self.right_frame,
                                                           width=110,
                                                           text=text_obj,
                                                           font=("Helvetica", 10),
                                                           wraplength=100,
                                                           )
        self.first_sentence_label.grid(row=1, column=1, sticky='nsew')

        self.tag_label = customtkinter.CTkLabel(self.right_frame, text=f"# {tag}",
                                                font=("Helvetica", 11, "italic", "bold"))
        self.tag_label.grid(row=2, column=1, sticky='s')

    # on_click function is currently disabled with no function but just clickable
    def on_click(self, id):
        return  id
