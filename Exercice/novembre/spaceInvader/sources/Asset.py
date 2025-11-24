import math
from abc import ABC, abstractmethod
import pygame
class Asset(ABC):
    def __init__(self, image, rect):
        self.image = image
        self.rect = rect

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

class Joueur(AssetMoving):
    def __init__(self, x, y):
        image = pygame.image.load("images/fusee.png").convert_alpha()
        image = pygame.transform.smoothscale(image, (50, 70))
        rect = image.get_rect()
        rect.center = (x, y)
        self.origImage = image
        super().__init__(image, rect)

    def bouge(self, event):
        fusee_x, fusee_y = self.rect.center
        angle = pygame.math.Vector2(event[0] - fusee_x, event[1] - fusee_y).angle_to((0, -1))
        self.image = pygame.transform.rotate(self.origImage, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

class Rocket(AssetMoving):
    def __init__(self, event, x, y):
        angle = pygame.math.Vector2(event[0] - x, event[1] - y).angle_to((0, -1))
        image = pygame.image.load("images/rocket.png").convert_alpha()
        image = pygame.transform.smoothscale(image, (20, 25))
        image = pygame.transform.rotate(image, angle)
        rect = image.get_rect()
        rect.center = (x, y)
        angle_rad = math.radians(angle)

        # Calcul du déplacement
        self.dy = - 5 * math.cos(angle_rad)
        self.dx = - 5 * math.sin(angle_rad)
        super().__init__(image, rect)

    def bouge(self, event):
        self.rect.x += self.dx
        self.rect.y += self.dy