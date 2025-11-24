from Exercice.Septembre.domotique.classes.Tool import Lampe, Thermostat


class Piece:
    def __init__(self, nom):
        self.__nom = nom
        self.__lampe = Lampe(nom)
        self.__thermostat = Thermostat(nom, 20)
        self.__lampe.piece = self

    def jour(self):
        self.__lampe.eteindre()
        self.__thermostat.temperature = 18

    def soirée(self):
        self.__lampe.allumer()
        self.__lampe.intensite = 100
        self.__thermostat.temperature = 21

    def lecture(self):
        self.__lampe.allumer()
        self.__lampe.intensite = 65
        self.__thermostat.temperature = 22

    @property
    def nom(self):
        return self.__nom

    def __str__(self):
        return f"{self.__nom} {self.__lampe} {self.__lampe.intensite} {self.__thermostat.temperature}"

