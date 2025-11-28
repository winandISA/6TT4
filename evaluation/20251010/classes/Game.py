import random

from Exercice.Septembre.PPSLS import resultat


class Game:
    def __init__(self, id, players):
        self.id = id
        self.__team1 = players[:]
        self.__team2 = []
        self.__ret1 = []
        self.__ret2 = []
        for i in range(5):
            self.__team2.append(random.choice(self.__team1))
            self.__team1.remove(self.__team2[i])
    def __calcValue(self, solde):
        val = random.randint(1 - 25)
        if solde < val:
            val = solde
        solde -= val
        return solde, val

    def __playTeam(self, team, kills, deaths):
        assists = 0
        for player in team:
            kills, kill = self.__calcValue(kills)
            deaths, death = self.__calcValue(deaths)
            assist = random.randint(1 - 25)
            player.addKDA(kill, death, assist)
            assists += assist
        if kills > 0:
            team[4] += kills
        if deaths > 0:
            team[4] += deaths
        return assists


    def playGame(self):
        resultat = random.choice(True, False)
        looseKills = random.randint(80, 99)
        self.__playTeam(self.__team1 if resultat else self.__team2, 100, looseKills)
        self.__playTeam(self.__team2 if resultat else self.__team1, looseKills, 100)


