from tile import Tile

class Grid:

  gui = 0
  images = 0
  def __init__(self,gui,images,x,y,preset='empty'):
    Tile.grid = self

    self.size_x = x
    self.size_y = y

    self.map = []
    if preset == 'empty':
      for i in range(size_y):
        self.map.append([])
        for j in size_x:
          self.map[i].append(Tile)
