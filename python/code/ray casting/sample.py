import pygame as pyg
import sys

grid = ["11111111",
        "10100001",
        "10100001",
        "10100001",
        "10100001",
        "10000101",
        "10000001",
        "11111111"
    ]
px,py = 400,300
scrn = pyg.display.set_mode((800,600))

def draw():
    x = -(600//8)
    for row in grid:
        x+=(600//8)
        y = -(600//8)
        for col in grid:
            y+=(600//8)
            if col == "1":
                pyg.draw.rect(scrn,(255,255,255),(x,y,(600//8),(600//8)))
            else:
                pyg.draw.rect(scrn,(0,0,0),(x,y,(600//8),(600//8)))
    char = pyg.draw.rect(scrn,(255,255,0),(px,py,10,10))

stop = False
while not stop:
    scrn.fill((100,100,100))
    draw()
    pyg.display.update()
    for event in pyg.event.get():
        keys = pyg.key.get_pressed()
        if event.type == pyg.QUIT:
            stop = True
        if keys[pyg.K_w]:
            py -=5
        if keys[pyg.K_a]:
            px -=5
        if keys[pyg.K_s]:
            py +=5
        if keys[pyg.K_d]:
            px +=5
                
pyg.quit()
sys.exit()
