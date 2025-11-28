import random

from .Asset import AssetMoving
import pygame

class Meteor(AssetMoving):
    def __init__(self, x, y, angle, fondSize):
        image = pygame.image.load("images/meteor.png").convert_alpha()
        image = pygame.transform.smoothscale(image, (50, 50))
        image = pygame.transform.rotate(image, angle)
        rect = image.get_rect()
        rect.center = (x, y)
        self.dy, self.dx = self.calculDeltaXY(angle)
        self.fondSize = fondSize
        super().__init__(image, rect)



    def bouge(self, event):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.x < 5 or self.rect.x + 50 > self.fondSize[0] -5:
            self.dx = -self.dx
        if self.rect.y < 5 or self.rect.y + 50 > self.fondSize[1] -5:
            self.dy = -self.dy