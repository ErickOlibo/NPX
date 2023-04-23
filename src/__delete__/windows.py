"""This module create an instance of the Desktop mainwindow"""
import customtkinter
import os
from PIL import Image
from collections.abc import Callable
from helpers import View


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

class LoginWindow(customtkinter.CTk):
    """Instantiate the Login view with its characteristics"""

    width = 300
    height = 300
    
    def __ini__(self) -> None:
        super().__init__()
        
        self.title("Login Page")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # self.assets_path = os.path.join(
        #     os.path.dirname(os.path.realpath(__file__)), "assets")
        
        self.login_view = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_view.grid(row=0, column=0, sticky="ns")
        self.login_label = customtkinter.CTkLabel(
            self.login_view, text="NPX App\nLogin Page",
            font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        
        self.username = customtkinter.CTkEntry(self.login_view, width=200, placeholder_text="username")
        self.username.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.password = customtkinter.CTkEntry(self.login_view, width=200, show="*", placeholder_text="password")
        self.password.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.login_button = customtkinter.CTkButton(self.login_view, text="Login", command=self.login_pressed, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))
        
        pass
    
    def login_pressed(self):
        print("Login Pressed!")
        pass
    


class MainWindow(customtkinter.CTk):
    """Determine characteristics of the Main window at app launch"""
    
    width = 900
    height = 600

    def __init__(self) -> None:
        super().__init__()

        self._set_window_default_parameters()

        self.navigation_bar = self._set_navigation_bar()

        self.top_logo = self._set_top_logo()

        self._navigation_icons()

        self._navigation_buttons()
        
        self._get_journal_view()
        self._get_planning_view()
        self._get_challenges_view()

        self._selected_view(View.JOURNAL)
        
        self._set_mode_menu()




    # PRIVATE METHODS
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
    
    def _get_journal_view(self):
        self.journal_view = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.journal_view.grid_columnconfigure(0, weight=1)
        self.journal_view_center_button = customtkinter.CTkButton(
            self.journal_view, text="Journal Main View", compound="left")
        self.journal_view_center_button.grid(row=0, column=0, padx=20, pady=10)
    
    def _get_planning_view(self):
        self.planning_view = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.planning_view.grid_columnconfigure(0, weight=1)
        self.planning_view_center_button = customtkinter.CTkButton(
            self.planning_view, text="Planning Main View", compound="left")
        self.planning_view_center_button.grid(row=0, column=0, padx=20, pady=10)
    
    def _get_challenges_view(self):
        self.challenges_view = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.challenges_view.grid_columnconfigure(0, weight=1)
        self.challenges_view_center_button = customtkinter.CTkButton(
            self.challenges_view, text="Challenges Main View", compound="left")
        self.challenges_view_center_button.grid(row=0, column=0, padx=20, pady=10)

    def _journal_button_event(self):
        self._selected_view(View.JOURNAL)
        print("Journal")
    
    def _planning_button_event(self):
        self._selected_view(View.PLANNING)
        print("Planning")
    
    def _challenges_button_event(self):
        self._selected_view(View.CHALLENGES)
        print("Challenges")
    
    
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
        
    
    #def _set_default_window(self, title, size, )
    
    def _set_window_default_parameters(self):
        # Set the window title and size
        self.title("Your Secret Companion")
        self.geometry(f"{self.width}x{self.height}")

        # set Grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # set assets folder path
        self.assets_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "assets")

    def _getImage(self, path: str)-> Image:
        return Image.open(os.path.join(self.assets_path, path))

    def _set_top_logo(self):
        logo_image = customtkinter.CTkImage(
            self._getImage("npx_logo.png"), size=(35, 35))
        top_logo = customtkinter.CTkLabel(
            self.navigation_bar, text="     NPX App", image=logo_image,
            compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        top_logo.grid(row=0, column=0, padx=20, pady=20)
        return top_logo

    def _set_navigation_bar(self):
        navigation_bar = customtkinter.CTkFrame(self, corner_radius=0)
        navigation_bar.grid(row=0, column=0, sticky="nsew")
        navigation_bar.grid_rowconfigure(4, weight=1)
        return navigation_bar


# if __name__ == "__main__":
#     app = MainWindow()
#     app.mainloop()
