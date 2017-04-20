from bullet import Bullet
import time

class Tank:
  
  gui = 0
  images = 0
  def __init__(self,x,y,player=True):

    ## Subcritical data ##
    #self.map = grid
    self.bullets = []
    self.last_fire = time.time()

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
    Tank.gui.Image(Tank.images['tank1'],self.x-24,self.y-24,48,48,self.rotation)
    Tank.gui.Image(Tank.images['turret1'],self.x-24,self.y-24,48,48,self.turret_rotation)

  def attack(self,vec):
    if  time.time() - self.last_fire > 1:
      if len(self.bullets) < 3:
        self.bullets.append(Bullet(Tank.gui,Tank.images,self.x,self.y,vec))
        self.last_fire = time.time()
      else:
        for i in range(0,len(self.bullets)):
          if self.bullets[i].alive == False:
            self.bullets[i] = Bullet(Tank.gui,Tank.images,self.x,self.y,vec)
            self.last_fire = time.time()
            break
