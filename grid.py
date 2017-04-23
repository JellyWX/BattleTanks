from tile import *

class Grid:

  gui = 0
  def __init__(self,x,y,preset='empty'):
    Tile.grid = self

    self.size_x = x
    self.size_y = y

    self.scale = 32

    self.map = []
    if preset == 'empty':
      for i in range(self.size_y):
        self.map.append([])
        for j in range(self.size_x):
          self.map[i].append(GrassTile())
    elif preset == 'park':
      for i in range(self.size_y):
        self.map.append([])
        for j in range(self.size_x):
          if j == 0 or j == self.size_y - 1:
            self.map[i].append(RoadTile())
          else:
            self.map[i].append(GrassTile())

    self.contents = []

  def grabCollision(self,x,y):
    x = round(x)
    y = round(y)
    if x <= 0 or y <= 0:
      return True
    if x >= self.size_x*self.scale or y >= self.size_y*self.scale:
      return True
    return False

  def addRenderingComponent(self,obj,zprior=0):
    try:
      self.contents[zprior].append(obj)
    except IndexError:
      for i in range(zprior+1):
        try:
          self.contents[i]
        except IndexError:
          self.contents.append([])
      self.contents[zprior].append(obj)

  def render(self):
    for i in range(len(self.map)):
      for j in range(len(self.map[i])):
        tile_at = self.map[i][j]
        Grid.gui.Image(tile_at.render(),j*self.scale,i*self.scale,self.scale*tile_at.size_rescale[0],self.scale*tile_at.size_rescale[1],tile_at.rotation)

    li_len = len(self.contents)
    for i in range(len(self.contents)):
      for j in self.contents[i-li_len]:
        if j.x < self.scale*self.size_x and j.y < self.scale*self.size_y:
          if j.x > 0 and j.y > 0:
            j.render()
