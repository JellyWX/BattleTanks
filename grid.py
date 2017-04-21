from tile import *

class Grid:

  gui = 0
  def __init__(self,x,y,preset='empty'):
    Tile.grid = self

    self.size_x = x
    self.size_y = y

    self.scale = 64

    self.map = []
    if preset == 'empty':
      for i in range(self.size_y):
        self.map.append([])
        for j in range(self.size_x):
          self.map[i].append(GrassTile())

    self.contents = []

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
        Grid.gui.Image(self.map[i][j].render(),j*self.scale,i*self.scale,self.scale,self.scale)

    li_len = len(self.contents)
    for i in range(len(self.contents)):
      for j in self.contents[i-li_len]:
        if j.x < self.scale*self.size_x and j.y < self.scale*self.size_y:
          if j.x > 0 and j.y > 0:
            j.render()
