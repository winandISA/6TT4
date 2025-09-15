import random

def createGrid():
    return [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

def findAxis(position):
# calcule les axes x et y sur base d'une position entre 1 et 9
# le -1 permet d'ajuster les valeurs a des index entre 0 et 2
    y = (position -1) // 3
    x = (position - 1) % 3
    return x, y

def printGrid(grid):
    for i in range(len(grid)):
        print(f" {grid[i][0]} | {grid[i][1]} | {grid[i][2]}")
        if i != len(grid) - 1:
            print("---+---+--")

def placeSign(grid, position, signe):
    x, y = findAxis(position)
    if grid[y][x] == " ":
        grid[y][x] = signe
        return True, grid
    return False, grid

def place(grid, player):
    correctPlace = False
    while not correctPlace:
        if player:
            try:
                printGrid(grid)
                print("""Choisissez une case (libre) entre 1 et 9
 1 | 2 | 3 
---+---+-- 
 4 | 5 | 6 
---+---+-- 
 7 | 8 | 9 """)
                correctPlace, grid = placeSign(grid, int(input("Enter the position on the grid: ")), "X")
                if not correctPlace:
                    print("la position est déjà choisie")
            except:
                print("valeur incorrecte")
        else:
            correctPlace, grid = placeSign(grid, random.randint(1, 9), "0")
    return not player

def checkFinished(grille):
    win = " "
    for i in range(len(grille[0])):
        if grille[0][i] == grille[1][i] == grille[2][i] and grille[0][i] != " ":
            win = grille[0][i]
    for ligne in grille:
        if ligne[0] == ligne[1] == ligne[2] and ligne[0] != " ":
            win = ligne[0]
    if (grille[0][0] == grille[1][1] == grille[2][2] and grille[0][0] != " ") or (grille[2][0] == grille[1][1] == grille[0][2] and grille[0][0] != " "):
        win = grille[1][1]
    if win != " ":
        if win == "X":
            print("Le joueur a gagné")
        else:
            print("Le PC a gagné")
        return True
    else:
        cpt = 0
        for ligne in grille:
            for cell in ligne:
                if cell == " ":
                    cpt += 1
        if cpt == 0:
            print("Match nul")
            return True
    return False

grid = createGrid()
a = int("a")
player = random.choice([True, False])
#choisi qui joue en premier, si True, c'est le joeur sinon, c'est le cpt
print("coucou3")
if not player:
    player = place(grid, player)
    print("Le PC commence")
else:
    print("Le joueur commence")

while not checkFinished(grid):
    player = place(grid, player)

