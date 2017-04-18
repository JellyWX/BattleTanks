import time

class Bullet:
  def __init__(gui,im,x,y,rotation):
    ## Rendering data ##
    self.gui = gui
    self.images = im

    ## Subcritical data ##
    #self.grid
    self.rotation = rotation

    ## Critical data ##
    self.x = x
    self.y = y
    self.vec = vec
    self.time = time.time()
    self.alive = True

  def move(self):
    if time.time() - self.time < 8:
      self.x += self.vec[0]
      self.y += self.vec[1]
    else:
      self.alive = False

  def render(self):
    self.gui.Image(self.images['bullet'],5,5,self.x,self.y,self.rotation)
