from .Asset import *
import pygame

class Game():
    def __init__(self, fond, player, win):
        self.fond = fond
        self.player = player
        self.rocket = []
        self.win = win

    def getFond(self):
        return self.fond

    def getPlayer(self):
        return self.player

    def addRocket(self, rocket):
        self.rocket.append(rocket)

    def move(self, mousePos):
        self.player.bouge(mousePos)
        for rocket in self.rocket:
            rocket.bouge(None)

    def display(self):
        self.fond.afficher(self.win)
        self.player.afficher(self.win)
        for rocket in self.rocket:
            rocket.afficher(self.win)