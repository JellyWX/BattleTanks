from tank import Tank
from bullet import Bullet

from random import randint, choice

class Tile(object):
  grid = 0
  images = 0
  def __init__(self):
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
    return 'grass'

class RoadTile(Tile):
  def assign(self):
    return 'road'

class Flower:
  gui = 0
  images = 0
  def __init__(self,x,y):
    self.size_rescale = (0.1,0.1)
    self.texture = choice(['flower1','flower2'])
    self.x = x
    self.y = y

  def render(self):
    pass
