from tile import *
from tank import Tank
from random import randint
from BaseClass import BaseClass

import math

class Grid(BaseClass):
  def __init__(self,x,y):

    self.size_x = x
    self.size_y = y

    self.scale = 32

    self.map = []

    self.contents = []

    self.decorations = []

  def Draw(self,t='empty'):
    if t == 'empty':
      for i in range(self.size_y):
        self.map.append([])
        for j in range(self.size_x):
          self.map[i].append(GrassTile())
    elif t == 'park1':
      for i in range(self.size_y):
        self.map.append([])
        for j in range(self.size_x):
          if j == 0 or j == self.size_y - 1:
            self.map[i].append(RoadTile())
          else:
            self.map[i].append(GrassTile())
    elif t == 'park2':
      for i in range(self.size_y):
        self.map.append([])
        for j in range(self.size_x):
          if j == 0 or j == self.size_y - 1 or i == self.size_y // 2:
            self.map[i].append(RoadTile())
          else:
            self.map[i].append(GrassTile())
            
      self.Decorator(Flower,24,base_tile='grass',also_avoid=[Crate])
      self.Decorator(Crate,6,base_tile='road',z=6,also_avoid=[Tank])
      self.Decorator(MiniCrate,16,z=6,also_avoid=[Crate,Tank])
      self.Decorator(WeaponCrate,2,z=6,also_avoid=[Crate,MiniCrate,Flower,Tank])

  def grabCollision(self,x,y,t,r=16):
    r_sq = r*r
    for j in range(-r*2,r*2 + 1):
      i = j/2
      x_val = x + i
      i_sq_val = math.sqrt(r_sq - (i*i))
      y_val = [y + i_sq_val,y - i_sq_val]
      x_val = round(x_val)
      y_val[0] = round(y_val[0])
      y_val[1] = round(y_val[1])
      for j in y_val:
        if x_val <= 0 or j <= 0:
          return True
        if x_val >= self.size_x*self.scale or j >= self.size_y*self.scale:
          return True
        for k in self.contents:
          for l in k:
            if type(t) in l.permitCollisions:
              j_size = [int(self.scale*l.size_rescale[0]),int(self.scale*l.size_rescale[1])]
              if (x_val - j_size[0]/2 < l.x < x_val + j_size[0]/2) and (j - j_size[1]/2 < l.y < j + j_size[1]/2):
                return l.CollisionManager(t)
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

  def deleteRenderingComponent(self,obj):
    for i in self.contents:
      for j in i:
        if j == obj:
          i.remove(obj)
          break

  def sortRenderingComponents(self):
    for i in self.contents:
      i.sort(key=lambda x:x.y)

  def Decorator(self,tile,number,base_tile='all',z=2,stack=False,also_avoid=[]):
    for _ in range(number):
      stacked = False
      rx = randint(0,self.size_x*self.scale-1)
      ry = randint(0,self.size_y*self.scale-1)
      if not stack:
        for li in self.contents:
          for item in li:
            if type(item) == tile or type(item) in also_avoid:
              x = self.scale * item.size_rescale[0]
              y = self.scale * item.size_rescale[1]
              if (item.x - x + 1 < rx < item.x + x - 1 and item.y - y + 1 < ry < item.y + y - 1) or stacked:
                stacked = True
                break
      while base_tile not in self.map[ry // self.scale][rx // self.scale].name or stacked:
        stacked = False
        rx = randint(0,self.size_x*self.scale-1)
        ry = randint(0,self.size_y*self.scale-1)
        if not stack:
          for li in self.contents:
            for item in li:
              if type(item) == tile or type(item) in also_avoid:
                x = self.scale * item.size_rescale[0]
                y = self.scale * item.size_rescale[1]
                if (item.x - x < rx < item.x + x and item.y - y < ry < item.y + y) or stacked:
                  stacked = True
                  break
      self.addRenderingComponent(tile(rx,ry),zprior=z)

  def render(self):
    for i in range(len(self.map)):
      for j in range(len(self.map[i])):
        tile_at = self.map[i][j]
        Grid.gui.Image(tile_at.render(),j*self.scale,i*self.scale,self.scale*tile_at.size_rescale[0],self.scale*tile_at.size_rescale[1],tile_at.rotation,True)

    li_len = len(self.contents)
    for i in range(len(self.contents)):
      for j in self.contents[i-li_len]:
        if j.x < self.scale*self.size_x and j.y < self.scale*self.size_y:
          if j.x > 0 and j.y > 0:
            j.render()
