# =========================
# UI Tkinter
# =========================
from tkinter import messagebox, ttk

from tkinter_ex.classes.Page.BasePage import BasePage
from tkinter_ex.classes.Page.CreateUser import CreateUserPage
from tkinter_ex.classes.db.DAO import UserDao


class LogIn(BasePage):
    def __init__(self, parent, controller):
        self.dao = UserDao()

        parent.title("Login")
        parent.geometry("500x200")
        parent.resizable(False, False)

        super().__init__(parent, controller)

        self.frame_connect = tk.LabelFrame(self.root, text="Connexion", padx=10, pady=10)
        self.frame_connect.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")


        tk.Label(self.frame_connect, text="Utilisateur :").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        tk.Label(self.frame_connect, text="Mot de passe :").grid(row=1, column=0, sticky="e", padx=5, pady=5)

        self.combo_user = ttk.Combobox(self.frame_connect, width=22, state="readonly")
        self.refresh_users()

        self.entry_connect_pwd = tk.Entry(self.frame_connect, width=25, show="*")
        self.combo_user.grid(row=0, column=1, padx=5, pady=5)
        self.entry_connect_pwd.grid(row=1, column=1, padx=5, pady=5)
        self.btn_switch = tk.Button(
            self.frame_connect,
            text="Créer un compte",
            command=self.handle_switch,
            bg=self.RED,
            fg="white"
        )
        self.btn_switch.grid(row=2, column=0, pady=10)
        self.btn_connect = tk.Button(self.frame_connect, text="Connect", width=12, command=self.on_connect)
        self.btn_connect.grid(row=2, column=1, pady=10)

    def on_connect(self):
        nom = self.combo_user.get().strip()
        pwd = self.entry_connect_pwd.get().strip()
        if not nom or not pwd:
            messagebox.showerror("Erreur", "Nom et mot de passe obligatoires.")
            return
        if self.dao.user_exists(nom, pwd):
            messagebox.showinfo("Connexion", "Accès autorisé ✅")
        else:
            messagebox.showerror("Connexion", "Accès refusé ❌")

    def refresh_users(self):
        users = self.dao.get_all_usernames()
        self.combo_user["values"] = users
        if users:
            self.combo_user.current(0)  # sélectionne le premier
        else:
            self.combo_user.set("")  # vide si aucun user

    def handle_switch(self):
        self.controller.show_page(CreateUserPage)
