import customtkinter
import textwrap
from datetime import datetime
from src.app.sql_handler import SQLHandler


class JournalEachEntry(customtkinter.CTkFrame):
    def __init__(self, master=None, id="", title="", date="", first_sentence="", time="", tag="", **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self._handler = SQLHandler()
        self.create_left_frame(date, id)
        self.create_right_frame(title, first_sentence, tag, time, id)
        # self.bind("<Button-1>", lambda event: self.on_click(id))
        # print(time)

    def create_left_frame(self, date, id):
        # from journal_view import JournalView
        # convert date string to datetime object
        date_obj = datetime.strptime(date, "%Y/%m/%d")

        # create left part of entry
        self.left_frame = customtkinter.CTkButton(self, hover_color="gray70",
                                                  fg_color="lightgray",
                                                  width=35,
                                                  height=40,
                                                  text_color="black",
                                                  text=date_obj.strftime("%e\n%b"),
                                                  font=("Helvetica", 15, "bold"))
        self.left_frame.grid(row=0, column=0, rowspan=3, padx=2, pady=2, sticky='w')

        # self.day_label = customtkinter.CTkLabel(self.left_frame, height=30, text=date_obj.strftime("%a"),
        #                                         font=("Helvetica", 12, "bold"))
        # self.day_label.grid(row=0, column=0, sticky='nsew', padx=5)

        # self.date_label = customtkinter.CTkLabel(self.left_frame, height=30, text=date_obj.strftime("%d"),
        #                                          font=("Helvetica", 30, "bold"))
        # self.date_label.grid(row=1, column=0, sticky='nsew', padx=5)

        # self.month_label = customtkinter.CTkLabel(self.left_frame, height=30, text=date_obj.strftime("%d %B"),
        #                                           font=("Helvetica", 10, "bold"))
        # self.month_label.grid(row=2, column=0, sticky='nsew', padx=5)

    def create_right_frame(self, title, first_sentence, tag, time, id):
        # from journal_view import JournalView
        # get limited text
        # text_obj = first_sentence[:69] if len(first_sentence) > 300 else first_sentence

        # get limited title
        wrapped_lines = textwrap.wrap(title, width=20)
        if len(wrapped_lines) > 2:
            wrapped_lines = wrapped_lines[:2]
            last_line = wrapped_lines[-1] + '...'
            wrapped_lines = wrapped_lines[:-1] + [last_line]
        title_obj = '\n'.join(wrapped_lines)

        # create right part of entry
        self.right_frame = customtkinter.CTkButton(self, hover_color="gray70",
                                                   fg_color="lightgray",
                                                   width=110,
                                                   text=f"{title_obj}",
                                                   text_color="black",
                                                   font=("Helvetica", 11))
        self.right_frame.grid(row=0, column=1, rowspan=3, columnspan=3, padx=2, pady=2, sticky='nsew')

        # self.title_label = customtkinter.CTkLabel(self.right_frame, text=title, font=("Helvetica", 12, "bold"))
        # self.title_label.grid(row=0, column=1, sticky='nsew')
        #
        # self.first_sentence_label = customtkinter.CTkLabel(self.right_frame,
        #                                                    width=110,
        #                                                    text=text_obj,
        #                                                    font=("Helvetica", 10),
        #                                                    wraplength=100,
        #                                                    )
        # self.first_sentence_label.grid(row=1, column=1, sticky='nsew')
        #
        # self.tag_label = customtkinter.CTkLabel(self.right_frame, text=f"# {tag}",
        #                                         font=("Helvetica", 11, "italic", "bold"))
        # self.tag_label.grid(row=2, column=1, sticky='s')

    # on_click function is currently disabled with no function but just clickable
    # def on_click(self, id):
    #     return  id
