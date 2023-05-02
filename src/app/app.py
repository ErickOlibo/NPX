class App(customtkinter.CTk):

# ############## CREATE THE JOURNAL VIEW HERE ###################################
    def _show_journal_view(self):
        self.navigation_bar.set_active_button(View.JOURNAL)

        # Configure Main app to accomodate Journal View
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure(0, weight=1)

        # Attach Journal View Elements
        self._attach_entry_box()
        self._attach_tags_entry()
        self._attach_save_botton()
        self._attach_delete_button()
        self._attach_edit_button()
        self._attach_clear_button()

    def _forget_journal_view_(self):
        self.tags_entry.grid_forget()
        self.save_button.grid_forget()
        self.entry_box.grid_forget()
        self.delete_button.grid_forget()
        self.edit_button.grid_forget()
        self.clear_button.grid_forget()


