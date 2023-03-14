# -*- coding: utf-8 -*-
import pygame,ghosts,time
pygame.init()
chomp=pygame.mixer.Sound("sounds\\chomp1.wav")
introd=pygame.mixer.Sound("sounds\\intro.wav")
pygame.mixer.music.load("sounds\\bgm.wav")
dead=pygame.mixer.Sound("sounds\\death.wav")
blck=(0,0,0)
white=(255,255,255)
green=(0,200,0)
red=(200,0,0)
brightgreen=(0,255,0)
brightred=(255,0,0)
yellow=(255,255,0)
pygame.display.set_caption("PAC-MAN")
icon=pygame.image.load(r'images\pac-man\open.png')
pygame.display.set_icon(icon)
clock=pygame.time.Clock()
l=1
xpls=ypls=0
side="left"
spd=2.5
x=ghosts.pacx
y=ghosts.pacy
life=0
bxpls=cxpls=pxpls=ixpls=bypls=cypls=pypls=iypls=0
gspd=2.5
m="scatter"
modchng=0
paletless=False
nextcommand=""
score=0
foodlen=0
winner=False
loser=False
ghostlist=[]
fright_timer=0
beaten=ceaten=peaten=ieaten=False
combo=0
def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)
def drawdeath():
    global life
    lifelist=((1,617),(13,617),(26,617))
    wall=pygame.image.load("images\\wall.png")
    palet=pygame.image.load("images\\palet.png")
    door=pygame.image.load("images\\door.png")
    power_palet=pygame.image.load("images\\power_palet.png")
    lifeimg=pygame.image.load("images\\life.png")
    for loc in ghosts.wall_list:
        ghosts.scrn.blit(wall,loc)
    for loc in ghosts.food_list:
        ghosts.scrn.blit(palet,loc)
    for loc in ghosts.palet_list:
        ghosts.scrn.blit(power_palet,loc)
    for loc in ghosts.door:
        ghosts.scrn.blit(door,loc)
    for i in range(life):
        ghosts.scrn.blit(lifeimg,lifelist[i])
def death():
    global side
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
        angle=0
        if side=="left":
            angle=180
        elif side=="up":
            angle=90
        elif side=="down":
            angle=-90
        pygame.mixer.Sound.play(dead)
        images=["open","open2","open3","open4","glow","glow2","glow3","finish"]
        for image in images:
            ghosts.scrn.fill(blck)
            drawdeath()
            pac_man=pygame.image.load("images\\pac-man\\"+image+".png")
            blitRotateCenter(ghosts.scrn,pac_man,(x,y),angle)
            pygame.display.flip()
            time.sleep(0.2)
        break
def crash():
    global x,y,life,side,m,beaten,ceaten,peaten,ieaten
    ghostslist=[(ghosts.blx,ghosts.bly),(ghosts.clx,ghosts.cly),(ghosts.inx,ghosts.iny),(ghosts.pix,ghosts.piy)]
    for ghost in ghostslist:
        gx,gy=ghost
        if gx==x or gy==y:
            if x-20<gx<x+20 and y-20<gy<y+20 and m!="fright":
                death()
                life-=1
                beaten=ceaten=peaten=ieaten=False
                x,y=ghosts.default[2]
                side=ghosts.bside=ghosts.cside=ghosts.iside=ghosts.pside="left"
                ghosts.blx,ghosts.bly=ghosts.default[4]
                ghosts.clx,ghosts.cly=ghosts.default[3]
                ghosts.inx,ghosts.iny=ghosts.default[1]
                ghosts.pix,ghosts.piy=ghosts.default[0]
def turn():
    global side,nextcommand,x,y
    if (x,y) in ghosts.nodelist:
        surround=[(x,y-20),(x-20,y),(x+20,y),(x,y+20)]
        trulist=[]
        for loc in surround:
            if loc in ghosts.wall_list or loc in ghosts.door:
                trulist.append(True)
            else:
                trulist.append(False)
        if nextcommand=="right":
            if not trulist[2]:
                side=nextcommand
                nextcommand=""
        elif nextcommand=="left":
            if not trulist[1]:
                side=nextcommand
                nextcommand=""
        elif nextcommand=="up":
            if not trulist[0]:
                side=nextcommand
                nextcommand=""
        elif nextcommand=="down":
            if not trulist[3]:
                side=nextcommand
                nextcommand=""
    if side=="left" or side=="right":
        if nextcommand=="left" or nextcommand=="right":
            side=nextcommand
    if side=="up" or side=="down":
        if nextcommand=="up" or nextcommand=="down":
            side=nextcommand
def mode():
    global m,modchng,paletless,fright_timer,beaten,ceaten,peaten,ieaten
    if paletless:
        m="fright"
        fright_timer=time.time()
        paletless=False
    if m=="fright":
        now=time.time()
        if now-fright_timer>10:
            beaten=ceaten=peaten=ieaten=False
            m="chase"
def is_winner():
    global winner,score
    file=open("pac.sav","a+")
    file.write(str(score))
    file.close()
    while True:
        ghosts.scrn.fill(blck)
        disp_message("Congradulations!!!", (ghosts.scrn_wdth//2,180),50,typ="centre")
        disp_message("You  are  a  winner", (ghosts.scrn_wdth//2,210), 50,typ="centre")
        disp_message("Your  score:  "+score,(ghosts.scrn_wdth//2,240),20,typ="centre")
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if 350>mouse[0]>250 and 500>mouse[1]>450:
            pygame.draw.rect(ghosts.scrn,brightgreen,(246,446,108,58))
            if click[0]==1:
                winner=False
                game_loop()
        else:
            pygame.draw.rect(ghosts.scrn,green,(250,450,100,50))
        if 550>mouse[0]>450 and 500>mouse[1]>450:
            pygame.draw.rect(ghosts.scrn,brightred,(446,446,108,58))
            if click[0]==1:
                pygame.quit()
                break
        else:
            pygame.draw.rect(ghosts.scrn,red,(450,450,100,50))
        disp_message("REPLAY", (300,475), 30,typ="centre")
        disp_message("QUIT", (500,475), 30,typ="centre")
        pygame.display.update()
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ghosts.scrn.fill(blck)
                pygame.quit()
def is_loser():
    global loser,score
    file=open("pac.sav","a+")
    file.write(str(score))
    file.close()
    while True:
        ghosts.scrn.fill(blck)
        disp_message("Do not Worry!!!", (ghosts.scrn_wdth//2,180),50,typ="centre")
        disp_message("Nobody Is Born As An Epic Gamer", (ghosts.scrn_wdth//2,210), 50,typ="centre")
        disp_message("Your  score:  "+score,(ghosts.scrn_wdth//2,240),20,typ="centre")
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if 350>mouse[0]>250 and 500>mouse[1]>450:
            pygame.draw.rect(ghosts.scrn,brightgreen,(246,446,108,58))
            if click[0]==1:
                loser=False
                game_loop()
        else:
            pygame.draw.rect(ghosts.scrn,green,(250,450,100,50))
        if 550>mouse[0]>450 and 500>mouse[1]>450:
            pygame.draw.rect(ghosts.scrn,brightred,(446,446,108,58))
            if click[0]==1:
                pygame.quit()
                break
        else:
            pygame.draw.rect(ghosts.scrn,red,(450,450,100,50))
        disp_message("RETRY", (300,475), 30,typ="centre")
        disp_message("QUIT", (500,475), 30,typ="centre")
        pygame.display.update()
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ghosts.scrn.fill(blck)
                pygame.quit()
def text_objects(text,font,color=white):
    surface=font.render(text,True,color)
    return surface,surface.get_rect()
def disp_message(text,pos,size,typ="side"):
    font=pygame.font.Font("fonts\\arcade.ttf",size)
    textsurf,textrect=text_objects(text,font)
    if typ=="centre":
        textrect.center=pos
    else:
        textrect=pos
    ghosts.scrn.blit(textsurf,textrect)
def Score():
    global score,foodlen
    if foodlen!=len(ghosts.food_list):
        score+=10
        foodlen=len(ghosts.food_list)
    text="Score  "+str(score)
    disp_message(text, (0,0),15)
def drawmaze():
    global life,beaten
    lifelist=((1,617),(13,617),(26,617))
    wall=pygame.image.load("images\\wall.png")
    palet=pygame.image.load("images\\palet.png")
    door=pygame.image.load("images\\door.png")
    power_palet=pygame.image.load("images\\power_palet.png")
    lifeimg=pygame.image.load("images\\life.png")
    for loc in ghosts.wall_list:
        ghosts.scrn.blit(wall,loc)
    for loc in ghosts.food_list:
        ghosts.scrn.blit(palet,loc)
    for loc in ghosts.palet_list:
        ghosts.scrn.blit(power_palet,loc)
    for loc in ghosts.door:
        ghosts.scrn.blit(door,loc)
    for i in range(life):
        ghosts.scrn.blit(lifeimg,lifelist[i])
    disppacman(x, y)
    ghosts.blinky(ghosts.blx,ghosts.bly,m,beaten)
    ghosts.inky(ghosts.inx,ghosts.iny,m,ieaten)
    ghosts.pinky(ghosts.pix,ghosts.piy,m,peaten)
    ghosts.clyde(m,ceaten)
def disppacman(x,y):
    global l,side
    pac_open=pygame.image.load(r'images\pac-man\open.png')
    pac_closed=pygame.image.load(r'images\pac-man\closed.png')
    if l==31:
        l=1
    if l<=15:
        if side=="right":
            blitRotateCenter(ghosts.scrn,pac_open,(x,y),0)
        elif side=="left":
            blitRotateCenter(ghosts.scrn,pac_open,(x,y),180)
        elif side=="up":
            blitRotateCenter(ghosts.scrn,pac_open,(x,y),90)
        elif side=="down":
            blitRotateCenter(ghosts.scrn,pac_open,(x,y),-90)
    else:
        blitRotateCenter(ghosts.scrn,pac_closed,(x,y),0)
def play():
    global combo,ceaten,ieaten,peaten,beaten,ghostlist,side,xpls,ypls,spd,x,y,m,bxpls,cxpls,pxpls,ixpls,bypls,cypls,pypls,iypls,paletless
    turn()
    crash()
    if side=="right":
        if (x+20,y) in ghosts.wall_list:
            xpls=0
            ypls=0
        else:
            xpls=spd
            ypls=0
    elif side=="left":
        if (x-20,y) in ghosts.wall_list:
            xpls=0
            ypls=0
        else:
            xpls=-spd
            ypls=0
    elif side=="up":
        if (x,y-20) in ghosts.wall_list:
            xpls=0
            ypls=0
        else:
            ypls=-spd
            xpls=0
    elif side=="down":
        if (x,y+20) in ghosts.wall_list:
            xpls=0
            ypls=0
        else:
            ypls=spd
            xpls=0
    if x==-20 and side=="left":
        x=800
    elif x==800 and side=="right":
        x=-20
    if ghosts.blx==-20 and ghosts.bside=="left":
        ghosts.blx=800
    elif ghosts.blx==800 and ghosts.bside=="right":
        ghosts.blx=-20
    if ghosts.clx==-20 and ghosts.cside=="left":
        ghosts.clx=800
    elif ghosts.clx==800 and ghosts.cside=="right":
        ghosts.clx=-20
    if ghosts.pix==-20 and ghosts.pside=="left":
        ghosts.pix=800
    elif ghosts.pix==800 and ghosts.pside=="right":
        ghosts.pix=-20
    if ghosts.inx==-20 and ghosts.iside=="left":
        ghosts.inx=800
    elif ghosts.inx==800 and ghosts.iside=="right":
        ghosts.inx=-20
    if x<ghosts.blx+10<x+20 and y<ghosts.bly+10<y+20:
        combo+=100
        beaten=True
        disp_message(str(combo),(ghosts.blx,ghosts.bly),10)
    if x<ghosts.clx+10<x+20 and y<ghosts.cly+10<y+20:
        ceaten=True
    if x<ghosts.inx+10<x+20 and y<ghosts.iny+10<y+20:
        ieaten=True
    if x<ghosts.pix+10<x+20 and y<ghosts.piy+10<y+20:
        peaten=True
    if (ghosts.blx,ghosts.bly) in ghosts.gridlist:
        bxpls,bypls=ghosts.blmovt(x, y, gspd, m,beaten)
    if (ghosts.clx,ghosts.cly) in ghosts.gridlist:
        cxpls,cypls=ghosts.clmovt(x, y, gspd, m,ceaten)
    if (ghosts.pix,ghosts.piy) in ghosts.gridlist:
        pxpls,pypls=ghosts.pimovt(x, y, gspd, m,side,peaten)
    if (ghosts.inx,ghosts.iny) in ghosts.gridlist:
        ixpls,iypls=ghosts.inmovt(x, y, gspd, m,side,ieaten)
    if (ghosts.blx,ghosts.bly)==(400,300):
        beaten=False
    for food in ghosts.food_list:
        fx,fy=food
        if x<fx+10<x+20 and y<fy+10<y+20:
            #pygame.mixer.Sound.stop(chomp)
            pygame.mixer.Sound.play(chomp)
            ghosts.food_list.remove(food)
    for palet in ghosts.palet_list:
        px,py=palet
        if x<px+10<x+20 and y<py+10<y+20:
            ghosts.palet_list.remove(palet)
            paletless=True
    x+=xpls
    y+=ypls
    ghosts.blx+=bxpls
    ghosts.bly+=bypls
    ghosts.clx+=cxpls
    ghosts.cly+=cypls
    ghosts.pix+=pxpls
    ghosts.piy+=pypls
    ghosts.inx+=ixpls
    ghosts.iny+=iypls
def start():
    global yellow
    strt=True
    while strt:
        ghosts.scrn.fill(blck)
        text="pac]man"
        font=pygame.font.Font("fonts\\pac.ttf",110)
        textsurf,textrect=text_objects(text,font,color=yellow)
        textrect.center=(400,100)
        ghosts.scrn.blit(textsurf,textrect)
        text="123456789"
        textsurf,textrect=text_objects(text,font,color=yellow)
        textrect.center=(400,250)
        ghosts.scrn.blit(textsurf,textrect)
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if 450>mouse[0]>350 and 400>mouse[1]>350:
            pygame.draw.rect(ghosts.scrn,brightgreen,(346,346,108,58))
            if click[0]==1:
                strt=False
                ghosts.scrn.fill(blck)
                game_loop()
                break
        else:
            pygame.draw.rect(ghosts.scrn,green,(350,350,100,50))
        if 450>mouse[0]>350 and 470>mouse[1]>420:
            pygame.draw.rect(ghosts.scrn,brightred,(346,416,108,58))
            if click[0]==1:
                strt=False
                ghosts.scrn.fill(blck)
                pygame.quit()
                break
        else:
            pygame.draw.rect(ghosts.scrn,red,(350,420,100,50))
        disp_message("PLAY", (400,375), 30,typ="centre")
        disp_message("QUIT", (400,445), 30,typ="centre")
        pygame.display.update()
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                strt=False
                pygame.quit()

def game_loop():
    global l,xpls,ypls,x,y,life,modchng,m,nextcommand,side,winner,loser
    life=3
    ghosts.grid()
    stop=False
    intro=True
    x,y=ghosts.default[2]
    side=ghosts.bside=ghosts.cside=ghosts.iside=ghosts.pside="left"
    ghosts.blx,ghosts.bly=ghosts.default[4]
    ghosts.clx,ghosts.cly=ghosts.default[3]
    ghosts.inx,ghosts.iny=ghosts.default[1]
    ghosts.pix,ghosts.piy=ghosts.default[0]
    while not stop:
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop=True
            pygame.mixer.Sound.play(introd)
            ghosts.scrn.fill(blck)
            drawmaze()
            disp_message("ready", (400,265), 15,typ="centre")
            pygame.display.flip()
            time.sleep(3)
            ghosts.scrn.fill(blck)
            drawmaze()
            disp_message("start", (400,265), 15,typ="centre")
            pygame.display.flip()
            time.sleep(1.5)
            intro=False
        #pygame.mixer.music.play()
        l+=1
        modchng+=1
        mode()
        if ghosts.food_list==[] and ghosts.palet_list==[]:
            winner=True
            break
        if life==0:
            loser=True
            break
        ghosts.scrn.fill(blck)
        if not winner and not loser:
            drawmaze()
            Score()
            play()
        pygame.display.flip()
        clock.tick(30)
        pressed=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop=True
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_F4:
                    if pressed[pygame.K_LALT]:
                        stop=True
                        pygame.quit()
                if event.key == pygame.K_LEFT:
                    if xpls==0 and ypls==0:
                        side="left"
                    else:
                        nextcommand="left"
                elif event.key == pygame.K_RIGHT:
                    if xpls==0 and ypls==0:
                        side="right"
                    else:
                        nextcommand="right"
                elif event.key == pygame.K_UP:
                    if xpls==0 and ypls==0:
                        side="up"
                    else:
                        nextcommand="up"
                elif event.key == pygame.K_DOWN:
                    if xpls==0 and ypls==0:
                        side="down"
                    else:
                        nextcommand="down"
    if winner:
        is_winner()
    if loser:
        is_loser()
start()
pygame.quit()

