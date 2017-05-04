from random import randint, choice
from BaseClass import BaseClass

class Tile(BaseClass):
  def __init__(self):
    self.name = ['all']
    self.permitCollisions = []
    self.texture = self.assign()
    self.size_rescale = (1,1)
    self.rotation = randint(0,359)

  def assign(self):
    return None

  def render(self):
    return self.images.getImage(self.texture)

class GrassTile(Tile):
  def assign(self):
    self.name.append('grass')
    return 'grass'

class RoadTile(Tile):
  def assign(self):
    self.name.append('road')
    return 'road'


class Flower(BaseClass):
  def __init__(self,x,y):
    self.permitCollisions = []
    self.size_rescale = (0.5,0.5)
    self.texture = choice(['flower1','flower2'])
    self.x = x
    self.y = y

  def render(self):
    size = [int(self.grid.scale*self.size_rescale[0]),int(self.grid.scale*self.size_rescale[1])]
    self.gui.Image(self.images.getImage(self.texture),self.x - size[0]/2,self.y - size[1]/2,size[0],size[1])
    self.gui.Rect(self.x,self.y,2,2)

class Crate(BaseClass):
  def __init__(self,x,y):
    self.permitCollisions = ['tank','bullet']
    self.size_rescale = (1,1.2)
    self.texture = 'crate_test'
    self.x = x
    self.y = y

  def render(self):
    size = [int(self.grid.scale*self.size_rescale[0]),int(self.grid.scale*self.size_rescale[1])]
    self.gui.Image(self.images.getImage(self.texture),self.x - size[0]/2,self.y - size[1]/2,size[0],size[1])
    self.gui.Color('FF0000')
    self.gui.Rect(self.x,self.y,2,2)
