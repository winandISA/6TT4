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
