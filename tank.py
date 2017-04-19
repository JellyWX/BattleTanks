from bullet import Bullet

class Tank():
  def __init__(self,gui_,im,x,y,player=True):
    ## Rendering data ##
    self.gui = gui_
    self.images = im

    ## Subcritical data ##
    #self.map = grid
    self.bullet = Bullet(self.gui,self.images,-10,-10,(0,0))

    ## Critical data ##
    self.x = x
    self.y = y

    self.rotation = 0
    self.turret_rotation = 0

    self.ai = not player

  def move(self,vec,rotation):
    if self.rotation > 360:
      self.rotation -= 360
    elif self.rotation < 0:
      self.rotation += 360
    rotation = round(rotation,-1)
    rot_diff = (rotation - self.rotation) % 360

    '## Credits to /u/swimmer91 on Reddit for help with the line above. Many thanks! ##'
    if rot_diff < 10:
      self.x += round(vec[0])
      self.y += round(vec[1])
    elif rot_diff < 180:
      self.rotation += 10
    elif rot_diff > 180:
      self.rotation -= 10
    else:
      self.x += round(vec[0])
      self.y += round(vec[1])

  def rotate_turret(self,rotation):
    self.turret_rotation = rotation

  def render(self):
    self.gui.Image(self.images['tank1'],self.x-24,self.y-24,48,48,self.rotation)
    self.gui.Image(self.images['turret1'],self.x-24,self.y-24,48,48,self.turret_rotation)

  def attack(self,vec):
    if not self.bullet.alive:
      self.bullet = Bullet(self.gui,self.images,self.x,self.y,vec)
