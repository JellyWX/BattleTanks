from bullet import Bullet

class Tank:
  def __init__(gui,im,grid,x,y,player=True):
    ## Rendering data ##
    self.gui = gui
    self.images = im

    ## Subcritical data ##
    self.map = grid

    ## Critical data ##
    self.x = x
    self.y = y
    self.facing = 0
    self.ai = not player

  def move(self,vec):
    self.x += vec[0]
    self.y += vec[1]

  def attack(self,touch,vec):
    self.bullet = Bullet(self,gui,self.im,self.x,self.y,)
