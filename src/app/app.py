"""
This module is the responsible for the Desktop app logic. It controls
the flow of data between the Views and the data models
"""

import customtkinter
import re
from helpers import View, SessionData, SessionIssue, StartUp, SQLTable
from gui.login_view import LoginView
from gui.navigation_bar import NavigationBar
from sql_handler import SQLHandler

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
        self.login_view_size = (500, 500)
        self.main_view_size = (1080, 720)
        self._show_login_view()

    def _show_main_view(self):
        self.title("NPX App | Your Secret Companion")
        self.geometry(f"{self.main_view_size[0]}x{self.main_view_size[1]}")
        self.resizable(True, True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.navigation_bar = NavigationBar(
            self, self._journal_tab_pressed,
            self._planning_tab_pressed,
            self._challenges_tab_pressed,
            self._logout_pressed)
        self.navigation_bar.grid(row=0, column=0, sticky="nsew")
        self.navigation_bar.grid_rowconfigure(4, weight=1)
        self._set_current_view("Journal Center View")

    def _set_current_view(self, title: str):
        self.current_view = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color=("gray90", "gray15"))
        self.current_view.grid_columnconfigure(0, weight=1)
        button = customtkinter.CTkButton(
            self.current_view, text=title, compound="left")
        button.grid(row=0, column=0, padx=20, pady=300)
        self.current_view.grid(row=0, column=1, sticky="nsew")

    def _show_login_view(self):
        self.title("NPX App | Login Screen")
        self.geometry(f"{self.login_view_size[0]}x{self.login_view_size[1]}")
        self.resizable(False, False)

        self.login_view = LoginView(self, self._login_signin_pressed)
        self.login_view.grid(row=0, column=0, padx=120, pady=50, sticky="ns")

    # LOGIN or SIGN IN Pressed
    def _login_signin_pressed(self, data: SessionData):
        issue = self._processed_data_issue(data)
        if issue == SessionIssue.NONE:
            self.login_view.grid_forget()
            self._show_main_view()
        else:
            self.login_view.set_wrong_credentials_message(issue)

    def _processed_data_issue(self, data: SessionData) -> SessionIssue:
        if not data.username:
            return SessionIssue.EMPTY_USERNAME
        if not data.password:
            return SessionIssue.EMPTY_PASSWORD
        if not re.search('[!@#$%^&?*]', data.password):
            return SessionIssue.MISSING_SPECIAL

        handler = SQLHandler()
        if data.type == StartUp.SIGN_IN:
            if not handler.username_taken(data.username):
                handler.insert_into(SQLTable.USERDATA,
                                    username=data.username, password=data.password)
                return SessionIssue.NONE
            return SessionIssue.USERNAME_TAKEN

        if data.type == StartUp.LOG_IN:
            if handler.verified_user(data.username, data.password):
                return SessionIssue.NONE
            if handler.username_taken(data.username):
                return SessionIssue.WRONG_PASSWORD
            return SessionIssue.WRONG_USERNAME
        return SessionIssue.UNKNOWN

    def _logout_pressed(self):
        self.navigation_bar.grid_forget()
        self.current_view.grid_forget()
        self._show_login_view()

    def _journal_tab_pressed(self):
        self.navigation_bar.set_active_button(View.JOURNAL)
        self._set_current_view("Journal Center View")
        print(f"{View.JOURNAL.name}")

    def _planning_tab_pressed(self):
        self.navigation_bar.set_active_button(View.PLANNING)
        self._set_current_view("Planning Center View")
        print(f"{View.PLANNING.name}")

    def _challenges_tab_pressed(self):
        self.navigation_bar.set_active_button(View.CHALLENGES)
        self._set_current_view("Challenges Center View")
        print(f"{View.CHALLENGES.name}")

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()
