from bullet import Bullet
from BaseClass import BaseClass


import time
import math

class Tank(BaseClass):
  def __init__(self,x,y,player=True):

    ## Subcritical data ##
    #self.map = grid
    self.bullets = []
    self.last_fire = time.time()

    ## Critical data ##
    self.x = x
    self.y = y
    self.vec = (0,0)
    self.speed = 3

    self.rotation = 0
    self.turret_rotation = 0

    self.permitCollisions = []

    self.grid.addRenderingComponent(self,zprior=5)

    self.size_rescale = (1.5,1.5)

    self.ai = not player

  def move_cursor(self,vec,rotation):
    self.goto_rotation = rotation

    if self.rotation > 360:
      self.rotation -= 360
    elif self.rotation < 0:
      self.rotation += 360
    rotation = round(rotation,-1)
    rot_diff = (rotation - self.rotation) % 360

    '## Credits to /u/swimmer91 on Reddit for help with the line above. Many thanks! ##'
    if rot_diff < 10:
      if self.collisions_x(vec[0]*self.speed):
        self.x += round(vec[0]*self.speed)
      if self.collisions_y(vec[1]*self.speed):
        self.y += round(vec[1]*self.speed)
    elif rot_diff < 180:
      self.rotation += 10
    elif rot_diff > 180:
      self.rotation -= 10
    else:
      if self.collisions_x(vec[0]*self.speed):
        self.x += round(vec[0]*self.speed)
      if self.collisions_y(vec[1]*self.speed):
        self.y += round(vec[1]*self.speed)
    self.vec = vec

  def move_keys(self,direction=0):
    if round(self.goto_rotation,-1) == self.rotation and self.collisions():
      if direction == 0:
        self.x -= self.vec[0]*self.speed
        self.y -= self.vec[1]*self.speed
      if direction == 1:
        self.x += self.vec[0]*self.speed
        self.y += self.vec[1]*self.speed

  def collisions_x(self,x_add):
    if self.grid.grabCollision(self.x+x_add,self.y,self,r=16):
      return False
    return True

  def collisions_y(self,y_add):
    if self.grid.grabCollision(self.x,self.y+y_add,self,r=16):
      return False
    return True

  def rotate_turret(self,rotation):
    self.turret_rotation = rotation

  def attack(self,vec):
    if  time.time() - self.last_fire > 1:
      if len(self.bullets) < 3:
        self.bullets.append(Bullet(self.x,self.y,vec))
        self.last_fire = time.time()
      else:
        for i in range(0,len(self.bullets)):
          if self.bullets[i].alive == False:
            self.bullets[i] = Bullet(self.x,self.y,vec)
            self.last_fire = time.time()
            break

  def render(self):
    Tank.gui.Image(Tank.images.getImage('tank1'),self.x-24,self.y-24,int(self.size_rescale[0]*self.grid.scale),int(self.size_rescale[1]*self.grid.scale),self.rotation)
    Tank.gui.Image(Tank.images.getImage('turret1'),self.x-24,self.y-24,int(self.size_rescale[0]*self.grid.scale),int(self.size_rescale[1]*self.grid.scale),self.turret_rotation)
    if Tank.gui.debug:
      r_sq = 16*16
      for i in range(-16,16):
        x_val = self.x + i
        i_sq_val = math.sqrt(r_sq - (i*i))
        y_val = [self.y + i_sq_val,self.y - i_sq_val]
        x_val = round(x_val)
        y_val[0] = round(y_val[0])
        y_val[1] = round(y_val[1])
        Tank.gui.Color('FF0000')
        Tank.gui.Rect(x_val,y_val[0],2,2)
        Tank.gui.Rect(x_val,y_val[1],2,2)
