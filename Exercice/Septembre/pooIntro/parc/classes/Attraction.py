import datetime


class Attraction:
    def __init__(self, nom, capacite, age):
        self.__nom = nom
        self.__capacite = capacite
        self.__age = age
        self.__maintenance = Maintenance(self)
        self.__fileAttente = FileAttente()



class Maintenance:

    def __init__(self, attraction):
        __motif = ""
        __duree = datetime.datetime.now()
        self.__attraction = attraction #passage de la référence à l'attraction pas obligatoire dans l'énoncé mais pertinent dans le cadre d'un développement futur

    def mettreEnMaintenance(self, motif, duree):
        self.__motif = motif
        self.__duree = datetime.datetime.now() + datetime.timedelta(seconds=duree)

    def estEnCours(self):
        return datetime.datetime.now() < self.__duree

    def getMotif(self):
        return self.__motif

class FileAttente:
    def __init__(self, capacite):
        self.__queue = []
        self.__capacite = capacite

    def ajouter(self, visiteur):
        self.__queue.append(visiteur)

    def longueurFile(self):
        return len(self.__queue)

    def prochainRide(self):
        return self.__queue[:self.__capacite]

    def retirerProchains(self):
        del self.__queue[:self.__capacite]

class AttractionFromDB:
    def __init__(self):
        pass #la on se connecte à la DB et on charge nos données

    def getAttractions(self):
        return [{"nom": "Grande roue", "capacite": 20, "age": 0, "VIP": 2},
                {"nom": "Montagne russes", "capacite": 10, "age": 14, "VIP": 1},
                {"nom": "Bateau pirate", "capacite": 15, "age": 12, "VIP": 2},]