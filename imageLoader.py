import pygame
import os

class imageLoader:
  def __init__(self,folder,default='404'):
    self.images = {}
    self.default = default

    for f in os.listdir(folder):
      if f[-4:] == '.png':
        print('Loading asset ' + f)
        self.images[f[0:-4]] = pygame.image.load(folder + f)

  def getImage(self,image,catch=True):
    if catch:
      try:
        return self.images[image]
      except KeyError:
        return self.images[self.default]
    else:
      return self.images[image]

  def addSource(self,folder):
    print('Loading another source. This will overwrite any files of the same name that are currently loaded.')
    for f in os.listdir(folder):
      if f[-4:] == '.png':
        print('Loading extra asset ' + f)
        self.images[f[0:-4]] = pygame.image.load(folder + f)
