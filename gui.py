import struct
from sys import exit
import pygame
from time import sleep

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

class GUI(object):
  def __init__(self,w,h,title):
    self.width = w
    self.height = h
    self.title = title
    self.color = (0,0,0)

    pygame.init()
    self.display = pygame.display
    self.page = self.display.set_mode((self.width,self.height),pygame.RESIZABLE)
    self.display.set_caption(self.title)

    self.f = None

  def resize(self,w,h):
    self.page = self.display.set_mode((w,h),pygame.RESIZABLE)
    self.width = w
    self.height = h

  def Color(self,hexa):
    if type(hexa) is str:
      self.color = struct.unpack('BBB',bytes.fromhex(hexa))
    elif type(hexa) is tuple:
      self.color = hexa
    else:
      raise ValueError

  def Text(self,t,s,anti=False,f='monospace'):
    self.f = pygame.font.SysFont(f, s).render(t,anti,self.color)

  def Rect(self,x,y,w,h):
    pygame.draw.rect(self.page, self.color, pygame.Rect(x,y,w,h))

  def Circle(self,x,y,r):
    pygame.draw.circle(self.page, self.color, (x,y), r)

  def showText(self,x,y):
    self.page.blit(self.f, (x,y))

  def flip(self,t):
    self.display.flip()
    sleep(1/t)

  def event(self):
    return pygame.event.get()

  def keyAction(self,k=None):
    if k != None:
      return pygame.key.get_pressed()[k]
    else:
      return pygame.key.get_pressed()

  def Image(self,im,x,y,size_x,size_y,rotation=0,tile=False):
    im = pygame.transform.scale(im,(size_x,size_y))
    im = rot_center(im,rotation)
    if tile:
      im = pygame.transform.scale(im,(size_x*4,size_y*4))
      self.page.blit(im,(x,y),(0.75*size_x,0.75*size_y,size_x,size_y))
      return
    self.page.blit(im,(x,y))

  def mouseAction(self,k=None):
    if k != None:
      return pygame.mouse.get_pressed()[k]
    else:
      return pygame.mouse.get_pressed()
