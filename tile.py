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
    return Tile.images.getImage(self.texture)

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
    self.size_rescale = (0.6,0.6)
    self.texture = choice(['flower1','flower2'])
    self.permitCollisions = ['tank']
    self.x = x
    self.y = y

  def render(self):
    size = [int(Flower.grid.scale*self.size_rescale[0]),int(Flower.grid.scale*self.size_rescale[1])]
    Flower.gui.Image(Flower.images.getImage(self.texture),self.x - size[0]/2,self.y - size[1]/2,size[0],size[1])
    if BaseClass.gui.debug:
      Flower.gui.Color('FF0000')
      Flower.gui.Rect(self.x,self.y,2,2)

  def CollisionManager(self,t):
    if t == 'tank':
      Flower.grid.deleteRenderingComponent(self)
      return False

class Crate(BaseClass):
  def __init__(self,x,y):
    self.size_rescale = (1,1.2)
    self.texture = 'crate_test'
    self.permitCollisions = ['tank','bullet']
    self.x = x
    self.y = y

  def render(self):
    size = [int(Crate.grid.scale*self.size_rescale[0]),int(Crate.grid.scale*self.size_rescale[1])]
    Crate.gui.Image(Crate.images.getImage(self.texture),self.x - size[0]/2,self.y - size[1]/2,size[0],size[1])
    if BaseClass.gui.debug:
      Crate.gui.Color('FF0000')
      Crate.gui.Rect(self.x,self.y,2,2)

  def CollisionManager(self,t):
    return True

class MiniCrate(Crate):
  def __init__(self,x,y):
    super().__init__(x,y)
    self.size_rescale = (0.5,0.6)

  def CollisionManager(self,t):
    if t == 'bullet':
      Crate.grid.deleteRenderingComponent(self)
    return True
