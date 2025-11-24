import pygame

from sources.Asset import Fond, Joueur, Rocket
from sources.Game import Game

WIDTH = 1024
HEIGHT = 768
pygame.init()
fenetre = pygame.display.set_mode((WIDTH, HEIGHT))

game = Game(Fond(), Joueur(WIDTH//2, HEIGHT//2), fenetre)

clock = pygame.time.Clock()
running = True
lastRocket = pygame.time.get_ticks()

# --- Boucle principale ---
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if pygame.time.get_ticks() - lastRocket > 100:
            lastRocket = pygame.time.get_ticks()
            game.addRocket(Rocket(pygame.mouse.get_pos(), WIDTH//2, HEIGHT//2))

    game.move(pygame.mouse.get_pos())

    game.display()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

