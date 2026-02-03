import pygame

from sources.Game import Game, FinDuJeu

WIDTH = 1024
HEIGHT = 768
pygame.init()
fenetre = pygame.display.set_mode((WIDTH, HEIGHT))
game = Game(fenetre)

clock = pygame.time.Clock()
running = True
lastRocket = pygame.time.get_ticks()
lastMeteor = pygame.time.get_ticks()

try:
    # --- Boucle principale ---
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if pygame.time.get_ticks() - lastRocket > 250:
                lastRocket = pygame.time.get_ticks()
                game.addRocket(pygame.mouse.get_pos())

        if pygame.time.get_ticks() - lastMeteor > 400:
            lastMeteor = pygame.time.get_ticks()
            game.addMeteor()

        game.move(pygame.mouse.get_pos())

        game.display()
        pygame.display.flip()
        clock.tick(60)
except FinDuJeu as e:
    print(e)
pygame.quit()

