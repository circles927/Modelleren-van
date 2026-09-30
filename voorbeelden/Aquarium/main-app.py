# New python project "Aquarium"
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

aquariumIMG = pygame.image.load("images/aquarium-basic.png").convert_alpha()
fishOneIMG = pygame.image.load("images/fishnr1.png").convert_alpha()
fishTwoIMG = pygame.image.load("images/fishnr2.png").convert_alpha()

class Aquarium:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.borders = 5
        self.waterHeight = 218
        self.waterWidth = 574
        self.aquaHeight = self.waterHeight + self.borders
        self.aquaWidth = self.waterWidth + (self.borders * 2)

    def whereToSwim(self, position, movement, size):
        # als de beoogde beweging x links van 
        positionX = position[0]
        positionY = position[1]

        movementX = movement[0]
        movementY = movement[1]

        sizeHeight = size[0]
        sizeWidth = size[1]

        if positionX + movementX < self.x + self.borders + 15:
            movementX = -movementX
        elif positionX + movementX + sizeWidth > self.x + 560:
            movementX = -movementX

        if positionY + movementY < self.y + 159:
            movementY = -movementY
        elif positionY + movementY + sizeHeight > self.y + 360:     
            movementY = -movementY

        return movementX, movementY

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

aquariumMain = Aquarium(aquariumIMG, 335, 200)
    

class Fish:
    def __init__(self, image, xy, widthHeight, maxSpeed):
        self.image = image
        self.x = xy[0]
        self.y = xy[1]
        self.width = widthHeight[0]
        self.height = widthHeight[1]
        self.maxSpeed = maxSpeed

    def move(self):
        dx = random.randint(-self.maxSpeed, self.maxSpeed)
        dy = random.randint(-self.maxSpeed, self.maxSpeed)

        position = (self.x, self.y)
        movement = (dx, dy)
        size = (self.width, self.height)

        dxFinal, dyFinal = aquariumMain.whereToSwim(position, movement, size)

        self.x += dxFinal
        self.y += dyFinal

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

# Sizes measured "by hand" in Aseprite
fish1 = Fish(fishOneIMG, (600, 500), (36, 34), 10)
fish2 = Fish(fishTwoIMG, (500, 600), (52, 23), 10)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Doing a trick with mousebutton position to see what coordinates the actual aquarium is in between
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Left mouse button clicked at:", event.pos)

    screen.fill((255, 255, 230))
    aquariumMain.draw(screen)

    # Aquarium begins at around (375, 390), untill (940, 660)
    # Which is the space the fish can move in between

    fish1.draw(screen)
    fish2.draw(screen)

    fish1.move()
    fish2.move()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()