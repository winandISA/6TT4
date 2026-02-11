import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime


class LogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monitor Log - Pace Tracker")
        self.root.geometry("400x300")

        # 1. La Textbox (en haut)
        # On utilise expand=True pour qu'elle occupe l'espace
        self.log_area = scrolledtext.ScrolledText(root, height=10, state='disabled')
        self.log_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # 2. Conteneur pour les boutons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        # Bouton Ajouter
        self.btn_add = tk.Button(btn_frame, text="Ajouter Log", command=self.add_log)
        self.btn_add.pack(side=tk.LEFT, padx=5)

        # Bouton Vider
        self.btn_clear = tk.Button(btn_frame, text="Vider & Log", command=self.clear_and_log)
        self.btn_clear.pack(side=tk.LEFT, padx=5)

    def add_log(self):
        now = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{now}] Nouveau log enregistré...\n"

        # En Tkinter, pour modifier un texte 'disabled', il faut l'ouvrir temporairement
        self.log_area.configure(state='normal')

        # On insère à la fin ('end')
        self.log_area.insert(tk.END, log_entry)

        # Auto-scroll vers le bas
        self.log_area.see(tk.END)

        self.log_area.configure(state='disabled')

    def clear_and_log(self):
        self.log_area.configure(state='normal')

        # On efface de l'index 1.0 (début) à la fin
        self.log_area.delete('1.0', tk.END)

        self.log_area.configure(state='disabled')
        self.add_log()


if __name__ == "__main__":
    root = tk.Tk()
    app = LogApp(root)
    root.mainloop()