import pygame

from .Asset import AssetMoving


class Rocket(AssetMoving):
    def __init__(self, event, x, y):
        angle = pygame.math.Vector2(event[0] - x, event[1] - y).angle_to((0, -1))
        image = pygame.image.load("images/rocket.png").convert_alpha()
        image = pygame.transform.smoothscale(image, (20, 25))
        image = pygame.transform.rotate(image, angle)
        rect = image.get_rect()
        rect.center = (x, y)
        self.dy, self.dx = self.calculDeltaXY(angle)
        super().__init__(image, rect)


    def bouge(self, event):
        self.rect.x += self.dx
        self.rect.y += self.dy
