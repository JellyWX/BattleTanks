from gui import GUI
from tank import Tank
from random import random
import math
import os
import pygame

gui = GUI(400,400,'Battle Tanks')
images = {}
done = False
process_stage = 0
player = Tank(gui,images,10,10)
player_sequence = [player]
render_sequence = player_sequence
speed = 1
speed_bullet = 2

for f in os.listdir('assets/images'):
  if f[-4:] == '.png':
    print('Loading asset ' + f)
    images[f[0:-4]] = pygame.image.load('assets/images/' + f)

def stage(n):
  global gui
  for e in gui.event():
    if e.type == pygame.QUIT:
      return -1
    if e.type == pygame.VIDEORESIZE:
      gui.resize(e.dict['size'][0],e.dict['size'][1])

  if n == 0:
    dx = pygame.mouse.get_pos()[0] - player.x
    dy = pygame.mouse.get_pos()[1] - player.y

    rad_angle_turret = math.atan2(dx,dy)

    final_rotation_turret = rad_angle_turret*180/math.pi

    if gui.mouseAction(0):
      if not (-8 < dx < 8 and -8 < dy < 8):
        rad_angle = math.atan2(dy,dx)

        final_vec = (speed*math.cos(rad_angle),speed*math.sin(rad_angle))
        final_rotation = math.atan2(final_vec[0],final_vec[1])*180/math.pi

        player.move(final_vec,final_rotation+180)

    elif gui.mouseAction(2):
      rad_angle_bullet = math.atan2(dy,dx)
      bullet_vec = (speed_bullet*math.cos(rad_angle_bullet),speed*math.sin(rad_angle_bullet))

      player.attack(bullet_vec)

    ## Rotate turret ##
    player.rotate_turret(final_rotation_turret+180)

    for p in player_sequence:
      p.bullet.move()

    return 0

  elif n == 1:
    return -1

while not done:
  if process_stage == -1:
    done = True

  process_stage = stage(process_stage)

  gui.page.fill((0,0,0))

  for i in render_sequence:
    if isinstance(i,Tank):
      i.bullet.render()
    i.render()

  gui.flip(64)
