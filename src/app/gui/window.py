"""This module create an instance of the Desktop window"""
import customtkinter
import os
from PIL import Image
from collections.abc import Callable
from helpers import View


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

class Window(customtkinter.CTk):
    """Determine characteristics of the GUI window"""
    
    width = 900
    height = 600

    def __init__(self) -> None:
        super().__init__()

        self._set_window_default_parameters()

        self.navigation_bar = self._set_navigation_bar()

        self.top_logo = self._set_top_logo()
        
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
        
        # Navigation button
        self.journal_button = self._set_navigation_button(
            "Journal", self.journal_icon, self._journal_button_event, (1, 0), "ew")
        
        self.planning_button = self._set_navigation_button(
            "Planning", self.planning_icon, self._planning_button_event, (2, 0), "ew")
        
        self.challenges_button = self._set_navigation_button(
            "Challenges", self.challenges_icon, self._challenges_button_event, (3, 0), "ew")
        
        # Create Navigation Views
        
        # Journal View
        self.journal_view = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.journal_view.grid_columnconfigure(0, weight=1)
        self.journal_view_center_button = customtkinter.CTkButton(
            self.journal_view, text="Journal Main View", compound="left")
        self.journal_view_center_button.grid(row=0, column=0, padx=20, pady=10)
        
        # Planning View
        self.planning_view = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.planning_view.grid_columnconfigure(0, weight=1)
        self.planning_view_center_button = customtkinter.CTkButton(
            self.planning_view, text="Planning Main View", compound="left")
        self.planning_view_center_button.grid(row=0, column=0, padx=20, pady=10)
        
        # Challenges View
        self.challenges_view = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.challenges_view.grid_columnconfigure(0, weight=1)
        self.challenges_view_center_button = customtkinter.CTkButton(
            self.challenges_view, text="Challenges Main View", compound="left")
        self.challenges_view_center_button.grid(row=0, column=0, padx=20, pady=10)
        
        self._select_view(View.JOURNAL)



    # PRIVATE METHODS
    def _select_view(self, name: View):
        
        # Reset selection color to transparent
        self.journal_button.configure(fg_color="transparent")
        self.planning_button.configure(fg_color="transparent")
        self.challenges_button.configure(fg_color="transparent")
        
        # dispose of all views before new selection
        self.journal_view.grid_forget()
        self.planning_view.grid_forget()
        self.challenges_view.grid_forget()
        
        # assign new view
        if name == View.JOURNAL:
            self.journal_button.configure(fg_color=("gray75", "gray25"))
            self.journal_view.grid(row=0, column=1, sticky="nsew")
        if name == View.PLANNING:
            self.planning_button.configure(fg_color=("gray75", "gray25"))
            self.planning_view.grid(row=0, column=1, sticky="nsew")
        if name == View.CHALLENGES:
            self.challenges_button.configure(fg_color=("gray75", "gray25"))
            self.challenges_view.grid(row=0, column=1, sticky="nsew")

    
    def _journal_button_event(self):
        self._select_view(View.JOURNAL)
        print("Journal")
    
    def _planning_button_event(self):
        self._select_view(View.PLANNING)
        print("Planning")
    
    def _challenges_button_event(self):
        self._select_view(View.CHALLENGES)
        print("Challenges")
    
    
    def _set_navigation_button(self, title: str,
                               icon: customtkinter.CTkImage,
                               action: Callable[[], None],
                               position: tuple[int, int],
                               stick_to: str)-> customtkinter.CTkButton:
        
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
#     app = Window()
#     app.mainloop()
