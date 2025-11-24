from .TypeVehicule import TypeVehicule
from .PlaceParking import PlaceParking
from .Voiture import Voiture

class Parking(object):
    def __init__(self, nom, places, placesEV, placesPMR):
        self.__nom = nom
        self.__places = {TypeVehicule.STANDARD: [], TypeVehicule.EV: [], TypeVehicule.PMR: []}
        numeroPlace = 1
        for i in range(places):
            if placesPMR != 0:
                self.__places[TypeVehicule.PMR].append(PlaceParking(numeroPlace, TypeVehicule.PMR))
                placesPMR -= 1
            elif placesEV != 0:
                self.__places[TypeVehicule.EV].append(PlaceParking(numeroPlace, TypeVehicule.EV))
                placesEV -= 1
            else:
                self.__places[TypeVehicule.STANDARD].append(PlaceParking(numeroPlace, TypeVehicule.STANDARD))
            numeroPlace += 1

    def __str__(self):
        return f"Le parking {self.__nom} dispose de {self.nbrPlacesLibres()} places libres"

    def garer(self, voiture : Voiture):
        for place in self.places_libre():
            if voiture.type == TypeVehicule.EV and (place.type == TypeVehicule.EV or place.type == TypeVehicule.STANDARD):
                place.gare(voiture)
                return True
            elif voiture.type == place.type:
                place.gare(voiture)
                return True
        return False

    def sortir(self, voiture : Voiture):
        for place in self.places_occupee():
            if place.voiture == voiture:
                place.libere()
                return True
        return False

    def places_libre(self):
        return self.__compterPlaces(self)[0]

    def places_occupee(self):
        return self.__compterPlaces(self)[1]

    @classmethod
    def nbrPlacesLibres(self):
        return len(self.__compterPlaces(self)[0])

    @staticmethod
    def __compterPlaces(self):
        placesLibres = []
        placesOccupees = []
        self.__compterPlacesTypr(self.__places[TypeVehicule.EV], placesLibres, placesOccupees)
        self.__compterPlacesTypr(self.__places[TypeVehicule.PMR], placesLibres, placesOccupees)
        self.__compterPlacesTypr(self.__places[TypeVehicule.STANDARD], placesLibres, placesOccupees)
        return placesLibres, placesOccupees

    @staticmethod
    def __compterPlacesTypr(places, placesLibres, placesOccupees):
        for place in places:
            if place.estLibre():
                placesLibres.append(place)
            else:
                placesOccupees.append(place)