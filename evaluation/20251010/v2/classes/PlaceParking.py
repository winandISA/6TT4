from .Voiture import Voiture
from .TypeVehicule import TypeVehicule


class PlaceParking:
    def __init__(self, numero, type):
        self.__numero = numero
        self.__type = type
        self.__voiture : Voiture = None

    def gare(self, voiture):
        if voiture.type == self.__type:
            self.__voiture = voiture
            return True
        elif self.__type == TypeVehicule.STANDARD and (voiture.type == TypeVehicule.EV or voiture.type == TypeVehicule.PMR):
            self.__voiture = voiture
            return True
        else:
            return False

    def libere(self):
        self.__voiture = None

    def estLibre(self):
        return self.__voiture is None

    @property
    def numero(self):
        return self.__numero

    @property
    def type(self):
        return self.__type

    @property
    def voiture(self):
        return self.__voiture
