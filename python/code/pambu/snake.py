import pygame
import random
pygame.init()

black=(0,0,0)
green=(0,240,0)
brightg=(0,255,0)
red=(240,0,0)
brightr=(255,0,0)
rgb=[255,0,0]
rgbval=1
snakecolor=[255,255,255]
width=800
height=600

snake=[(420,300),(410,300),(400,300)]
side="left"
score=0
food=(random.randint(0,80)*10,random.randint(0,58)*10+10)
clock=pygame.time.Clock()

#checks if food is in the position of the snake
while food in snake:
    food=(random.randint(0,80)*10,random.randint(0,58)*10+10)

#creates a surface to display the text
def text_objects(text,font,colour=(255,255,255)):
    surface=font.render(text,True,colour)
    return surface,surface.get_rect()

#renders the text onto the screen
def disp_message(text,pos,size,typ="side",color=(255,255,255)):
    font=pygame.font.Font("arcade.ttf",size)
    textsurf,textrect=text_objects(text,font,colour=color)
    if typ=="centre":
        textrect.center=pos
    else:
        textrect=pos
    scrn.blit(textsurf,textrect)

#the movement of the snake
def move():
    global snake
    snake.pop(0)
    if side == "left":
        x=[snake[-1][0]-10,snake[-1][1]]
        if x[0] == -10:
            x[0] = 790
    elif side == "right":
        x=[snake[-1][0]+10,snake[-1][1]]
        if x[0] == 800:
            x[0] = 0
    elif side == "up":
        x=[snake[-1][0],snake[-1][1]-10]
        if x[1] == 10:
            x[1] = 590
    elif side == "down":
        x=[snake[-1][0],snake[-1][1]+10]
        if x[1] == 600:
            x[1] = 0
    snake.append(tuple(x))

#checks if the snake has eaten the food
def eat():
    global snake, food, score, snakecolor
    if snake[-1] == food:
        l=[(snake[0][0]+(snake[0][0]-snake[1][0]),\
            snake[0][1]+(snake[0][1]-snake[1][1]))]
        l+=snake
        snake=l
        score+=20
        snakecolor=list(rgb)
        food=(random.randint(0,80)*10,random.randint(0,59)*10+10)
        while food in snake:
            food=(random.randint(0,80)*10,random.randint(0,59)*10+10)

#changes the colour values
def RGB():
    global rgb, rgbval
    if rgbval==1:
        rgb[0]-=5
        rgb[1]+=5
    elif rgbval==2:
        rgb[1]-=5
        rgb[2]+=5
    elif rgbval==3:
        rgb[2]-=5
        rgb[0]+=5
    if rgb[0]==255:
        rgbval=1
    elif rgb[1]==255:
        rgbval=2
    elif rgb[2]==255:
        rgbval=3

#checks if the snake has collided with itself
def collide():
    head=snake[-1]
    if head in snake[:-1]:
        return True
    else:
        return False
        
#draws the snake and food onto the screen
def draw():
    disp_message(str(score),(0,0),20)
    for i in snake:
        pygame.draw.rect(scrn,snakecolor,(i[0],i[1],9,9))
    pygame.draw.rect(scrn,rgb,(food[0]+2,food[1]+2,5,5))
    if side == "left" or side == "up":
        pygame.draw.rect(scrn,black,(snake[-1][0]+2,snake[-1][1]+2,2,2))
    elif side == "down":
        pygame.draw.rect(scrn,black,(snake[-1][0]+2,snake[-1][1]+5,2,2))
    elif side == "right":
        pygame.draw.rect(scrn,black,(snake[-1][0]+5,snake[-1][1]+2,2,2))

#displays the gameover screen
def gameover():
    while True:
        scrn.fill(black)
        disp_message("GAME OVER!!",(400,180),50,typ="centre")
        disp_message("Your Score:"+str(score),(400,300),20,typ="centre")
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if 350>mouse[0]>250 and 500>mouse[1]>450:
            pygame.draw.rect(scrn,brightg,(246,446,108,58))
            if click[0] == 1:
                game()
        else:
            pygame.draw.rect(scrn,green,(250,450,100,50))
        if 550>mouse[0]>450 and 500>mouse[1]>450:
            pygame.draw.rect(scrn,brightr,(446,446,108,58))
            if click[0] == 1:
                pygame.quit()
                break
        else:
            pygame.draw.rect(scrn,red,(450,450,100,50))
        disp_message("RETRY",(300,475),30,typ="centre")
        disp_message("QUIT",(500,475),30,typ="centre")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

#displays the starting screen
def strt():
    while True:
        scrn.fill(black)
        RGB()
        disp_message("SNAKE",(400,180),250,typ="centre",color=rgb)
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if 350>mouse[0]>250 and 500>mouse[1]>450:
            pygame.draw.rect(scrn,brightg,(246,446,108,58))
            if click[0] == 1:
                game()
        else:
            pygame.draw.rect(scrn,green,(250,450,100,50))
        if 550>mouse[0]>450 and 500>mouse[1]>450:
            pygame.draw.rect(scrn,brightr,(446,446,108,58))
            if click[0] == 1:
                pygame.quit()
                break
        else:
            pygame.draw.rect(scrn,red,(450,450,100,50))
        disp_message("PLAY",(300,475),30,typ="centre")
        disp_message("QUIT",(500,475),30,typ="centre")
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

#main game loop 
def game():
    global score, side, snake
    snake=[(420,300),(410,300),(400,300)]
    score=0
    while True:
        scrn.fill(black)
        if collide():
            gameover()
            break
        draw()
        eat()
        move()
        RGB()
        pygame.display.update()
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if side=="down":
                        continue
                    side="up"
                if event.key == pygame.K_DOWN:
                    if side=="up":
                        continue
                    side="down"
                if event.key == pygame.K_LEFT:
                    if side=="right":
                        continue
                    side="left"
                if event.key == pygame.K_RIGHT:
                    if side=="left":
                        continue
                    side="right"

#to check if the file is imported as a module
if __name__ == "__main__":
    
    #creates the main window
    scrn=pygame.display.set_mode((width,height))
    strt()
    quit()
