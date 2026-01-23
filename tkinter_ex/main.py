import tkinter as tk

from tkinter_ex.classes.Page.LogIn import LogIn
from tkinter_ex.classes.db.DbConnection import DbConnection


class Main:
    def __init__(self):
        self.root = tk.Tk()
        DbConnection("resources/db/app.db")

        self.current_page = None

        self.show_page(LogIn)
        self.root.mainloop()

    def show_page(self, page_class):

        if self.current_page is not None:
            self.current_page.destroy()

        self.current_page = page_class(self.root, self)
        self.current_page.grid(row=0, column=0, sticky="nsew")

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

Main()
