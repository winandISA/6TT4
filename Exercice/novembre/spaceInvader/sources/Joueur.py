import pygame

from .Asset import AssetMoving


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
