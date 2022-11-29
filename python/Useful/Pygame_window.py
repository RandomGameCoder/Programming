import pygame

pygame.init()

res = (800,600)

scrn = pygame.display.set_mode(res)

Quit = False

while not Quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Quit = True
            break
    pygame.display.flip()

pygame.quit()
