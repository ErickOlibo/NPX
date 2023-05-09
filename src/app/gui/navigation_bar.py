"""This module creates a NPX Navigation Bar."""
from collections.abc import Callable
import customtkinter
from helpers import View, Assets, CustomImage, CustomTabButton


class NavigationBar(customtkinter.CTkFrame):
    """A view of type CTkFrame to embeded in custom GUI design."""
    def __init__(self, master, action: Callable[[], View]):
        """Instantiate with the necessary attributes

        Parameters
        ----------
            master: Any
                The object that will be owning this object.
            action: Callable
                a method to trigger in the master when the button is pressed
        """
        super().__init__(master)
        self._action = action
        self._attach_logo()
        self._navigation_icons()
        self._navigation_buttons()
        self._set_mode_menu()
        self._set_logout_button()

    def _attach_logo(self):
        logo_image = CustomImage((35, 35), Assets.NPX_LOGO).image
        self.top_logo = customtkinter.CTkLabel(
            self, text="     NPX App", image=logo_image,
            compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.top_logo.grid(row=0, column=0, padx=20, pady=20)

    def _navigation_icons(self):
        size = (26, 26)
        self.journal_icon = CustomImage(
            size, Assets.LIGHT_JOURNAL, Assets.DARK_JOURNAL).image
        self.entries_icon = CustomImage(
            size, Assets.LIGHT_ENTRIES, Assets.DARK_ENTRIES).image

    def _navigation_buttons(self):
        self.journal_button = CustomTabButton(
            self, "Journal", self.journal_icon,
            self._journal_pressed, (1, 0), "ew").button
        self.entries_button = CustomTabButton(
            self, "Entries", self.entries_icon,
            self._entries_pressed, (2, 0), "ew").button

    def _set_mode_menu(self):
        self.mode_menu = customtkinter.CTkSegmentedButton(
            self, values=["Light", "System", "Dark"],
            command=self._change_appearance_mode_event)
        self.mode_menu.grid(row=6, column=0, padx=20, pady=(0, 12), sticky="s")

    def _change_appearance_mode_event(self, new_value):
        customtkinter.set_appearance_mode(new_value)

    def _set_logout_button(self):
        self.logout = customtkinter.CTkButton(
            self, fg_color="transparent", border_width=2,
            text="Logout", text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"), command=self._logout_pressed)
        self.logout.grid(row=7, column=0, padx=20, pady=20, sticky="s")

    def set_active_button(self, tab: View):
        """Set the navigation tab button to active for View enum type."""
        self._reset_navigation_buttons_color()
        color = ("gray75", "gray25")
        if tab == View.JOURNAL:
            self.journal_button.configure(fg_color=color)
        if tab == View.ENTRIES:
            self.entries_button.configure(fg_color=color)

    def _reset_navigation_buttons_color(self):
        color = "transparent"
        self.journal_button.configure(fg_color=color)
        self.entries_button.configure(fg_color=color)

    def _journal_pressed(self):
        self._action(View.JOURNAL)

    def _entries_pressed(self):
        self._action(View.ENTRIES)

    def _logout_pressed(self):
        self._action(View.LOGOUT)
