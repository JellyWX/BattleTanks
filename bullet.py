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
    self.vec = vec
    self.time = time.time()
    self.alive = True
    self.speed = 6

    self.permitCollisions = []

    self.size_rescale = (0.5,0.5)

    self.rotation = math.atan2(self.vec[0],self.vec[1])*180/math.pi

    self.grid.addRenderingComponent(self,zprior=4)

  def move(self):
    if not self.grid.grabCollision(self.x,self.y,self,r=8) \
       and time.time() - self.time < 6 and self.alive:
      self.x += self.vec[0]*self.speed
      self.y += self.vec[1]*self.speed
    else:
      self.alive = False

  def render(self):
    if self.alive:
      self.gui.Image(self.images.getImage('bullet'),self.x-8,self.y-8,int(self.size_rescale[0]*self.grid.scale),int(self.size_rescale[1]*self.grid.scale),self.rotation+180)
