from BaseClass import BaseClass

import time
import math

class Bullet(BaseClass):
  def __init__(self,x,y,vec):

    ## Subcritical data ##
    #self.grid

    ## Critical data ##
    self.x = x
    self.y = y
    self.vec = list(vec)
    self.time = time.time()
    self.alive = True
    self.speed = 0.2

    self.permitCollisions = []

    self.size_rescale = (0.5,0.5)

    self.rotation = math.atan2(self.vec[0],self.vec[1])*180/math.pi

    self.grid.addRenderingComponent(self,zprior=4)

  def move(self):
    x_add = self.vec[0]*self.speed*Bullet.grid.scale
    y_add = self.vec[1]*self.speed*Bullet.grid.scale

    if not self.grid.grabCollision(self.x + x_add,self.y + y_add,self,r=8) \
       and time.time() - self.time < 6 and self.alive:
      self.x += x_add
      self.y += y_add
    else:
      if self.grid.grabCollision(self.x + x_add,self.y,self,r=8,obj=True).bounce:
        self.vec[0] *= -1
      if self.grid.grabCollision(self.x,self.y + y_add,self,r=8,obj=True).bounce:
        self.vec[1] *= -1
      if self.grid.grabCollision(self.x + x_add,self.y + y_add,self,r=8,obj=True) == BaseClass:
        self.alive = False
    if time.time() - self.time > 6:
      self.alive = False

  def render(self):
    if self.alive:
      self.gui.Image(self.images.getImage('bullet'),self.x-8,self.y-8,int(self.size_rescale[0]*self.grid.scale),int(self.size_rescale[1]*self.grid.scale),self.rotation+180)
