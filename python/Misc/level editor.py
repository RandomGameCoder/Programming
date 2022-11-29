from ursina import *

x,y =2,1

def update():
    global x,y
    if mouse.right:
        if x == 2 and y == 1:
            x,y = mouse.position[0],mouse.position[1]
            print(x,y)
        else:
            a,b = x,y
            x,y = mouse.position[0],mouse.position[1]
            camera.x += 2*(a-x)
            camera.y += 2*(b-y)
    else:
        x,y = 2,1

app = Ursina()

grid = Entity(model = Grid(100,100),scale =50)



app.run()
