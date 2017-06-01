from tile import *

class mapLoader():
  def __init__(self,name,path):
    self.name = name
    self.path = path

    with open(self.path + '/map.map') as f:
      for line in f:
        
