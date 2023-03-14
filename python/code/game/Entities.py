import pygame

class Entity:
    def __init__(self,x,y,life):
        self.x,self.y = x,y
        self.life = life
        self.xvel,self.yvel = 0,0
        self.maxvel = 3
    def get_pos(self):
        return self.x,self.y
    def get_life(self):
        return self.life

class Player(Entity):
    def move(self,side,val):
        if side == "left":
            if val:
                self.xvel = -self.maxvel
            else:
                self.xvel = 0
        elif side == "right":
            if val:
                self.xvel = self.maxvel
            else:
                self.xvel = 0
        elif side == "up":
            if val:
                self.yvel = -self.maxvel
            else:
                self.yvel = 0
        elif side == "down":
            if val:
                self.yvel = self.maxvel
            else:
                self.yvel = 0
    def draw(self,scrn):
        pygame.draw.rect(scrn,(255,255,255),(self.x,self.y,40,60))
        self.x += self.xvel
        self.y += self.yvel
