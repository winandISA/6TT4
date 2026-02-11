import pygame



from multiJoueur.client.classes.NetClient import NetClient

SERVER_IP = "127.0.0.1"
PORT = 5000

WIDTH, HEIGHT = 500, 300
STEP = 5  # déplacement par tick

# ----- Messages: JSON + longueur (4 octets) -----



# ----- Pygame -----

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame Multiplayer (2 carrés)")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    net = NetClient(SERVER_IP, PORT)
    print(f"Joueur {net.color} connecté")

    running = True
    while running and net.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        dx = dy = 0

        if keys[pygame.K_z]:
            dy -= STEP
        if keys[pygame.K_s]:
            dy += STEP
        if keys[pygame.K_q]:
            dx -= STEP
        if keys[pygame.K_d]:
            dx += STEP

        if dx != 0 or dy != 0:
            net.move(dx, dy)

        players = net.get_players()
        xR, yR = players["RED"]
        xB, yB = players["BLUE"]

        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, (255, 0, 0), (xR, yR, 30, 30))
        pygame.draw.rect(screen, (0, 0, 255), (xB, yB, 30, 30))

        txt = font.render(f"Joueur {net.color} connecté", True, (220, 220, 220))
        screen.blit(txt, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    net.close()
    pygame.quit()

if __name__ == "__main__":
    main()
