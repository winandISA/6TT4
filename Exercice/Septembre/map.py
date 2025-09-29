import random

monstre={"vide":[0, 0], "gobelin": [10, 1], "orc":[15, 2] }
recompence = ["vide", "epee", "bouclier", "potion", "potion"]

def createMap(x, y):
    map = []
    for i in range(y):
        ligne = []
        for j in range(x):
            ligne.append([random.choice(list(monstre.keys())), random.choice(recompence), random.randint(0, 100), [1 if i != 0 else 0, 1 if j != x - 1 else 0, 1 if i != y - 1 else 0, 1 if j != 0 else 0, 1]])
        map.append(ligne)
    return map

def displayMap(map):
    print("+-----+-----+-----+-----")
    for ligne in map:
        dLigne = "|"
        rLigne = "|"
        oLigne = "|"
        iLigne = "+"
        for cell in ligne:
            dLigne += f" {cell[0][:3]} |"
            rLigne += f" {cell[1][:3]} {"|" if cell[3][1] == 0 else " "}"
            oLigne += f" {str(cell[2])[:3].ljust(3)} |"
            iLigne += "-----+" if cell[3][2] == 0 else "-   -+"
        print(dLigne)
        print(rLigne)
        print(oLigne)
        print(iLigne)

def generateMap():
    map = createMap(4, 4)
    print(map)
    displayMap(map)

generateMap()
