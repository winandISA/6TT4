from Exercice.Septembre.pooIntro.parc.classes.Attraction import AttractionFromDB, Attraction


class Parc:
    def __init__(self, nom):
        self.__nom = nom
        self.__ouvert = False
        self.__attractions = {}
        chargement = AttractionFromDB()
        listeAttraction = chargement.getAttractions()
        for attraction in listeAttraction:
            listeAttraction[attraction["nom"]] = Attraction(attraction["nom"], attraction["capacite"], attraction["age"])

    def ouvrir(self):
        self.__ouvert = True

    def fermer(self):
        self.__ouvert = False

    def getAttraction(self, nom):
        return self.__attractions[nom]


