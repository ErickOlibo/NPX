"""This module is the main application. The implementation starts here
and all actions should be in sync with this class as it interact with
the user
"""

import customtkinter
import os
from PIL import Image
from collections.abc import Callable
from helpers import View


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

class MainApp(customtkinter.CTk):
    login_view_size = (500, 500)
    main_view_size = (1280, 720)
    
    def __init__(self) -> None:
        super().__init__()

        # Prepare Login View
        self.title("NPX App | Login Screen")
        self.geometry(f"{self.login_view_size[0]}x{self.login_view_size[1]}")
        self.resizable(False, False)

        # Path to assets folder
        self.assets_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "gui/assets")

        # Create Login View
        self.login_view = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_view.grid(row=0, column=0, padx=120, pady=85, sticky="ns")

        # Attach Logo Title and Credential to Login view
        self._attach_logo_to_login_view()
        self._attach_title_credentials()



    # PUBLIC METHODS




    # PRIVATE METHODS
    def _prepare_main_view(self):
        self._set_main_view_default_parameters()
        self._set_navigation_bar()
        self._set_top_logo()
        self._navigation_icons()
        self._navigation_buttons()
        self._get_temporary_main_views()

        self._selected_view(View.JOURNAL)
        self._set_mode_menu()

    def _set_mode_menu(self):
        self.mode_menu = customtkinter.CTkSegmentedButton(
            self.navigation_bar, values=["Light", "System", "Dark"],
            command=self._change_appearance_mode_event)
        self.mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

    def _change_appearance_mode_event(self, new_value):
        customtkinter.set_appearance_mode(new_value)

    def _navigation_buttons(self):
        self.journal_button = self._set_navigation_button(
            "Journal", self.journal_icon, self._journal_button_event, (1, 0), "ew")
        self.planning_button = self._set_navigation_button(
            "Planning", self.planning_icon, self._planning_button_event, (2, 0), "ew")
        self.challenges_button = self._set_navigation_button(
            "Challenges", self.challenges_icon, self._challenges_button_event, (3, 0), "ew")

    def _journal_button_event(self):
        self._selected_view(View.JOURNAL)
        print("Journal")

    def _planning_button_event(self):
        self._selected_view(View.PLANNING)
        print("Planning")

    def _challenges_button_event(self):
        self._selected_view(View.CHALLENGES)
        print("Challenges")

    def _selected_view(self, name: View):
        self._reset_views_buttons()
        if name == View.JOURNAL:
            self._set_active_view_button(self.journal_view, self.journal_button)
        if name == View.PLANNING:
            self._set_active_view_button(self.planning_view, self.planning_button)
        if name == View.CHALLENGES:
            self._set_active_view_button(self.challenges_view, self.challenges_button)



    def _reset_views_buttons(self):
        # Reset selection color to transparent
        self.journal_button.configure(fg_color="transparent")
        self.planning_button.configure(fg_color="transparent")
        self.challenges_button.configure(fg_color="transparent")

        # dispose of all views before new selection
        self.journal_view.grid_forget()
        self.planning_view.grid_forget()
        self.challenges_view.grid_forget()

    def _set_active_view_button(self, view: customtkinter.CTkFrame,
                                button: customtkinter.CTkButton):
        button.configure(fg_color=("gray75", "gray25"))
        view.grid(row=0, column=1, sticky="nsew")

    def _navigation_icons(self):
        icon_size = (26, 26)
        self.journal_icon = self._light_dark_image(
            "icons/light_journal.png", "icons/dark_journal.png", icon_size)
        self.planning_icon = self._light_dark_image(
            "icons/light_planning.png", "icons/dark_planning.png", icon_size)
        self.challenges_icon = self._light_dark_image(
            "icons/light_trophy.png", "icons/dark_trophy.png", icon_size)
        self.login_icon = self._light_dark_image(
            "icons/light_login.png", "icons/dark_login.png", icon_size)
        self.logout_icon = self._light_dark_image(
            "icons/light_logout.png", "icons/dark_logout.png", icon_size)

    def _light_dark_image(self, light: str, dark: str, size: tuple)-> customtkinter.CTkImage:
        """create a customtkinter image by setting the dark mode image,
        light mode image and the size

        Parameters
        ----------
            light (str): the relative path to the light icon
            dark (str): the relative path to the dark icon
            size (tuple): the size of the displayed icon (Width, Height)

        Returns
        -------
            customtkinter.CTkImage: an object CTKImage with the light and dark images
            accessible via the object's properties light_image, dark_image
        """
        return customtkinter.CTkImage(
            light_image=self._getImage(dark),
            dark_image=self._getImage(light),
            size=size)
    
    def _set_navigation_button(self, title: str,
                               icon: customtkinter.CTkImage,
                               action: Callable[[], None],
                               position: tuple[int, int],
                               stick_to: str)-> customtkinter.CTkButton:
        """Creates a button with charateristics from the parameters

        Parameters
        ----------
            title (str): the text in the button
            icon (customtkinter.CTkImage): the icon image to use
            action (Callable[[], None]): the method to call on click
            position (tuple[int, int]): the grid location inside the parent frame
            stick_to (str): the border side, nsew [north, south, east, west] where
            to have the button being stuck to

        Returns:
            customtkinter.CTkButton: a button satisfying the parameters
        """
        nav_button = customtkinter.CTkButton(
            self.navigation_bar, corner_radius=0, height=40, border_spacing=20,
            text=f"{title}", fg_color="transparent", text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"), image=icon, anchor="w",
            font=customtkinter.CTkFont(size=15), command=action)
        nav_button.grid(row=position[0], column=position[1], sticky=stick_to)
        return nav_button
    
    def _set_top_logo(self):
        logo_image = customtkinter.CTkImage(
            self._getImage("npx_logo.png"), size=(35, 35))
        self.top_logo = customtkinter.CTkLabel(
            self.navigation_bar, text="     NPX App", image=logo_image,
            compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.top_logo.grid(row=0, column=0, padx=20, pady=20)
    
    def _set_navigation_bar(self):
        self.navigation_bar = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_bar.grid(row=0, column=0, sticky="nsew")
        self.navigation_bar.grid_rowconfigure(4, weight=1)
    
    def _set_main_view_default_parameters(self):
        self.title("NPX App | Your Secret Companion")
        self.geometry(f"{self.main_view_size[0]}x{self.main_view_size[1]}")
        self.resizable(True, True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
    
    def _login_event(self):
        print(f"Credential: {self.username.get()} | {self.password.get()}")
        self.login_view.grid_forget()
        self._prepare_main_view()

    def _attach_title_credentials(self):
        self.login_label = customtkinter.CTkLabel(
            self.login_view, text="Sign in / Login",
            font=customtkinter.CTkFont(size=20, weight="bold"))

        self.login_label.grid(row=2, column=0, padx=30, pady=(50, 15))
        self.username = customtkinter.CTkEntry(
            self.login_view, width=200, placeholder_text="username")
        self.username.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.password = customtkinter.CTkEntry(
            self.login_view, width=200, show="*", placeholder_text="password")
        self.password.grid(row=4, column=0, padx=30, pady=(0, 15))
        self.login_button = customtkinter.CTkButton(
            self.login_view, text="Login", command=self._login_event, width=200)
        self.login_button.grid(row=5, column=0, padx=30, pady=(15, 15))
    
    def _attach_logo_to_login_view(self):
        self.logo_image = customtkinter.CTkImage(
            self._getImage("npx_logo.png"), size=(45, 45))
        self.logo_label = customtkinter.CTkLabel(
            self.login_view, text="     NPX App", image=self.logo_image,
            compound="left", font=customtkinter.CTkFont(size=25, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=30, pady=(10, 15))
    
    def _getImage(self, path: str)-> Image:
        return Image.open(os.path.join(self.assets_path, path))

    # TEMPORARY view for each Navigation Tab (Journal, Planning, Challenges)
    def _get_temporary_main_views(self):
        self.journal_view = self._set_temp_view("Journal Main View")
        self.planning_view = self._set_temp_view("Planning Main View")
        self.challenges_view = self._set_temp_view("Challenges Main View")
    
    def _set_temp_view(self, title: str) -> customtkinter.CTkFrame:
        temp_view = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        temp_view.grid_columnconfigure(0, weight=1)
        temp_view_center_button = customtkinter.CTkButton(
            temp_view, text=title, compound="left")
        temp_view_center_button.grid(row=0, column=0, padx=20, pady=300)
        return temp_view
    





if __name__ == "__main__":
    app = MainApp()
    app.mainloop()