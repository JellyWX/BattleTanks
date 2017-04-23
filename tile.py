from tank import Tank
from bullet import Bullet

from random import randint

class Tile:
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
