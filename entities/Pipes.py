import pygame
import random

from .Entity import Entity
from utils import sprite_get

class Pipes:
  BOTTOM_PIPE_SPRITE = sprite_get('pipe.png')
  TOP_PIPE_SPRITE = pygame.transform.flip(BOTTOM_PIPE_SPRITE, False, True)
  DISTANCE = 200
  SPEED = 5
  def __init__(self, screen: pygame.Surface, x: int):
    altitude = random.randrange(50, 450)

    self.top_pipe = Entity(
      screen=screen,
      sprite=self.TOP_PIPE_SPRITE,
      x=x,
      y=altitude - self.TOP_PIPE_SPRITE.get_height(),
    )
    
    self.bottom_pipe = Entity(
      screen=screen,
      x=x,
      sprite=self.BOTTOM_PIPE_SPRITE,
      y=altitude + self.DISTANCE,
    )

    self.CANO_BASE = self.BOTTOM_PIPE_SPRITE
    self.passed = False

  def update(self):
    self.top_pipe.x -= self.SPEED
    self.bottom_pipe.x -= self.SPEED

  def draw(self):
    self.top_pipe.draw()
    self.bottom_pipe.draw()