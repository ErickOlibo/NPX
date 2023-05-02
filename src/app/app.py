"""
This module is the responsible for the Desktop app logic. It controls
the flow of data between the Views and the data models
"""

import customtkinter
from helpers import View, SessionData, IssueMessage

from gui.login_view import LoginView
from gui.navigation_bar import NavigationBar
from sql_handler import SQLHandler
from issue_handler import IssueHandler


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
        self._start_up(with_login=True)

    def _start_up(self, with_login: bool):
        self._show_login_view() if with_login else self._show_main_view()

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
        if view == View.PLANNING:
            self._show_planning_view()
        if view == View.CHALLENGES:
            self._show_challenges_view()

# ############## CREATE THE JOURNAL VIEW HERE ###################################
    def _show_journal_view(self):
        self.navigation_bar.set_active_button(View.JOURNAL)

        # Configure Main app to accomodate Journal View
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure(0, weight=1)

        # Attach Journal View Elements
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
        self.entry_box = customtkinter.CTkTextbox(self, width=250)
        self.entry_box.grid(row=0, column=1, columnspan= 2, padx=(20, 0), pady=(20, 20), sticky="nsew")

    def _attach_tags_entry(self):
        self.tags_entry = customtkinter.CTkEntry(self, placeholder_text="Tags")
        self.tags_entry.grid(row=2, column=1, columnspan=2, padx=(20, 0), pady=(3, 20), sticky="nsew")

    def _attach_save_botton(self):
        self.save_button = customtkinter.CTkButton(
            self, text="Save",
            command=lambda: self.button_pressed('ADD'),
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "gray90"))
        self.save_button.grid(row=2, column=3, padx=(20, 20), pady=(3, 20), sticky="nsew")

    def _attach_delete_button(self):
        self.delete_button = customtkinter.CTkButton(
            self, text="Delete",
            command=lambda: self.button_pressed('DELETE'),
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "gray90"),
            state='disabled')
        self.delete_button.grid(row=3, column=1, padx=(20, 20), pady=(60, 20), sticky="nsew")

    def _attach_clear_button(self):
        self.clear_button = customtkinter.CTkButton(
            self, text="Clear",
            command=lambda: self.button_pressed('CLEAR'),
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "gray90"))
        self.clear_button.grid(row=3, column=3, padx=(20, 20), pady=(60, 20), sticky="nsew")

    def _attach_edit_button(self):
        self.edit_button = customtkinter.CTkButton(
            self, text="Edit",
            command=lambda: self.button_pressed('EDIT'),
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "gray90"),
            state='disabled')
        self.edit_button.grid(row=3, column=2, padx=(20, 20), pady=(60, 20), sticky="nsew")

    def activate(self):
        """Activate the delete button and edit button."""

        state = 'enabled'
        self.delete_button.configure(state=state)
        self.edit_button.configure(state=state)

    def deactivate(self):
        """Deactivate the delete button and edit button."""

        state = 'disabled'
        self.delete_button.configure(state=state)
        self.edit_button.configure(state=state)

    def button_pressed(self, text):
        print(text)
        if text == 'ADD':
            self.activate()

        if text == 'DELETE':
            self.deactivate()

        if text == 'CLEAR':
            if self.entry_box.get('1.0', 'end-1c') != '':
                self.entry_box.delete('1.0', 'end')

        if text == 'Edit':
            pass


# ############# END JOURNAL ENTRY VIEW ##########################################

    def _show_planning_view(self):
        self.navigation_bar.set_active_button(View.PLANNING)
        self._forget_journal_view_()
        self._show_temporary_center_view(View.PLANNING)

    def _show_challenges_view(self):
        self.navigation_bar.set_active_button(View.CHALLENGES)
        self._forget_journal_view_()
        self._show_temporary_center_view(View.CHALLENGES)

    def _configure_main_view(self):
        self.title("NPX App | Your Secret Companion")
        self.geometry(f"{self.main_view_size[0]}x{self.main_view_size[1]}")
        self.resizable(True, True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=0)

    def _attach_navigation_bar(self):
        self.navigation_bar = NavigationBar(self, self._navigation_button_pressed)
        self.navigation_bar.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.navigation_bar.grid_rowconfigure(4, weight=1)

    def _login_signin_pressed(self, data: SessionData):
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
        self.current_view = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color=("gray90", "gray15"))
        self.current_view.grid_columnconfigure(0, weight=1)
        button = customtkinter.CTkButton(
            self.current_view, text=f"{view.name} Center View", compound="left")
        button.grid(row=0, column=0, padx=20, pady=300)
        self.current_view.grid(row=0, column=1, sticky="nsew")

    # Navigation Bar buttons
    def _navigation_button_pressed(self, view: View):
        print(view.name)
        if view == View.JOURNAL:
            self._show_journal_view()

        if view == View.PLANNING:
            self._show_planning_view()

        if view == View.LOGOUT:
            self.navigation_bar.grid_forget()
            self.current_view.grid_forget()
            self._forget_journal_view_()
            self._show_login_view()


if __name__ == "__main__":
    app = App()
    app.mainloop()
