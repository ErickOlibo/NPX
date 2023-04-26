"""This module test main app class using unittest."""

import unittest
import customtkinter
from main_app import MainApp

class TestMainApp(unittest.TestCase):
    """Test classes and methods using UnitTest."""
    
    def setUp(self):
        self.app = MainApp()
    
    # def tearDown(self) -> None:
    #     self.app.forget()
    #     return super().tearDown()

    def test_prepare_login_view(self):
        self.assertEqual(self.app.resizable(), (False, False))
        self.assertIsInstance(self.app.login_view, customtkinter.CTkFrame)
    
    # def test_prepare_main_view(self):
    #     app = MainApp()
        
    #     pass
    
    # def test_set_logout_button(self):
    #     #app = MainApp()
    #     self.assertIsInstance(self.app.logout, customtkinter.CTkButton)
    #     pass
    
    # def test_logging_out_pressed(self):
    #     pass
    
    # def test_set_mode_menu(self):
    #     pass
    
    # def test_change_appearance_mode_event(self):
    #     pass
    
    # def test_navigation_buttons(self):
    #     pass
    
    # def test_journal_planning_challenges_button_event(self):
    #     pass
    
    # def test_selected_view(self):
    #     pass
    
    # def test_reset_views_buttons(self):
    #     pass
    
    # def test_set_active_view_button(self):
    #     pass
    
    # def test_navigation_icons(self):
    #     pass
    
    # def test_light_dark_image(self):
    #     pass
    
    # def test_set_navigation_button(self):
    #     pass
    
    # def test_set_top_logo(self):
    #     pass
    
    # def test_set_navigation_bar(self):
    #     pass
    
    # def test_set_main_view_default_parameters(self):
    #     pass
    
    # def test_login_event(self):
    #     pass
    
    # def test_attach_title_credentials(self):
    #     pass
    
    # def test_attach_logo_to_login_view(self):
    #     pass
    
    # def test_getImage(self):
    #     pass
    
    # def test_get_temporary_main_views(self):
    #     pass
    
    # def test_set_temp_view(self):
    #     pass
    
    


if __name__ == '__main__':
    unittest.main()