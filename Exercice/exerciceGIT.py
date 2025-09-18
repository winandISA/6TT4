print("coucou")

Biblio = {"Martine à la ferme": ["Martine à la ferme","Martin", "1975", "Jeunessetrt"]}
Continue = True
while Continue:
    titre = input("Titre: ")
    auteur = input("Auteur: ")
    annee = input("Annee: ")
    genre = input("Genre: ")
    Biblio[titre] = [titre, auteur, annee, genre]
    if input("Continue? (y/n): ").lower() == "n":
        Continue = False
print(Biblio)
for key in Biblio:
    print(f"Titre: {Biblio[key][0]}, Auteur: {Biblio[key][1]}")

