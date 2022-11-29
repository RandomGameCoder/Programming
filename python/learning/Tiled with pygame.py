import pygame
pygame.init()

scrn = pygame.display.set_mode((1200,720))
q = False

while not q:
    scrn.fill('black')
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            q = True
            break

pygame.quit()
quit()