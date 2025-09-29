class Personnage():
    def __init__(self, nom, pv, pa):
        self.__nom = nom
        self.__pv = pv
        self.__pa = pa
        self.__objets = []

    def subirDegat(self, points):
        self.__pv -= points
        if self.__pv < 0:
            self.__pv = 0
        print(f"{self.__nom} a subit {points} dégats et il lui reste {self.__pv} pv.")

    def __soigner(self, points):
        self.__pv += points

    @property
    def nom(self):
        return self.__nom

    @property
    def pv(self):
        return self.__pv

    @property
    def pa(self):
        return self.__pa

    @pv.setter
    def pv(self, val):
        raise ValueError("Modification non autorisée")

    def addObjets(self, objet):
        self.__objets.append(objet)

    def getObjets(self, effet):
        returnList = []
        for objet in self.__objets:
            if objet.effet == effet:
                returnList.append(objet)
        return returnList

    def utiliserObjet(self, objet):
        if objet.effet == "soin":
            self.__soigner(objet.valeur)
            print(f"{objet.nom} a soigné {objet.valeur} pv.")
        self.__objets.remove(objet)

class Objet():
    def __init__(self, nom, effet, valeur):
        self.__nom = nom
        self.__effet = effet
        self.__valeur = valeur

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, val):
        self.__nom = val

    @property
    def effet(self):
        return self.__effet

    @effet.setter
    def effet(self, val):
        self.__effet = val

    @property
    def valeur(self):
        return self.__valeur

    @valeur.setter
    def valeur(self, val):
        self.__valeur = val

mario = Personnage("Mario", 100, 15)
mario.addObjets(Objet("potion 20 pv", "soin", 20))
mario.addObjets(Objet("potion 30 pv", "soin", 30))

bowser = Personnage("Bowser", 100, 20)

while mario.pv != 0 and bowser.pv != 0:
    mario.subirDegat(bowser.pa)
    bowser.subirDegat(mario.pa)
    potions = mario.getObjets("soin")
    if len(potions) > 0:
        mario.utiliserObjet(potions[0])

if mario.pv != 0:
    print("Mario a gagné")
else:
    print("Bowser a gagné")