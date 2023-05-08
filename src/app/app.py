"""
This module is the responsible for the Desktop app logic. It controls
the flow of data between the Views and the data models
"""

import customtkinter
from helpers import * 
from gui.login_view import LoginView
from gui.navigation_bar import NavigationBar
from sql_handler import SQLHandler
from issue_handler import IssueHandler
from gui.entries_view import EntriesView
from gui.journal_view import JournalView


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
        self.resizable(False, False)
        self._start_up(with_login=False)

# ##### BYPASS LOGIN VIEW ##### #
    def _start_up(self, with_login: bool):
        if with_login:
            self._show_login_view()
        else:
            self._session_data = SessionData("Test User", "123456", StartUp.LOG_IN)
            self._show_main_view_from_startup()

# ##### LOGIN VIEW ##### #
    def _show_login_view(self):
        self.title("NPX App | Login Screen")
        self.geometry(f"{self.login_view_size[0]}x{self.login_view_size[1]}")
        self.login_view = LoginView(self, self._login_signin_pressed)
        self.login_view.grid(row=0, column=0, padx=120, pady=50, sticky="ns")
    
    def _login_signin_pressed(self, data: SessionData):
        self._session_data = data
        issue = IssueHandler().get_issue_message(data)
        if issue == IssueMessage.NONE:
            self.login_view.grid_forget()
            self._show_main_view_from_startup()
        else:
            self.login_view.set_wrong_credentials_message(issue)
    
# ##### MAIN VIEW ##### #
    def _configure_main_view(self):
        self.title("NPX App | Your Secret Companion")
        self.geometry(f"{self.main_view_size[0]}x{self.main_view_size[1]}")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.navigation_bar = NavigationBar(self, self._navigation_button_pressed)
        self.navigation_bar.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.navigation_bar.grid_rowconfigure(4, weight=1)

    def _show_main_view_from_startup(self):
        self._configure_main_view()
        self.navigation_bar.set_active_button(View.JOURNAL)
        self._active_view = View.JOURNAL
        self._show_journal_view()

# ##### JOURNAL VIEW ##### #
    def _show_journal_view(self):
        self._journal_view = JournalView(self, self._session_data.username)
        self._journal_view.state(ViewState.JOURNAL_INSERT)
        self._journal_view.grid(row=0, column=1, rowspan=4, sticky="nsew")


# ##### ENTRIES VIEW ##### #
    def _show_entries_view(self):
        self._entriesView = EntriesView(self)

    def _navigation_button_pressed(self, view: View):
        if self._active_view == view:
            return None
        else:
            self._active_view = view
        
        self.navigation_bar.set_active_button(view)
        print(view.name)
        if view == View.JOURNAL:
            self._entriesView.grid_forget()
            self._show_journal_view()

        if view == View.ENTRIES:
            self._journal_view.grid_forget()
            self._show_entries_view()

        if view == View.LOGOUT:
            for view in self.grid_slaves():
                view.grid_forget()
            self._show_login_view()
    


if __name__ == "__main__":
    app = App()
    app.mainloop()
