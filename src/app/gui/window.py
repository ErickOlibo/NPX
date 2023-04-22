"""This module create an instance of the Desktop window"""
# import tkinter
import customtkinter
import os
from PIL import Image


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




    def button_function(self):
        print("button was pressed!")

    # PRIVATE METHODS
    def _set_window_default_parameters(self):
        # Set the window title and size
        self.title("Your Secret Companion")
        self.geometry(f"{self.width}x{self.height}")

        # set Grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # set assets folder path
        self.assets_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "assets")

    
    def _getImage(self, path)-> Image:
        return Image.open(os.path.join(self.assets_path, path))
    
    def _set_top_logo(self):
        logo_image = customtkinter.CTkImage(
            self._getImage("npx_logo.png"), size=(30, 30))
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


if __name__ == "__main__":
    app = Window()
    app.mainloop()
