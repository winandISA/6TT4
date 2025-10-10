import datetime

from Exercice.Septembre.pooIntro.parc.classes.Attraction import AttractionFromDB


class Visiteur:
    def __init__(self, nom, age, passVIP = False):
        self.__nom = nom
        self.__age = age
        if passVIP:
            self.__billet = Billet()
        else:
            listeAttraction =  AttractionFromDB().getAttractions()
            attractionNonVIP = {}
            for attraction in listeAttraction:
                attractionNonVIP[attraction["nom"]] = attraction["VIP"]
            self.__billet = Billet([attractionNonVIP])

    def peutEmbarquer(self, attraction):
        if attraction["age"] <= self.__age and self.__billet.isValid():
            return self.__billet.peutEmbarquer(attraction["nom"])
        else:
            return False

    def sortieDefinitive(self):
        self.__billet.sortieDefinitive()

    def getBilletNr(self):
        return self.__billet.getId()

    def getNom(self):
        return self.__nom

class Billet:
    __cptId = 0
    def __init__(self, attractions = None):
        self.__id = Billet.__cptId
        Billet.__cptId += 1
        self.__h_entree = datetime.datetime.now()
        self.__h_sortie = None
        self.__attractions = attractions

    def peutEmbarquer(self, nomAttraction):
        if self.__attractions == None:
            return True
        else:
            if self.__attractions[nomAttraction] == 0:
                return False
            else:
                return True

    def sortieDefinitive(self):
        self.__h_sortie = datetime.datetime.now()

    def isValid(self):
        return self.__h_sortie == None

    def getId(self):
        return self.__id
