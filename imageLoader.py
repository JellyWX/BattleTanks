import pygame

class imageLoader:
  def __init__(self,folder):
    self.images = {}

    for f in os.listdir('assets/images'):
      if f[-4:] == '.png':
        print('Loading asset ' + f)
        images[f[0:-4]] = pygame.image.load('assets/images/' + f)
