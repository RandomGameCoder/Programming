import pygame
import time
import os
import random
pygame.font.init()

birds = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird1.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird2.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird3.png")))]
pipe = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png")))
base = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","base.png")))
bg = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bg.png")))
font=pygame.font.SysFont("comicsans",50)

class Bird:
      imgs = birds
      max_rotation = 25
      rot_vel = 20
      anim_time = 5
      def __init__(self,x,y):
            self.x = x
            self.y = y
            self.tilt = 0
            self.tick_count = 0
            self.vel = self.height = self.y
            self.img_count = 0
            self.img = self.imgs[0]
      def jump(self):
            self.vel = -10.5
            self.tick_count = 0
            self.height = self.y
      def move(self):
            self.tick_count += 1
            d=self.vel*self.tick_count + 1.5*self.tick_count**2
            if d >= 16:
                  d = 16
            if d<0:
                  d-=2
            self.y += d
            if d <0 or self.y<self.height+50:
                  if self.tilt<self.max_rotation:
                        self.tilt=self.max_rotation
            else:
                  if self.tilt>-90:
                        self.tilt-=self.rot_vel
      def draw(self,win):
            self.img_count+=1
            if self.img_count<self.anim_time:
                  self.img=self.imgs[0]
            elif self.img_count<self.anim_time*2:
                  self.img=self.imgs[1]
            elif self.img_count<self.anim_time*3:
                  self.img=self.imgs[2]
            elif self.img_count<self.anim_time*4:
                  self.img=self.imgs[1]
            elif self.img_count<self.anim_time*4+1:
                  self.img=self.imgs[0]
                  self.img_count=0
            if self.tilt<=-80:
                  self.img=self.imgs[1]
                  self.img_count=self.anim_time*2
            rotated_image = pygame.transform.rotate(self.img, self.tilt)
            new_rect = rotated_image.get_rect(center = self.img.get_rect(topleft = (self.x,self.y)).center)
            win.blit(rotated_image, new_rect.topleft)
      def get_mask(self):
            return pygame.mask.from_surface(self.img)
class Pipe:
      gap=200
      vel=5
      def __init__(self,x):
            self.x=x
            self.height=0
            self.top=0
            self.bottom=0
            self.pipe_top=pygame.transform.flip(pipe,False,True)
            self.pipe_bottom=pipe
            self.passed=False
            self.set_height()

      def set_height(self):
            self.height=random.randrange(50,450)
            self.top=self.height-self.pipe_top.get_height()
            self.bottom=self.height+self.gap
      def move(self):
            self.x-=self.vel
      def draw(self,win):
            win.blit(self.pipe_top,(self.x,self.top))
            win.blit(self.pipe_bottom,(self.x,self.bottom))
      def collide(self,bird):
            bird_mask=bird.get_mask()
            top_mask=pygame.mask.from_surface(self.pipe_top)
            bottom_mask=pygame.mask.from_surface(self.pipe_bottom)
            top_offset=(self.x-bird.x,self.top-round(bird.y))
            bottom_offset=(self.x-bird.x,self.bottom-round(bird.y))
            b_point=bird_mask.overlap(bottom_mask,bottom_offset)
            t_point=bird_mask.overlap(top_mask,top_offset)
            if t_point or b_point:
                  return True
            return False
class Base:
      VEL=5
      width=base.get_width()
      img=base
      def __init__(self,y):
            self.y=y
            self.x1=0
            self.x2=self.width
      def move(self):
            self.x1-=self.VEL
            self.x2-=self.VEL
            if self.x1+self.width<0:
                  self.x1=self.x2+self.width
            if self.x2+self.width<0:
                  self.x2=self.x1+self.width
      def draw(self,win):
            win.blit(self.img,(self.x1,self.y))
            win.blit(self.img,(self.x2,self.y))

      
def draw_win(win,bird,pipes,base,score):
      win.blit(bg,(0,-100))
      for pipe in pipes:
            pipe.draw(win)
      text=font.render("Score: "+str(score),1,(0,0,0))
      win.blit(text,(490-text.get_width(),10))
      base.draw(win)
      bird.draw(win)
      pygame.display.update()
      
def main():
      bird=Bird(230,350)
      b=Base(630)
      pipes=[Pipe(600)]
      win=pygame.display.set_mode((500,700))
      clock=pygame.time.Clock()
      score=0
      run=True
      while run:
            clock.tick(30)
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                      run=False
                  if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                              bird.jump()
            
            rem=[]
            add_pipe=False
            bird.move(10)
            for pipe in pipes:
                  if pipe.collide(bird):
                        pass
                  if pipe.x+pipe.pipe_top.get_width()<0:
                        rem.append(pipe)
                  if not pipe.passed and pipe.x<bird.x:
                        score+=1
                        pipe.passed=True
                        add_pipe=True
                  pipe.move()
            if add_pipe:
                  pipes.append(Pipe(600))
                  add_pipe=False
            for r in rem:
                  pipes.remove(r)
            b.move()
            draw_win(win,bird,pipes,b,score)
      pygame.quit()
      quit()
main()
