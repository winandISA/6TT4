class Voiture:
    def __init__(self, plaque, modele, type):
        self.__plaque = plaque
        self.__modele = modele
        self.__type = type

    @property
    def plaque(self):
        return self.__plaque
    @property
    def modele(self):
        return self.__modele
    @property
    def type(self):
        return self.__type
    @plaque.setter
    def plaque(self, plaque):
        self.__plaque = plaque
    @modele.setter
    def modele(self, modele):
        self.__modele = modele
    @type.setter
    def type(self, type):
        self.__type = type

