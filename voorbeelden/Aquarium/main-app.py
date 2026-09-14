# New python project "Aquarium"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

aquarium = pygame.image.load("images/aquarium-basic.png").convert_alpha()
fishOne = pygame.image.load("images/fishnr1.png").convert_alpha()
fishTwo = pygame.image.load("images/fishnr2.png").convert_alpha()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Doing a trick with mousebutton position to see what coordinates the actual aquarium is in between
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Left mouse button clicked at:", event.pos)

    screen.fill((255, 255, 230))
    screen.blit(aquarium, (335, 200))

    # Aquarium begins at around (375, 390), untill (940, 660)
    # Which is the space the fish can move in between
    screen.blit(fishOne, (600, 500))
    screen.blit(fishTwo, (500, 600))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()