"""
This module is the responsible for the Desktop app logic. It controls
the flow of data between the Views and the data models
"""

from datetime import datetime
import customtkinter
from helpers import View, SessionData, IssueMessage, EntriesData
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
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        # Attach Journal View Elements
        self._attach_title_entry()
        self._attach_entry_box()
        self._attach_tags_entry()
        self._attach_save_botton()
        self._attach_delete_button()
        self._attach_edit_button()
        self._attach_clear_button()

    def _forget_journal_view_(self):
        self.title_entry.grid_forget()
        self.tags_entry.grid_forget()
        self.save_button.grid_forget()
        self.entry_box.grid_forget()
        self.delete_button.grid_forget()
        self.edit_button.grid_forget()
        self.clear_button.grid_forget()

    def _attach_title_entry(self):
        self.title_entry = customtkinter.CTkEntry(self, placeholder_text="Title")
        self.title_entry.grid(row=0, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

    def _attach_entry_box(self):
        self.entry_box = customtkinter.CTkTextbox(self, width=350, wrap="word")
        self.entry_box.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

    def _attach_tags_entry(self):
        self.tags_entry = customtkinter.CTkEntry(self, placeholder_text="Tags")
        self.tags_entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(0, 80), sticky="nsew")

    def _attach_save_botton(self):
        self.save_button = customtkinter.CTkButton(
            self, text="Save",
            command=lambda: self.button_pressed('ADD'),
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "gray90"))
        self.save_button.grid(row=3, column=3, padx=(40, 20), pady=(0, 80), sticky="nsew")

    def _attach_delete_button(self):
        self.delete_button = customtkinter.CTkButton(
            self, text="Delete",
            command=lambda: self.button_pressed('DELETE'),
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "gray90"),
            state='disabled')
        self.delete_button.grid(row=3, column=1, padx=(20, 20), pady=(60, 20), sticky="w")
        self._invisible_button(self.delete_button, "disabled")

    def _attach_edit_button(self):
        self.edit_button = customtkinter.CTkButton(
            self, text="Edit",
            command=lambda: self.button_pressed('EDIT'),
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "gray90"),
            state='disabled')
        self.edit_button.grid(row=3, column=2, padx=(20, 0), pady=(60, 20), sticky="e")
        self._invisible_button(self.edit_button, "disabled")

    def _attach_clear_button(self):
        self.clear_button = customtkinter.CTkButton(
            self, text="Clear",
            command=lambda: self.button_pressed('CLEAR'),
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "gray90"))
        self.clear_button.grid(row=3, column=3, padx=(40, 20), pady=(60, 20), sticky="nsew")

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

    def _invisible_button(self, button: customtkinter.CTkButton, state: str):
        button.configure(border_width=0, text="", state=state)

    def _visible_button(self, button: customtkinter.CTkButton, label: str, state: str):
        button.configure(border_width=2, text=label, state=state)

    def button_pressed(self, text):
        """Respond to a button being pressed in the GUI"""
        print(text)
        if text == 'ADD':
            self.activate()
            self._add()

        if text == 'DELETE':
            self.deactivate()

        if text == 'CLEAR':
            self._clear()

        if text == 'Edit':
            pass

    def _add(self):
        username = self._session_data.username
        title = self.title_entry.get()
        tags = self.tags_entry.get()
        entry = self.entry_box.get('1.0', 'end')
        now = datetime.now().strftime('%Y/%m/%d')
        timenow = datetime.now().strftime("%H:%M:%S")
        if len(entry.rstrip()) > 0:
            data = EntriesData(username, title, entry, now, timenow, tags)
            self._handler.insert_into_entries(data)
        self._clear()

    def _clear(self):
        if self.entry_box.get('1.0', 'end-1c') != '':
            self.entry_box.delete('1.0', 'end')

        self.title_entry.delete(0, 'end')

        self.tags_entry.delete(0, 'end')
        self.tags_entry.configure(placeholder_text="Tags")
        self.focus()

# ############# END JOURNAL ENTRY VIEW ##########################################
    def _show_planning_view(self):
        self.navigation_bar.set_active_button(View.PLANNING)
        self._forget_journal_view_()
        self.current_view.grid_forget()
        self._show_temporary_center_view(View.PLANNING)

    def _show_challenges_view(self):
        self.navigation_bar.set_active_button(View.CHALLENGES)
        self._forget_journal_view_()
        self.current_view.grid_forget()
        self._show_temporary_center_view(View.CHALLENGES)

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

        if view == View.PLANNING:
            self._show_planning_view()

        if view == View.CHALLENGES:
            self._show_challenges_view()

        if view == View.LOGOUT:
            self.navigation_bar.grid_forget()
            self.current_view.grid_forget()
            self._forget_journal_view_()
            self._show_login_view()


if __name__ == "__main__":
    app = App()
    app.mainloop()
