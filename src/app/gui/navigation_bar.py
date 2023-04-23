import customtkinter
import os
from collections.abc import Callable
from PIL import Image
from helpers import View

class NavigationBar(customtkinter.CTkFrame):
    assets_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "assets")
    
    def __init__(self, master,
                 journal: Callable[[], None],
                 planning: Callable[[], None],
                 challenges: Callable[[], None],
                 logout: Callable[[], None]):
        super().__init__(master)
        self._attach_logo()
        self._navigation_icons()
        self._navigation_buttons(journal, planning, challenges)
        self._set_mode_menu()
        self._set_logout_button(logout)


    def _reset_navigation_buttons_color(self):
        self.journal_button.configure(fg_color="transparent")
        self.planning_button.configure(fg_color="transparent")
        self.challenges_button.configure(fg_color="transparent")
        pass
    
    def set_active_button(self, tab: View):
        self._reset_navigation_buttons_color()
        if tab == View.JOURNAL:
            self.journal_button.configure(fg_color=("gray75", "gray25"))
        if tab == View.PLANNING:
            self.planning_button.configure(fg_color=("gray75", "gray25"))
        if tab == View.CHALLENGES:
            self.challenges_button.configure(fg_color=("gray75", "gray25"))

    
    
    def _attach_logo(self):
        logo_image = customtkinter.CTkImage(
            self._getImage("npx_logo.png"), size=(35, 35))
        self.top_logo = customtkinter.CTkLabel(
            self, text="     NPX App", image=logo_image,
            compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.top_logo.grid(row=0, column=0, padx=20, pady=20)
    
    
    def _getImage(self, path: str)-> Image:
        return Image.open(os.path.join(self.assets_path, path))
    
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
    
    def _navigation_buttons(self, journal_action, planning_action, challenges_action ):
        self.journal_button = self._set_navigation_button(
            "Journal", self.journal_icon, journal_action, (1, 0), "ew")
        self.planning_button = self._set_navigation_button(
            "Planning", self.planning_icon, planning_action, (2, 0), "ew")
        self.challenges_button = self._set_navigation_button(
            "Challenges", self.challenges_icon, challenges_action, (3, 0), "ew")

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
            self, corner_radius=0, height=40, border_spacing=20,
            text=f"{title}", fg_color="transparent", text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"), image=icon, anchor="w",
            font=customtkinter.CTkFont(size=15), command=action)
        nav_button.grid(row=position[0], column=position[1], sticky=stick_to)
        return nav_button
    
    def _set_mode_menu(self):
        self.mode_menu = customtkinter.CTkSegmentedButton(
            self, values=["Light", "System", "Dark"],
            command=self._change_appearance_mode_event)
        self.mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")
    
    def _change_appearance_mode_event(self, new_value):
        customtkinter.set_appearance_mode(new_value)

    def _set_logout_button(self, action):
        self.logout = customtkinter.CTkButton(
            self, fg_color="transparent", border_width=2,
            text="Logout", text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"), command=action)
        self.logout.grid(row=7, column=0, padx=20, pady=20, sticky="s")