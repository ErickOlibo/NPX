import customtkinter
from datetime import datetime


class JournalEachEntry(customtkinter.CTkButton):
    def __init__(self, master=None, title="", date="", first_sentence="", tag="", **kwargs):
        super().__init__(master, fg_color="transparent", hover_color="gray70", **kwargs)
        self.create_left_frame(date)
        self.create_right_frame(title, first_sentence, tag)

    def create_left_frame(self, date):
        # convert date string to datetime object
        date_obj = datetime.strptime(date, "%Y/%m/%d")

        # create left part of entry
        self.left_frame = customtkinter.CTkFrame(self, fg_color="lightgray")
        self.left_frame.grid(row=0, column=0, rowspan=3, padx=3, pady=3, sticky='w')

        self.day_label = customtkinter.CTkLabel(self.left_frame, height=30, text=date_obj.strftime("%a"), font=("Helvetica", 12, "bold"))
        self.day_label.grid(row=0, column=0, sticky='nsew', padx=5)

        self.date_label = customtkinter.CTkLabel(self.left_frame, height=30, text=date_obj.strftime("%d"), font=("Helvetica", 30, "bold"))
        self.date_label.grid(row=1, column=0, sticky='nsew', padx=5)

        self.month_label = customtkinter.CTkLabel(self.left_frame, height=30, text=date_obj.strftime("%B %Y"), font=("Helvetica", 10, "bold"))
        self.month_label.grid(row=2, column=0, sticky='nsew', padx=5)

    def create_right_frame(self, title, first_sentence, tag):
        # get limited text
        text_obj = first_sentence[:69] if len(first_sentence) > 300 else first_sentence

        # create right part of entry
        self.right_frame = customtkinter.CTkFrame(self, fg_color="lightgray")
        self.right_frame.grid(row=0, column=1, rowspan=3, columnspan=3, padx=3, pady=3, sticky='nsew')

        self.title_label = customtkinter.CTkLabel(self.right_frame, text=title, font=("Helvetica", 12, "bold"))
        self.title_label.grid(row=0, column=1, sticky='nsew')

        self.first_sentence_label = customtkinter.CTkLabel(self.right_frame,
                                                           width=110,
                                                           height=5,
                                                           text=text_obj,
                                                           font=("Helvetica", 10),
                                                           wraplength=100,
                                                           )
        self.first_sentence_label.grid(row=1, column=1, sticky='nsew')

        self.tag_label = customtkinter.CTkLabel(self.right_frame, text=f"# {tag}",
                                                font=("Helvetica", 11, "italic", "bold"))
        self.tag_label.grid(row=2, column=1, sticky='s')
