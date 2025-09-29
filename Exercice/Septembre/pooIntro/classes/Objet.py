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
