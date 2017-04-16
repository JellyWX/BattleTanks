class Bullet:
  def __init__(gui,im,grid,x,y,vec):
    ## Rendering data ##
    self.gui
    self.im

    ## Subcritical data ##
    self.grid

    ## Critical data ##
    self.x
    self.y
    self.vec

  def move(self):
    self.x += self.vec[0]
    self.y += self.vec[1]

  def render(self):
    self.gui.Image(self.im,5,5,self.x,self.y)
