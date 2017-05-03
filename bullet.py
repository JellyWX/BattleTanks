import time
import math

class Bullet:

  gui = 0
  images = 0
  grid = 0
  def __init__(self,x,y,vec):

    ## Subcritical data ##
    #self.grid

    ## Critical data ##
    self.x = x
    self.y = y
    self.vec = vec
    self.time = time.time()
    self.alive = True

    self.permitCollisions = []

    self.rotation = math.atan2(self.vec[0],self.vec[1])*180/math.pi

    self.grid.addRenderingComponent(self,zprior=4)

  def move(self):
    if not self.grid.grabCollision(self.x,self.y,'bullet',r=8) \
       and time.time() - self.time < 6:
      self.x += self.vec[0]
      self.y += self.vec[1]
    else:
      self.alive = False

  def render(self):
    if self.alive:
      self.gui.Image(self.images.getImage('bullet'),self.x-8,self.y-8,int(0.5*self.grid.scale),int(0.5*self.grid.scale),self.rotation+180)
