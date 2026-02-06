import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageLoaderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sélecteur d'images")
        self.geometry("600x500")

        # Widget d'affichage (Zone de texte / Label)
        self.path_label = tk.Label(self, text="Aucun fichier sélectionné", fg="grey")
        self.path_label.pack(pady=10)

        # Bouton Load
        self.load_btn = tk.Button(self, text="Load Image", command=self.open_file)
        self.load_btn.pack(pady=5)

        # Zone d'affichage de l'image
        self.canvas = tk.Label(self)
        self.canvas.pack(expand=True)

    def open_file(self):
        # Configuration du sélecteur (Filtres images)
        filetypes = [("Images", "*.jpg *.jpeg *.png *.bmp *.gif"), ("Tous les fichiers", "*.*")]
        filepath = filedialog.askopenfilename(title="Ouvrir une image", filetypes=filetypes)

        if filepath:
            self.path_label.config(text=filepath, fg="black")
            self.display_image(filepath)

    def display_image(self, path):
        # Utilisation de Pillow pour charger et redimensionner
        img = Image.open(path)
        img.thumbnail((400, 400))  # Garde le ratio, max 400px

        # Conversion pour Tkinter
        self.photo = ImageTk.PhotoImage(img)
        self.canvas.config(image=self.photo)


if __name__ == "__main__":
    app = ImageLoaderApp()
    app.mainloop()