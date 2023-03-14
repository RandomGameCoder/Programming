import pygame, sys

from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()
size = (400,400)
pygame.display.set_caption("Game")
scrn = pygame.display.set_mode(size,0,32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)
