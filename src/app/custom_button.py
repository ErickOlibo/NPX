"""This module create a object of class CTK Button."""
import customtkinter


class CustomButton(customtkinter.CTkButton):
    """A Custom TKinter Button to embeded in the GUI."""
    def __init__(self, master, label: str, action):
        """Create a button of type CTkButton with the proper attributes."""
        super().__init__(master)
        self._label = str(label).lower().capitalize()
        self._action = action
        self.configure(
            text=self._label,
            command=action,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "gray90")
        )

    @property
    def hidden(self):
        """Set the button to disable and hidden out of the GUI."""
        self.configure(border_width=0, text="", state="disabled")

    @property
    def visible(self):
        """Set the button to enable and showwing in the GUI."""
        self.configure(border_width=2, text=self._label, state="normal")
