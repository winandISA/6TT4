import tkinter as tk


class BasePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        self.controller = controller
        self.root = parent
        self.root.columnconfigure(0, weight=0, minsize=150)
        self.root.columnconfigure(1, weight=1)
        self.BLUE = "#1a466a"
        self.RED = "#d32f2f"
        self.FONT_BOLD = ("Helvetica", 10, "bold")

        # Initialisation du logo (commun à toutes les pages)
        self._init_logo()

    def _init_logo(self):
        # Utilisation de resources/images/logo.png
        self.logo_img = tk.PhotoImage(file="resources/images/logo.png")
        lbl_logo = tk.Label(self, image=self.logo_img, bg="white")
        lbl_logo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")