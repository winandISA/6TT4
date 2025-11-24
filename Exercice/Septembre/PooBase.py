class Pernnage:
    def __init__(self, nom, pv):
        self.nom = nom
        self.__pv = pv

    def prendDegat(self, pdegat):
        self.__pv -= pdegat


    def getPv(self):
        return self.__pv
    def getNom(self):
        return self.nom
    def setPv(self, pv):
        self.__pv = pv
    def setNom(self, nom):
        self.nom = nom

link = Pernnage("Link", 100)
link.nom = ""
link.pv = 0
print(link.pv)
print(link.getPv())
link.setPv(95)
link.prendDegat(5)
