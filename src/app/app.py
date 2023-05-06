"""
This module is the responsible for the Desktop app logic. It controls
the flow of data between the Views and the data models
"""

from datetime import datetime
import customtkinter
from helpers import * 
from gui.login_view import LoginView
from gui.navigation_bar import NavigationBar
from sql_handler import SQLHandler
from issue_handler import IssueHandler
from custom_button import CustomButton


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):
    """
    Create an instance of the NPX application. At start-up the login view is
    presented following by the save journal or the creation of a new journal.
    """

    def __init__(self) -> None:
        """Instantiate the App object and display the login view"""
        super().__init__()
        self._handler = SQLHandler()
        self.login_view_size = (500, 500)
        self.main_view_size = (800, 600)
        self.current_view = customtkinter.CTkFrame(self)
        self._start_up(with_login=False)

    def _start_up(self, with_login: bool):
        if with_login:
            self._show_login_view()
        else:
            self._session_data = SessionData("Test User", "123456", StartUp.LOG_IN)
            self._configure_main_view()
            self._attach_navigation_bar()
            self._show_journal_view()


    def _show_login_view(self):
        self.title("NPX App | Login Screen")
        self.geometry(f"{self.login_view_size[0]}x{self.login_view_size[1]}")
        self.resizable(False, False)
        self.login_view = LoginView(self, self._login_signin_pressed)
        self.login_view.grid(row=0, column=0, padx=120, pady=50, sticky="ns")

    def _show_main_view(self):
        self._configure_main_view()
        self._attach_navigation_bar()
        self._attach_center_view(View.JOURNAL)

    def _attach_center_view(self, view: View):
        if view == View.JOURNAL:
            self._show_journal_view()
        if view == View.ENTRIES:
            self._show_entries_view()


# ############## CREATE THE JOURNAL VIEW HERE ###################################
    def _show_journal_view(self):
        self.navigation_bar.set_active_button(View.JOURNAL)
        self._configure_main_view_for_journal_view()
        self._attach_journal_view_elements()

    def _configure_main_view_for_journal_view(self):
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure(0, weight=1)

    def _attach_journal_view_elements(self):
        self._attach_entry_box()
        self._attach_tags_entry()
        self._attach_save_botton()
        self._attach_delete_button()
        self._attach_edit_button()
        self._attach_clear_button()

    def _forget_journal_view_(self):
        self.tags_entry.grid_forget()
        self.save_button.grid_forget()
        self.entry_box.grid_forget()
        self.delete_button.grid_forget()
        self.edit_button.grid_forget()
        self.clear_button.grid_forget()

    def _attach_entry_box(self):
        self.entry_box = customtkinter.CTkTextbox(self, width=350, wrap="word")
        self.entry_box.grid(row=0, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

    def _attach_tags_entry(self):
        self.tags_entry = customtkinter.CTkEntry(self, placeholder_text="Tags")
        self.tags_entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(0, 80), sticky="nsew")

    # REFACTORING BUTTONS
    def _attach_save_botton(self):
        label = JournalButton.SAVE
        self.save_button = CustomButton(self, label, lambda: self.button_pressed(label))
        self.save_button.grid(row=3, column=3, padx=(40, 20), pady=(0, 80), sticky="nsew")

    def _attach_delete_button(self):
        label = JournalButton.DELETE
        self.delete_button = CustomButton(self, label, lambda: self.button_pressed(label))
        self.delete_button.grid(row=3, column=1, padx=(20, 20), pady=(60, 20), sticky="w")
        self.delete_button.hidden()

    def _attach_edit_button(self):
        label = JournalButton.EDIT
        self.edit_button = CustomButton(self, label, lambda: self.button_pressed(label))
        self.edit_button.grid(row=3, column=2, padx=(20, 0), pady=(60, 20), sticky="e")
        self.edit_button.hidden()

    def _attach_clear_button(self):
        label = JournalButton.CLEAR
        self.clear_button = CustomButton(self, label, lambda: self.button_pressed(label))
        self.clear_button.grid(row=3, column=3, padx=(40, 20), pady=(60, 20), sticky="nsew")

    def button_pressed(self, type: JournalButton):
        """Respond to a button being pressed in the GUI"""
        print(type)
        if type == JournalButton.SAVE:
            self._add()

        if type == JournalButton.DELETE:
            pass

        if type == JournalButton.CLEAR:
            self._clear()

        if type == JournalButton.EDIT:
            pass

    def _add(self):
        username = self._session_data.username
        tags = self.tags_entry.get()
        entry = self.entry_box.get('1.0', 'end')
        now = datetime.now().strftime('%Y/%m/%d')
        timenow = datetime.now().strftime("%H:%M:%S")
        if len(entry.rstrip()) > 0:
            data = EntriesData(username, entry, now, timenow, tags)
            self._handler.insert_into_entries(data)
        self._clear()

    def _clear(self):
        if self.entry_box.get('1.0', 'end-1c') != '':
            self.entry_box.delete('1.0', 'end')

        self.tags_entry.delete(0, 'end')
        self.tags_entry.configure(placeholder_text="Tags")
        self.focus()

# ############# END JOURNAL ENTRY VIEW ##########################################
    def _show_entries_view(self):
        self.navigation_bar.set_active_button(View.ENTRIES)
        self._forget_journal_view_()
        self.current_view.grid_forget()
        self._show_temporary_center_view(View.ENTRIES)

    # def _show_challenges_view(self):
    #     self.navigation_bar.set_active_button(View.CHALLENGES)
    #     self._forget_journal_view_()
    #     self.current_view.grid_forget()
    #     self._show_temporary_center_view(View.CHALLENGES)

    def _configure_main_view(self):
        self.title("NPX App | Your Secret Companion")
        self.geometry(f"{self.main_view_size[0]}x{self.main_view_size[1]}")
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=0)

    def _attach_navigation_bar(self):
        self.navigation_bar = NavigationBar(self, self._navigation_button_pressed)
        self.navigation_bar.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.navigation_bar.grid_rowconfigure(4, weight=1)

    def _login_signin_pressed(self, data: SessionData):
        self._session_data = data
        issue = IssueHandler().get_issue_message(data)
        if issue == IssueMessage.NONE:
            self.login_view.grid_forget()
            self._show_main_view()
        else:
            self.login_view.set_wrong_credentials_message(issue)

    def _set_current_view(self, title: str):
        self.current_view = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color=("gray90", "gray15"))
        self.current_view.grid_columnconfigure(0, weight=1)
        button = customtkinter.CTkButton(
            self.current_view, text=title, compound="left")
        button.grid(row=0, column=0, padx=20, pady=300)
        self.current_view.grid(row=0, column=1, sticky="nsew")

    def _show_temporary_center_view(self, view: View):
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self._set_current_view(view.name)

    # Navigation Bar buttons
    def _navigation_button_pressed(self, view: View):
        print(view.name)
        if view == View.JOURNAL:
            self._show_journal_view()

        if view == View.ENTRIES:
            self._show_entries_view()

        if view == View.LOGOUT:
            self.navigation_bar.grid_forget()
            self.current_view.grid_forget()
            self._forget_journal_view_()
            self._show_login_view()


if __name__ == "__main__":
    app = App()
    app.mainloop()
