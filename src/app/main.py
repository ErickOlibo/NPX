"""
===== NPX App =====

some docstring here to explain the purpose and how to use
"""
import tkinter
import customtkinter



def main():
    """Run the main program."""
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    app = customtkinter.CTk()
    app.geometry("400x240")
    button = customtkinter.CTkButton(master=app, text="Press Here!", command=button_function)
    button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    app.mainloop()
    
    
def button_function():
    print("Button Pressed!")
    


if __name__ == "__main__":
    main()
