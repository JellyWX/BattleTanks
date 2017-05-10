from gui import GUI
from tank import Tank
from bullet import Bullet
from tile import Tile, Flower, Crate, MiniCrate
from grid import Grid
from BaseClass import BaseClass
from imageLoader import imageLoader

from random import random

import math
import os
import pygame
import sys

if 'debug' in sys.argv:
  GUI.debug = True

imageloader = imageLoader('assets/images/')

gui = GUI(400,400,'Battle Tanks')
grid = Grid(16,16)

BaseClass.grid = grid
BaseClass.gui = gui
BaseClass.images = imageloader

Tank.gui = gui
Tank.images = imageloader
Tank.grid = grid
Bullet.gui = gui
Bullet.images = imageloader
Bullet.grid = grid

grid.Draw('park')

done = False
process_stage = 0
player = Tank(40,40)
player_sequence = [player]
speed = 2
speed_bullet = 4

render_sequence =  [grid]

grid.Decorator(Flower,10,base_tile='grass')
grid.Decorator(Crate,4,base_tile='road',z=6)
grid.Decorator(MiniCrate,6,z=6)

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

        hyp_tank = math.sqrt(dx*dx + dy*dy)

        hyp_dis_x = dx / hyp_tank
        hyp_dis_y = dy / hyp_tank

        final_vec = (speed*hyp_dis_x,speed*hyp_dis_y)
        final_rotation = math.atan2(final_vec[0],final_vec[1])*180/math.pi

        player.move_cursor(final_vec,final_rotation+180)

    elif gui.keyAction(pygame.K_UP) or gui.keyAction(pygame.K_w):
      player.move_keys(1)

    elif gui.keyAction(pygame.K_DOWN) or gui.keyAction(pygame.K_s):
      player.move_keys(0)

    if gui.mouseAction(2):
      hyp_bullet = math.sqrt(dx*dx + dy*dy)

      hyp_dis_x_bullet = dx / hyp_bullet
      hyp_dis_y_bullet = dy / hyp_bullet

      bullet_vec = (speed_bullet*hyp_dis_x_bullet,speed_bullet*hyp_dis_y_bullet)

      player.attack(bullet_vec)



    ## Rotate turret ##
    player.rotate_turret(final_rotation_turret+180)

    for p in player_sequence:
      for b in p.bullets:
        b.move()

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
      for b in i.bullets:
        b.render()
    i.render()

  gui.flip(64)
