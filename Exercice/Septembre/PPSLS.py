import random

resultat = {"Pierre":["Lezard", "Sciseaux"],
            "Lezard":["Spock", "Papier"],
            "Spock":["Sciseaux", "Pierre"],
            "Sciseaux":["Papier", "Lezard"],
            "Papier":["Pierre", "Spock"]}
returnChoix = {"0": "Quitter", "1": "Pierre", "2": "Papier",
               "3": "Sciseaux", "4": "Lezard", "5": "Spock", }

def choixJoueur():
    correct = False
    while not correct:
        print("""Veuillez entrer un choix
        1-Pierre
        2-Papier
        3-Sciseaux
        4-Lezard
        5-Spock
        0-Quitter""")
        choix = input("joueur : ")
        if choix in ["1","2","3","4","5","0"]:
            correct = True
        else:
            print("choix incorrect")
    return returnChoix[choix]


def game(mj, mg, mp):
    choix = choixJoueur()
    choixPc = random.choice(list(resultat.keys()))
    mj += 1
    if choix != "Quitter":
        if choixPc == choix:
            print(f"Le joueur et le PC ont choisi {choixPc}")
        if choix in resultat[choixPc]:
            mp += 1
            print(f"Le pc a gagné, il a choisi {choixPc} et le joueur choisi {choix}")
        else:
            mg += 1
            print(f"Le joueur a gagné, il a choisi {choix} et le PC a choisi {choixPc}")
    return mj, mg, mp, choix

mj = 0
mg = 0
mp = 0

continuer = True
while continuer:
    mj, mg, mp, choix = game(mj, mg, mp)
    if choix == "Quitter":
        continuer = False
    else:
        print(f"mj = {mj}, mg = {mg}, mp = {mp}")
print("bonne journée")