import random

from .Asset import Fond
from .Meteor import Meteor
from .Joueur import Joueur
from .Rocket import Rocket
import pygame

class Game():
    def __init__(self, win):
        self.fond = Fond()
        self.player = Joueur(win.get_width()//2, win.get_height()//2)
        self.rocket = []
        self.meteor = []
        self.win = win

    def addRocket(self, mouse):
        x, y = self.player.getRectXY()
        self.rocket.append(Rocket(mouse, x, y))

    def addMeteor(self):
        correctPosition = False
        x = 0
        y = 0
        while not correctPosition:
            x = random.randint(26, self.win.get_width() -26)
            y = random.randint(26, self.win.get_height() -26)
            if not (self.player.rect.x - 50 < x < self.player.rect.x + 50) and not (self.player.rect.y + 50 < y < self.player.rect.y + 50):
                correctPosition = True
        angle = random.randint(0, 360)
        self.meteor.append(Meteor(x, y, angle,[self.win.get_width(), self.win.get_height()]))

    def move(self, mousePos):
        self.player.bouge(mousePos)
        for rocket in self.rocket:
            rocket.bouge(None)
            if rocket.rect.x < 0 or rocket.rect.x > self.win.get_width() or rocket.rect.y < 0 or rocket.rect.y > self.win.get_height():
                self.rocket.remove(rocket)
        for meteor in self.meteor:
            meteor.bouge(None)
        self.__collision()

    def display(self):
        self.fond.afficher(self.win)
        self.player.afficher(self.win)
        for rocket in self.rocket:
            rocket.afficher(self.win)
        for meteor in self.meteor:
            meteor.afficher(self.win)

    def __collision(self):
        for meteor in self.meteor:
            if meteor.rect.colliderect(self.player.rect):
                raise FinDuJeu("Game over")
        for rocket in self.rocket:
            for meteor in self.meteor:
                if rocket.rect.colliderect(meteor.rect):
                    self.rocket.remove(rocket)
                    self.meteor.remove(meteor)

class FinDuJeu(Exception):
    pass