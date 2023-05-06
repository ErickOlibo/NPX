import customtkinter

class CustomButton:

    def __init__(self, master, label: str, action):
        """Create a button of type CTkButton with the proper attributes."""
        self._label = str(label).lower().capitalize()
        self._action = action
        self._button = customtkinter.CTkButton(
            master, text=self._label,
            command=action,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "gray90")
        )

    def get(self) -> customtkinter.CTkButton:
        return self._button