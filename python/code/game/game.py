import pygame,sys,Entities
pygame.init()
clock = pygame.time.Clock()

scrn = pygame.display.set_mode((800,600))

def Draw():
    pygame.draw.rect(scrn,(255,255,255),(380,270,40,60))


stop = False
guy=Entities.Player(380,270,100)
while not stop:
    scrn.fill((0,0,0))
    guy.draw(scrn)
    pygame.display.flip()
    clock.tick(60)
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            stop = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                guy.move("up",True)
            if event.key == pygame.K_DOWN:
                guy.move("down",True)
            if event.key == pygame.K_LEFT:
                guy.move("left",True)
            if event.key == pygame.K_RIGHT:
                guy.move("right",True)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                guy.move("up",False)
            if event.key == pygame.K_DOWN:
                guy.move("down",False)
            if event.key == pygame.K_LEFT:
                guy.move("left",False)
            if event.key == pygame.K_RIGHT:
                guy.move("right",False)
pygame.quit()
sys.exit()
