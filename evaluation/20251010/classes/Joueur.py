class Joueur:
    def __init__(self, nom_joueur):
        self.__nom_joueur = nom_joueur
        self.__kill = 0
        self.__death = 0
        self.__assist = 0
        self.__won = 0
        self.__lost = 0

    def addKDA(self, kill, death, assist):
        self.__kill = kill
        self.__death = death
        self.__assist = assist

    def addWinLoss(self, won):
        if won:
            self.__won += 1
        else:
            self.__lost += 1

    def getRatios(self):
        return self.__won / (self.__won + self.__lost), (self.__kill + (0.5 * self.__assist))/self.__death

    def getNomJoueur(self):
        return self.__nom_joueur


