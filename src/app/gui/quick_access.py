import customtkinter
from datetime import datetime


class JournalEachEntry(customtkinter.CTkFrame):
    def __init__(self, master=None, title="", date="", first_sentence="", tag="", **kwargs):
        super().__init__(master, **kwargs)

        # convert date string to datetime object
        date_obj = datetime.strptime(date, "%Y/%m/%d")

        # get limited text
        text_obj = first_sentence[:69] if len(first_sentence) > 300 else first_sentence

        # create left part of entry
        self.left_frame = customtkinter.CTkFrame(self, fg_color="lightgray")
        self.left_frame.grid(row=0, column=0, rowspan=3, padx=5, pady=5, sticky='w')

        self.day_label = customtkinter.CTkLabel(self.left_frame, height=30, text=date_obj.strftime("%a"), font=("Helvetica", 12, "bold"))
        self.day_label.grid(row=0, column=0, sticky='nsew', padx=5)

        self.date_label = customtkinter.CTkLabel(self.left_frame, height=30, text=date_obj.strftime("%d"), font=("Helvetica", 30, "bold"))
        self.date_label.grid(row=1, column=0, sticky='nsew', padx=5)

        self.month_label = customtkinter.CTkLabel(self.left_frame, height=30, text=date_obj.strftime("%B %Y"), font=("Helvetica", 10, "bold"))
        self.month_label.grid(row=2, column=0, sticky='nsew', padx=5)

        # create right part of entry
        self.right_frame = customtkinter.CTkFrame(self, fg_color="lightgray")
        self.right_frame.grid(row=0, column=1, rowspan=5, columnspan=3, padx=5, pady=5, sticky='nsew')

        self.title_label = customtkinter.CTkLabel(self.right_frame, text=title, font=("Helvetica", 12, "bold"))
        self.title_label.grid(row=0, column=1, padx=5, sticky='nsew')

        self.first_sentence_label = customtkinter.CTkLabel(self.right_frame,
                                                           width=100,
                                                           text=text_obj,
                                                           font=("Helvetica", 10),
                                                           wraplength=100,
                                                           )
        self.first_sentence_label.grid(row=1, column=1, padx=5, sticky='nsew')

        self.tag_label = customtkinter.CTkLabel(self.right_frame, text=f"# {tag}", font=("Helvetica", 11, "italic", "bold"))
        self.tag_label.grid(row=2, column=1, padx=5, sticky='nsew')

        i click each frame, the journal will show on the main window, how can i achive
