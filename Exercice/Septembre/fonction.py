def calculCarre():
    cote = int(input("cote : "))
    return calculAire(cote, cote)

def calculRect():
    longueur = int(input("longueur : "))
    largeur = int(input("largeur : "))
    return calculAire(longueur, largeur)

def calculTriangle():
    base = int(input("base : "))
    hauteur = int(input("hauteur : "))
    return (calculAire(base, hauteur)) / 2


def calculAire(base, hauteur):
    return base * hauteur


def calculAires():
    print("""Quelle aire voulez vous calculer
    1. rectangle
    2. Carré
    3. triangle
    4.quitter""")
    choix = int(input("choix : "))
    if choix == 1:
        result = calculRect()
    if choix == 2:
        result = calculCarre()
    if choix == 3:
        result = calculTriangle()
    if choix == 4:
        return False
    print(f"le résultat est : {result}")
    return True

continuer = True
while continuer:
    continuer = calculAires()