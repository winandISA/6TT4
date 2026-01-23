import tkinter as tk
from tkinter import messagebox

from exercices.tkinter.classes.Page.BasePage import BasePage
from exercices.tkinter.classes.db.DAO import UserDao


class CreateUserPage(BasePage):
    def __init__(self, parent, controller):
        self.dao = UserDao()

        parent.title("Create User")
        parent.geometry("500x200")
        parent.resizable(False, False)

        super().__init__(parent, controller)

        self.frame_add = tk.LabelFrame(self.root, text="Ajouter un utilisateur", padx=10, pady=10)
        self.frame_add.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        # Labels
        tk.Label(self.frame_add, text="Nom :").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        tk.Label(self.frame_add, text="Mot de passe :").grid(row=1, column=0, padx=10, pady=10, sticky="e")

        # Entries
        self.entry_add_nom = tk.Entry(self.frame_add, width=25)
        self.entry_add_pwd = tk.Entry(self.frame_add, width=25, show="*")

        self.entry_add_nom.grid(row=0, column=1, padx=10, pady=10)
        self.entry_add_pwd.grid(row=1, column=1, padx=10, pady=10)

        # Buttons
        self.btn_switch = tk.Button(
            self.frame_add,
            text="Log In",
            command=self.handle_switch,
            bg=self.RED,
            fg="white"
        )
        self.btn_switch.grid(row=2, column=0, pady=10)
        self.btn_add = tk.Button(self.frame_add, text="Add", width=12, command=self.on_add)
        self.btn_add.grid(row=2, column=1, padx=10, pady=10)

    def on_add(self):
        nom = self.entry_add_nom.get().strip()
        pwd = self.entry_add_pwd.get().strip()
        if not nom or not pwd:
            messagebox.showerror("Erreur", "Nom et mot de passe obligatoires.")
            return
        ok = self.dao.add_user(nom, pwd)
        if ok:
            messagebox.showinfo("OK", f"Utilisateur '{nom}' ajouté.")
            self.entry_add_pwd.delete(0, tk.END)
        else:
            messagebox.showerror("Erreur", f"Le nom '{nom}' existe déjà.")

    def handle_switch(self):
        from exercices.tkinter.classes.Page.LogIn import LogIn
        self.controller.show_page(LogIn)
