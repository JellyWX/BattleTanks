from tank import Tank
from bullet import Bullet

class Tile:
  grid = 0
  images = 0
  def __init__(self):
    self.permitCollisions = [Tank,Bullet]
    self.contents = []
    self.texture = self.assign()

  def assign(self):
    return None

  def render(self):
    return self.images.getImage(self.texture)

class GrassTile(Tile):
  def assign(self):
    return 'grass'
