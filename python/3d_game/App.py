import ursina as ur
import math

App = ur.Ursina()

def menuscreen():
    pass

def pause():
    if ur.application.paused:
        ur.application.resume()
    else:
        ur.application.pause()

player = ur.Entity(model = "cube",
color = ur.color.blue,
rotation_y = -90,
texture = 'white_cube',
collider = 'box')

camera = ur.Entity(model = "cube")
camera.visible = False
camera.eternal = True

cube = ur.Entity(model = "cube",
color = ur.color.red,
position = (2,1,1),
texture = 'white_cube',
collider = 'box')

floor = ur.Entity(model = "plane",
scale = (100,0,100),
position = (0,-5,0),
collider = 'mesh')

menu = ur.Button(text = "menu",
color = ur.color.azure,
scale = (.08,.05),
position = (-0.83,0.45))
menu.on_click = pause

ur.camera.parent = camera
#ur.camera.y += 0.5

def gravity(obj):
    hit_info = obj.intersects()
    if hit_info.hit:
        dy = 0
    else:
        dy = .08
    obj.y -= dy

yvel = -2
jumped = False
ur.mouse.locked = True

def jump():
    global yvel,jumped
    yvel = 7
    jumped = True

def camera_movement():
    current = ur.mouse.position
    camera.rotation_y += current[0]*15
    camera.rotation_x -= current[1]*15

def control():
    global yvel,jumped
    
    front = camera.forward
    left = camera.left
    plfr = player.forward
    #movement in horizontal plane
    if ur.held_keys['w']:
        player.x += front[0]*ur.time.dt*10
        player.z += front[2]*ur.time.dt*10
        cos = (plfr[0]*front[0] + plfr[2]*front[2])/(math.sqrt(plfr[0]**2 + plfr[2]**2)*math.sqrt(front[0]**2 + front[2]**2))
        player.rotation_y += (math.acos(cos)-(math.pi/2))* 5
    if ur.held_keys['s']:
        player.x -= front[0]*ur.time.dt*10
        player.z -= front[2]*ur.time.dt*10
        cos = (plfr[0]*(-front[0]) + plfr[2]*(-front[2]))/(math.sqrt(plfr[0]**2 + plfr[2]**2)*math.sqrt(front[0]**2 + front[2]**2))
        player.rotation_y += (math.acos(cos)-(math.pi/2))* 5
    if ur.held_keys['a']:
        player.x += left[0]*ur.time.dt*10
        player.z += left[2]*ur.time.dt*10
        cos1 = (plfr[0]*left[0] + plfr[2]*left[2])/(math.sqrt(plfr[0]**2 + plfr[2]**2)*math.sqrt(left[0]**2 + left[2]**2))
        cos = (plfr[0]*front[0] + plfr[2]*front[2])/(math.sqrt(plfr[0]**2 + plfr[2]**2)*math.sqrt(front[0]**2 + front[2]**2))
        player.rotation_y += (math.acos(cos1)-(math.pi/2))* 5
        camera.rotation_y -= (math.acos(cos)-(math.pi/2))*0.2
    if ur.held_keys['d']:
        player.x -= left[0]*ur.time.dt*10
        player.z -= left[2]*ur.time.dt*10
        cos1 = (plfr[0]*(-left[0]) + plfr[2]*(-left[2]))/(math.sqrt(plfr[0]**2 + plfr[2]**2)*math.sqrt(left[0]**2 + left[2]**2))
        cos = (plfr[0]*front[0] + plfr[2]*front[2])/(math.sqrt(plfr[0]**2 + plfr[2]**2)*math.sqrt(front[0]**2 + front[2]**2))
        player.rotation_y += (math.acos(cos1)-(math.pi/2))* 5
        camera.rotation_y -= (math.acos(cos)-(math.pi/2))*0.2
    
    if ur.held_keys['space'] and jumped == False:
        jump()
    player.y += yvel * ur.time.dt
    hit_info = player.intersects()
    if yvel != 0:
        if yvel < -6:
            yvel = -7
        else:
            yvel = yvel-(11*ur.time.dt)
        if hit_info.hit:
            yvel = 0
            jumped = False
    
    #turning function
    player.rotation_y -= ur.held_keys['1']*ur.time.dt * 100
    player.rotation_y += ur.held_keys['2']*ur.time.dt * 100

def update():
    control()
    camera_movement()
    camera.x,camera.y,camera.z = player.x,player.y+1,player.z
    #print(math.degrees(math.atan(player.forward[0]/player.forward[2])))
    #print(player.forward[0])

    

App.run()
