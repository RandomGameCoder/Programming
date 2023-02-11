# -*- coding: utf-8 -*-
import pygame
pygame.init()
bside=cside=iside=pside="left"
scrn_wdth=800
scrn_hght=630
scrn=pygame.display.set_mode((scrn_wdth,scrn_hght))
blx=bly=inx=iny=pix=piy=clx=cly=pacx=pacy=0
bl_back=pi_back=in_back=cl_back=False
gridlist=[]
nodelist=[]
doornode=[]
default=[]
mazelayout=[
    "########################################",
    "#n-------n--------n##n--------n-------n#",
    "#-#######-########-##-########-#######-#",
    "#-#     #-#      #n--n#      #-#     #-#",
    "#-# #####-###### #-##-# ######-##### #-#",
    "#-###n---n----n# #-##-# #n----n---n###-#",
    "#n---n###o####-###-##-###-####-###n---n#",
    "#-###-###-####n---n##n---n####o###-###-#",
    "#-# #n---nn---n###n--n###n---nn---n# #-#",
    "#-# ######-##### #-##-# #####-###### #-#",
    "#-#      #-#     #-##-#     #-#      #-#",
    "#-########-#######-##-#######-########-#",
    "#n-n------n----n  sdds  --n--n--n---n-n#",
    "###-######-####-###~~#####-#####-###-###",
    "---n---n--n--n-n#diddcd###-#####-###n---",
    "###-###-#####-###p dd b#n-n--n--n---n###",
    "###-###-#####-##########-####-######-###",
    "#n-n---n-n---n----n--n--n----nn-----n-n#",
    "#-#######-########-##-########-#######-#",
    "#-#     #-#      #-##-#      #-#     #-#",
    "#-# #####-###### #-##-# ######-##### #-#",
    "#-###n---nn---n# #n--n# #n---nn---n###-#",
    "#n---n####o###-###-##-###-###-####n---n#",
    "#-###-####-###n---n##n---n###o####-###-#",
    "#-# #n----n---n###-##-###n---n----n# #-#",
    "#-# ######-##### #-##-# #####-###### #-#",
    "#-#      #-#     #n-Pn#     #-#      #-#",
    "#-########-#######-##-#######-########-#",
    "#n--------n-------n##n-------n--------n#",
    "########################################",
    ]
wall_list=[(-20,285),(-20,305),(800,285),(800,305)]
food_list=[]
palet_list=[]
door=[]
def turn(x,y,dest,side):
    surround=[(x,y-20),(x-20,y),(x+20,y),(x,y+20)]
    trulist=[]
    for loc in surround:
        if loc in wall_list:
            trulist.append(True)
        else:
            trulist.append(False)
    if dest[0]-x>=0 and dest[1]-y<=0:
        if not trulist[0] and side!="down":
            side="up"
        elif not trulist[2] and side!="left":
            side="right"
        elif not trulist[3] and side!="up":
            side="down"
        elif not trulist[1] and side!="right":
            side="left"
    elif dest[0]-x<=0 and dest[1]-y<=0:
        if not trulist[0] and side!="down":
            side="up"
        elif not trulist[1] and side!="right":
            side="left"
        elif not trulist[3] and side!="up":
            side="down"
        elif not trulist[2] and side!="left":
            side="right"
    elif dest[0]-x<=0 and dest[1]-y>=0:
        if not trulist[3] and side!="up":
            side="down"
        elif not trulist[1] and side!="right":
            side="left"
        elif not trulist[0] and side!="down":
            side="up"
        elif not trulist[2] and side!="left":
            side="right"
    else:
        if not trulist[3] and side!="up":
            side="down"
        elif not trulist[2] and side!="left":
            side="right"
        elif not trulist[0] and side!="down":
            side="up"
        elif not trulist[1] and side!="right":
            side="left"
    return side
def blinky(x,y,mode,eaten):
    blnky_img=pygame.image.load(r'images\ghosts\blinkyl.png')
    if mode=="fright":
        blnky_img=pygame.image.load(r"images\ghosts\frightened.png")
        if eaten:
            up=pygame.image.load("images\\ghosts\\eyeup.png")
            left=pygame.image.load("images\\ghosts\\eyeleft.png")
            if bside=="up":
                blnky_img=up
            elif bside=="left":
                blnky_img=left
            elif bside=="down":
                blnky_img= pygame.transform.rotate(up, 180)
                new_rect = blnky_img.get_rect(center = up.get_rect(topleft = (x,y)).center)
                x,y=new_rect.topleft
            elif bside=="right":
                blnky_img= pygame.transform.rotate(left, 180)
                new_rect = blnky_img.get_rect(center = left.get_rect(topleft = (x,y)).center)
                x,y=new_rect.topleft
            if bl_back:
                if bside=="left":
                    blnky_img=pygame.image.load(r'images\ghosts\blinkyl.png')
                elif bside=="right":
                    blnky_img=pygame.image.load(r'images\ghosts\blinkyr.png')
                elif bside=="up":
                    blnky_img=pygame.image.load(r'images\ghosts\blinkyu.png')
                elif bside=="down":
                    blnky_img=pygame.image.load(r'images\ghosts\blinkyd.png')
    else:
        if bside=="left":
            blnky_img=pygame.image.load(r'images\ghosts\blinkyl.png')
        elif bside=="right":
            blnky_img=pygame.image.load(r'images\ghosts\blinkyr.png')
        elif bside=="up":
            blnky_img=pygame.image.load(r'images\ghosts\blinkyu.png')
        elif bside=="down":
            blnky_img=pygame.image.load(r'images\ghosts\blinkyd.png')
    scrn.blit(blnky_img,(x,y))
def inky(x,y,mode,eaten):
    if mode=="fright":
        nky_img=pygame.image.load(r"images\ghosts\frightened.png")
        if eaten:
            up=pygame.image.load("images\\ghosts\\eyeup.png")
            left=pygame.image.load("images\\ghosts\\eyeleft.png")
            if iside=="up":
                nky_img=up
            elif iside=="left":
                nky_img=left
            elif iside=="down":
                nky_img= pygame.transform.rotate(up, 180)
                new_rect = nky_img.get_rect(center = up.get_rect(topleft = (x,y)).center)
                x,y=new_rect.topleft
            elif iside=="right":
                nky_img= pygame.transform.rotate(left, 180)
                new_rect = nky_img.get_rect(center = left.get_rect(topleft = (x,y)).center)
                x,y=new_rect.topleft
            if in_back:
                if iside=="left":
                    nky_img=pygame.image.load(r'images\ghosts\inkyl.png')
                elif iside=="right":
                    nky_img=pygame.image.load(r'images\ghosts\inkyr.png')
                elif iside=="up":
                    nky_img=pygame.image.load(r'images\ghosts\inkyu.png')
                elif iside=="down":
                    nky_img=pygame.image.load(r'images\ghosts\inkyd.png')
    else:
        if iside=="left":
            nky_img=pygame.image.load(r'images\ghosts\inkyl.png')
        elif iside=="right":
            nky_img=pygame.image.load(r'images\ghosts\inkyr.png')
        elif iside=="up":
            nky_img=pygame.image.load(r'images\ghosts\inkyu.png')
        elif iside=="down":
            nky_img=pygame.image.load(r'images\ghosts\inkyd.png')
    scrn.blit(nky_img,(x,y))
def pinky(x,y,mode,eaten):
    global ptop,pdwn,plft,prgt
    ptop=(x,y+10)
    pdwn=(x+10,y+20)
    plft=(x+10,y)
    prgt=(x+20,y+10)
    if mode=="fright":
        pnky_img=pygame.image.load(r"images\ghosts\frightened.png")
        if eaten:
            up=pygame.image.load("images\\ghosts\\eyeup.png")
            left=pygame.image.load("images\\ghosts\\eyeleft.png")
            if pside=="up":
                pnky_img=up
            elif pside=="left":
                pnky_img=left
            elif pside=="down":
                pnky_img= pygame.transform.rotate(up, 180)
                new_rect = pnky_img.get_rect(center = up.get_rect(topleft = (x,y)).center)
                x,y=new_rect.topleft
            elif pside=="right":
                pnky_img= pygame.transform.rotate(left, 180)
                new_rect = pnky_img.get_rect(center = left.get_rect(topleft = (x,y)).center)
                x,y=new_rect.topleft
            if pi_back:
                if pside=="left":
                    pnky_img=pygame.image.load(r'images\ghosts\pinkyl.png')
                elif pside=="right":
                    pnky_img=pygame.image.load(r'images\ghosts\pinkyr.png')
                elif pside=="up":
                    pnky_img=pygame.image.load(r'images\ghosts\pinkyu.png')
                elif pside=="down":
                    pnky_img=pygame.image.load(r'images\ghosts\pinkyd.png')
    else:
        if pside=="left":
            pnky_img=pygame.image.load(r'images\ghosts\pinkyl.png')
        elif pside=="right":
            pnky_img=pygame.image.load(r'images\ghosts\pinkyr.png')
        elif pside=="up":
            pnky_img=pygame.image.load(r'images\ghosts\pinkyu.png')
        elif pside=="down":
            pnky_img=pygame.image.load(r'images\ghosts\pinkyd.png')
    scrn.blit(pnky_img,(x,y))
def clyde(mode,eaten):
    global clx,cly
    if mode=="fright":
        clyd_img=pygame.image.load(r"images\ghosts\frightened.png")
        if eaten:
            up=pygame.image.load("images\\ghosts\\eyeup.png")
            left=pygame.image.load("images\\ghosts\\eyeleft.png")
            if cside=="up":
                clyd_img=up
            elif pside=="left":
                clyd_img=left
            elif pside=="down":
                clyd_img= pygame.transform.rotate(up, 180)
                new_rect = clyd_img.get_rect(center = up.get_rect(topleft = (clx,cly)).center)
                clx,cly=new_rect.topleft
            elif pside=="right":
                clyd_img= pygame.transform.rotate(left, 180)
                new_rect = clyd_img.get_rect(center = left.get_rect(topleft = (clx,cly)).center)
                clx,cly=new_rect.topleft
            if cl_back:
                if cside=="left":
                    clyd_img=pygame.image.load(r'images\ghosts\clydel.png')
                elif cside=="right":
                    clyd_img=pygame.image.load(r'images\ghosts\clyder.png')
                elif cside=="up":
                    clyd_img=pygame.image.load(r'images\ghosts\clydeu.png')
                else:
                    clyd_img=pygame.image.load(r'images\ghosts\clyded.png')
    else:
        if cside=="left":
            clyd_img=pygame.image.load(r'images\ghosts\clydel.png')
        elif cside=="right":
            clyd_img=pygame.image.load(r'images\ghosts\clyder.png')
        elif cside=="up":
            clyd_img=pygame.image.load(r'images\ghosts\clydeu.png')
        else:
            clyd_img=pygame.image.load(r'images\ghosts\clyded.png')
    scrn.blit(clyd_img,(clx,cly))
def bmove(x,y,m):
    global blx,bly
    locx=locy=0
    if m=="scatter":
        locx=760
        locy=35
    elif m=="chase":
        locx=x
        locy=y
    elif m=="fright":
        locx=380
        locy=255
        if blx==380 and bly==255:
            locx,locy=400,300
    if 320<blx<460 and 295<bly<375:
        locx=380
        locy=255
    return locx,locy
def pmove(x,y,m,side):
    global pix,piy
    if m=="scatter":
        locx=20
        locy=35
    elif m=="chase":
        if side=="left":
            locx=x-80
            locy=y
        elif side=="right":
            locx=x+80
            locy=y
        elif side=="up":
            locx=x
            locy=y-80
        elif side=="down":
            locx=x
            locy=y+80
    elif m=="fright":
        locx=380
        locy=255
        if pix==380 and piy==255:
            locx,locy=400,300
    return locx,locy
def imove(x,y,m,side):
    global inx,iny
    if m=="scatter":
        locx=760
        locy=585
    elif m=="chase":
        if side=="left":
            locx=(x-20)+((x-20)-blx)
            locy=y+(y-bly)
        elif side=="right":
            locx=(x+20)+((x+20)-blx)
            locy=y+(y-bly)
        elif side=="up":
            locx=x+(x-blx)
            locy=(y-20)+((y-20)-bly)
        elif side=="down":
            locx=x+(x-blx)
            locy=(y+20)+((y+20)-bly)
    elif m=="fright":
        locx=380
        locy=255
        if inx==380 and iny==255:
            locx,locy=380,275
    if 320<inx<460 and 295<iny<375:
        locx=380
        locy=275
    return locx,locy
def cmove(x,y,m):
    global clx,cly
    if 320<clx<460 and 295<cly<375:
        locx=380
        locy=255
    elif m=="scatter":
        locx=20
        locy=585
    elif m=="chase":
        if x-80<=clx<=x+80 and y-80<=cly<=y+80:
            locx=20
            locy=595
        else:
            locx=x
            locy=y
    elif m=="fright":
        locx=380
        locy=255
        if clx==380 and cly==255:
            locx,locy=400,300
    return locx,locy
def blmovt(x,y,spd,m,eaten):
    global blx,bly,bside,bl_back
    if m=="fright" and blx==380 and bly==275:
        bl_back=True
    if m!="fright":
        bl_back=False
    if bl_back:
        m="chase"
    if (blx,bly) in nodelist or (blx,bly) in doornode:
        lx,ly=bmove(x,y,m)
        bside=turn(blx,bly,(lx,ly),bside)
    if bside=="up":
        if m=="fright":
            xpls=0
            ypls=-1
            if eaten:
                xpls=0
                ypls=-10
        else:
            xpls=0
            ypls=-spd
    elif bside=="down":
        if m=="fright":
            xpls=0
            ypls=1
            if eaten:
                xpls=0
                ypls=10
        else:
            xpls=0
            ypls=spd
    elif bside=="left":
        if m=="fright":
            xpls=-1
            ypls=0
            if eaten:
                xpls=-10
                ypls=0
        else:
            xpls=-spd
            ypls=0
    else:
        if m=="fright":
            xpls=1
            ypls=0
            if eaten:
                xpls=10
                ypls=0
        else:
            xpls=spd
            ypls=0
    return xpls,ypls
def inmovt(x,y,spd,m,side,eaten):
    global inx,iny,iside,in_back
    if m=="fright" and inx==380 and iny==275:
        in_back=True
    if m!="fright":
        in_back=False
    if in_back:
        m="chase"
    if (inx,iny) in nodelist or (inx,iny) in doornode:
        lx,ly=imove(x,y,m,side)
        iside=turn(inx,iny,(lx,ly),iside)
    if iside=="up":
        if m=="fright":
            xpls=0
            ypls=-1
            if eaten:
                xpls=0
                ypls=-10
        else:
            xpls=0
            ypls=-spd
    elif iside=="down":
        if m=="fright":
            xpls=0
            ypls=1
            if eaten:
                xpls=0
                ypls=10
        else:
            xpls=0
            ypls=spd
    elif iside=="left":
        if m=="fright":
            xpls=-1
            ypls=0
            if eaten:
                xpls=-10
                ypls=0
        else:
            xpls=-spd
            ypls=0
    else:
        if m=="fright":
            xpls=1
            ypls=0
            if eaten:
                xpls=10
                ypls=0
        else:
            xpls=spd
            ypls=0
    return xpls,ypls
def pimovt(x,y,spd,m,side,eaten):
    global pix,piy,pside,pi_back
    if m=="fright" and pix==380 and piy==275:
        pi_back=True
    if m!="fright":
        pi_back=False
    if pi_back:
        m="chase"
    if (pix,piy) in nodelist or (pix,piy) in doornode:
        lx,ly=pmove(x,y,m,side)
        pside=turn(pix,piy,(lx,ly),pside)
    if pside=="up":
        if m=="fright":
            xpls=0
            ypls=-1
            if eaten:
                xpls=0
                ypls=-10
        else:
            xpls=0
            ypls=-spd
    elif pside=="down":
        if m=="fright":
            xpls=0
            ypls=1
            if eaten:
                xpls=0
                ypls=10
        else:
            xpls=0
            ypls=spd
    elif pside=="left":
        if m=="fright":
            xpls=-1
            ypls=0
            if eaten:
                xpls=-10
                ypls=0
        else:
            xpls=-spd
            ypls=0
    else:
        if m=="fright":
            xpls=1
            ypls=0
            if eaten:
                xpls=10
                ypls=0
        else:
            xpls=spd
            ypls=0
    return xpls,ypls
def clmovt(x,y,spd,m,eaten):
    global clx,cly,cside,cl_back
    if m=="fright" and clx==380 and cly==275:
        cl_back=True
    if m!="fright":
        cl_back=False
    if cl_back:
        m="chase"
    if (clx,cly) in nodelist or (clx,cly) in doornode:
        lx,ly=cmove(x,y,m)
        cside=turn(clx,cly,(lx,ly),cside)
    if cside=="up":
        if m=="fright":
            xpls=0
            ypls=-1
            if eaten:
                xpls=0
                ypls=-10
        else:
            xpls=0
            ypls=-spd
    elif cside=="down":
        if m=="fright":
            xpls=0
            ypls=1
            if eaten:
                xpls=0
                ypls=10
        else:
            xpls=0
            ypls=spd
    elif cside=="left":
        if m=="fright":
            xpls=-1
            ypls=0
            if eaten:
                xpls=-10
                ypls=0
        else:
            xpls=-spd
            ypls=0
    else:
        if m=="fright":
            xpls=1
            ypls=0
            if eaten:
                xpls=10
                ypls=0
        else:
            xpls=spd
            ypls=0
    return xpls,ypls
def grid():
    global blx,bly,inx,iny,pix,piy,clx,cly,pacx,pacy,gridlist
    x=-20
    y=-5
    for i in range(40):
        x+=20
        for j in range(30):
            y+=20
            gridlist.append((x,y))
            mazechar=mazelayout[j][i]
            if mazechar=="#":
                wall_list.append((x,y))
            elif mazechar=="-":
                food_list.append((x,y))
            elif mazechar=="o":
                palet_list.append((x,y))
            elif mazechar=="n":
                food_list.append((x,y))
                nodelist.append((x,y))
            elif mazechar=="s":
                nodelist.append((x,y))
            elif mazechar=="d":
                doornode.append((x,y))
            elif mazechar=="p":
                doornode.append((x,y))
                default.append((x,y))
                pix=x
                piy=y
            elif mazechar=="i":
                default.append((x,y))
                inx=x
                iny=y
            elif mazechar=="b":
                default.append((x,y))
                doornode.append((x,y))
                blx=x
                bly=y
            elif mazechar=="c":
                default.append((x,y))
                clx=x
                cly=y
            elif mazechar=="P":
                default.append((x,y))
                pacx=x
                pacy=y
            elif mazechar=="~":
                door.append((x,y))
        y=-5

