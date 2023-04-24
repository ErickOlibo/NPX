import customtkinter
from collections.abc import Callable
from helpers import View, Assets, CustomImage, CustomTabButton

class NavigationBar(customtkinter.CTkFrame):

    def __init__(self, master,
                 journal: Callable[[], None],
                 planning: Callable[[], None],
                 challenges: Callable[[], None],
                 logout: Callable[[], None]):
        super().__init__(master)
        self._attach_logo()
        self._navigation_icons()
        self._navigation_buttons_v2(journal, planning, challenges)
        self._set_mode_menu()
        self._set_logout_button(logout)


    def _reset_navigation_buttons_color(self):
        color = "transparent"
        self.journal_button.configure(fg_color=color)
        self.planning_button.configure(fg_color=color)
        self.challenges_button.configure(fg_color=color)
    
    def set_active_button(self, tab: View):
        self._reset_navigation_buttons_color()
        color = ("gray75", "gray25")
        if tab == View.JOURNAL: self.journal_button.configure(fg_color=color)
        if tab == View.PLANNING: self.planning_button.configure(fg_color=color)
        if tab == View.CHALLENGES: self.challenges_button.configure(fg_color=color)


    def _attach_logo(self):
        logo_image = CustomImage((35, 35),Assets.NPX_LOGO).image
        self.top_logo = customtkinter.CTkLabel(
            self, text="     NPX App", image=logo_image,
            compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.top_logo.grid(row=0, column=0, padx=20, pady=20)

    
    def _navigation_icons(self):
        size = (26, 26)
        self.journal_icon = CustomImage(size, Assets.LIGHT_JOURNAL, Assets.DARK_JOURNAL).image
        self.planning_icon = CustomImage(size, Assets.LIGHT_PLANNING, Assets.DARK_PLANNING).image
        self.challenges_icon = CustomImage(size, Assets.LIGHT_CHALLENGES, Assets.DARK_CHALLENGES).image


    def _navigation_buttons_v2(self, jour, plan, chall):
        self.journal_button = CustomTabButton(self,
            "Journal", self.journal_icon, jour, (1, 0), "ew").button
        self.planning_button = CustomTabButton(self,
            "Planning", self.planning_icon, plan, (2, 0), "ew").button
        self.challenges_button = CustomTabButton(self,
            "Challenges", self.challenges_icon, chall, (3, 0), "ew").button
    
    
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

