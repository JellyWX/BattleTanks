import time
import math

class Bullet:
  def __init__(self,gui,im,x,y,vec):
    ## Rendering data ##
    self.gui = gui
    self.images = im

    ## Subcritical data ##
    #self.grid

    ## Critical data ##
    self.x = x
    self.y = y
    self.vec = vec
    self.time = time.time()
    self.alive = True

    self.rotation = math.atan2(self.vec[0],self.vec[1])*180/math.pi

    print('new bullet at ' + str(self.x) + ' ' + str(self.y))

  def move(self):
    if time.time() - self.time < 5:
      self.x += self.vec[0]
      self.y += self.vec[1]
    else:
      self.alive = False

  def render(self):
    self.gui.Image(self.images['bullet'],self.x,self.y,16,16,self.rotation)
