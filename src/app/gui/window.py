"""This module create an instance of the Desktop window"""
import tkinter
import customtkinter


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

class Window(customtkinter.CTk):
    """Determine characteristics of the GUI window"""
    
    def __init__(self) -> None:
        super().__init__()

        # Set the window title and size
        self.title("Your Secret Companion")
        self.geometry("800x600")
        
        # set Grid layout
        self.grid_columnconfigure(1)
        pass


    def button_function(self):
        print("button was pressed!")
    



if __name__ == "__main__":
    app = Window()
    app.mainloop()
