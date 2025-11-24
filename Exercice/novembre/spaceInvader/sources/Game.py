from .Asset import *
import pygame

class Game():
    def __init__(self, win):
        self.fond = Fond()
        self.player = Joueur(win.get_width()//2, win.get_height()//2)
        self.rocket = []
        self.win = win

    def getFond(self):
        return self.fond

    def getPlayer(self):
        return self.player

    def addRocket(self, mouse):
        x, y = self.player.getRectXY()
        self.rocket.append(Rocket(mouse, x, y))

    def move(self, mousePos):
        self.player.bouge(mousePos)
        for rocket in self.rocket:
            rocket.bouge(None)

    def display(self):
        self.fond.afficher(self.win)
        self.player.afficher(self.win)
        for rocket in self.rocket:
            rocket.afficher(self.win)