from bullet import Bullet

import time
import math

class Tank:

  gui = 0
  images = 0
  grid = 0

  def __init__(self,x,y,player=True):

    ## Subcritical data ##
    #self.map = grid
    self.bullets = []
    self.last_fire = time.time()

    ## Critical data ##
    self.x = x
    self.y = y
    self.vec = (0,0)

    self.rotation = 0
    self.turret_rotation = 0

    self.grid.addRenderingComponent(self,zprior=2)

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
    if self.collisions(round(vec[0]),round(vec[1])):
      if rot_diff < 10:
        self.x += round(vec[0])
        self.y += round(vec[1])
      elif rot_diff < 180:
        self.rotation += 10
      elif rot_diff > 180:
        self.rotation -= 10
      else:
        self.x += round(vec[0])
        self.y += round(vec[1])
    self.vec = vec

  def move_keys(self,direction=0):
    if round(self.goto_rotation,-1) == self.rotation and self.collisions(self.vec[0],self.vec[1]):
      if direction == 0:
        self.x -= self.vec[0]
        self.y -= self.vec[1]
      if direction == 1:
        self.x += self.vec[0]
        self.y += self.vec[1]

  def collisions(self,x_add,y_add):
    r_sq = 16*16
    for i in range(-16,16):
      x_val = self.x + i + x_add
      i_sq_val = math.sqrt(r_sq - (i*i))
      y_val = self.y + y_add

      if (self.grid.grabCollision(x_val, y_val + i_sq_val)
         or self.grid.grabCollision(x_val, y_val - i_sq_val)):
        return False
        break
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
    Tank.gui.Image(Tank.images.getImage('tank1'),self.x-24,self.y-24,48,48,self.rotation)
    Tank.gui.Image(Tank.images.getImage('turret1'),self.x-24,self.y-24,48,48,self.turret_rotation)

    r_sq = 16*16
    for i in range(-16,16):
      self.gui.Color('ff0000')
      self.gui.Rect(self.x + i,round(self.y + math.sqrt(r_sq - (i*i))),2,2)
      self.gui.Rect(self.x + i,round(self.y - math.sqrt(r_sq - (i*i))),2,2)
