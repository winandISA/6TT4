import math
from abc import ABC, abstractmethod
import pygame
class Asset(ABC):
    def __init__(self, image, rect):
        self.image = image
        self.rect = rect

    def getRectXY(self):
        return self.rect.center

    @abstractmethod
    def bouge(self, event):
        pass

    @abstractmethod
    def afficher(self, win):
        pass

class Fond(Asset):
    def __init__(self):
        image = pygame.image.load("images/fond.png").convert()
        super().__init__(image, image.get_rect())

    def bouge(self, event):
        pass

    def afficher(self, win):
        win.blit(self.image, (0, 0))

class AssetMoving(Asset):
    def __init__(self, image, rect):
        super().__init__(image, rect)


    def afficher(self, win):
        win.blit(self.image, self.rect.topleft)

    @staticmethod
    def calculDeltaXY(angle):
        angle_rad = math.radians(angle)
        # Calcul du déplacement
        return - 5 * math.cos(angle_rad) , - 5 * math.sin(angle_rad)



