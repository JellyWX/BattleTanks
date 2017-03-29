from gui import GUI
import pygame

gui = GUI(400,400,'Battle Tanks')
done = False
process_stage = 0

def stage(n):
  global gui
  for e in gui.event():
    if e.type == pygame.QUIT:
      return -1

  if n == 0:
    if gui.keysDown

  elif n == 1:
    return -1

while not done:
  if process_stage == -1:
    done = True

  process_stage = stage(process_stage)

  gui.flip(128)
