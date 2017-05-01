from tank import Tank
from bullet import Bullet

from random import randint, choice

class Tile(object):
  grid = 0
  images = 0
  def __init__(self):
    self.name = ['all']
    self.permitCollisions = [Tank,Bullet]
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

class Flower:
  grid = 0
  gui = 0
  images = 0
  def __init__(self,x,y):
    self.size_rescale = (0.5,0.5)
    self.texture = choice(['flower1','flower2'])
    self.x = x
    self.y = y

  def render(self):
    self.gui.Image(self.images.getImage(self.texture),self.x,self.y,int(self.grid.scale*self.size_rescale[0]),int(self.grid.scale*self.size_rescale[1]))
