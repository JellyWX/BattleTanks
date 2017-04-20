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

  def render(self):
    for i in range(len(self.map)):
      for j in range(len(self.map[i])):
        Grid.gui.Image(self.map[i][j].render(),j*self.scale,i*self.scale,self.scale,self.scale)
