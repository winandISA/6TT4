class Lampe:
    def __init__(self, nom):
        self.__nom = nom
        self.__intensite = 0
        self.__etat = False
        self.__piece = None

    def allumer(self):
        self.__etat = True

    def eteindre(self):
        self.__etat = False

    def estAllumé(self):
        return self.__etat



#Getter Setter
    @property
    def nom(self):
        return self.__nom

    @property
    def intensite(self):
        return self.__intensite

    @intensite.setter
    def intensite(self, value):
        self.__intensite = value

    @property
    def piece(self):
        return self.__piece

    @piece.setter
    def piece(self, value):
        self.__piece = value

class Thermostat:
    def __init__(self, nom, temperature):
        self.__nom = nom
        self.__temperature = temperature

    @property
    def nom(self):
        return self.__nom

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        self.__temperature = value
