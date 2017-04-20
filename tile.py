from tank import Tank
from bullet import Bullet

class Tile:
  grid = 0
  images = 0
  def __init__(self):
    self.permitCollisions = [Tank,Bullet]
    self.texture = 
