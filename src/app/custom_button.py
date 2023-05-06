import customtkinter


class CustomButton(customtkinter.CTkButton):

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

    def hidden(self):
        self.configure(border_width=0, text="", state="disabled")

    def visible(self):
        self.configure(border_width=2, text=self._label, state="enabled")
