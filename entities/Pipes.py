import pygame
import random

from .Entity import Entity
from utils import sprite_get

class Pipes:
  BOTTOM_PIPE_SPRITE = sprite_get('pipe.png')
  TOP_PIPE_SPRITE = pygame.transform.flip(BOTTOM_PIPE_SPRITE, False, True)
  DISTANCE = 200
  SPEED = 5
  def __init__(self, x):
    altitude = random.randrange(50, 450)

    self.top_pipe = Entity(
      x=x,
      y=altitude - self.TOP_PIPE_SPRITE.get_height(),
      sprite=self.TOP_PIPE_SPRITE
    )
    
    self.bottom_pipe = Entity(
      x=x,
      y=altitude + self.DISTANCE,
      sprite=self.BOTTOM_PIPE_SPRITE
    )

    self.CANO_BASE = self.BOTTOM_PIPE_SPRITE
    self.passed = False

  def update(self):
    self.top_pipe.x -= self.SPEED
    self.bottom_pipe.x -= self.SPEED

  def draw(self, screen):
    screen.blit(self.TOP_PIPE_SPRITE, (self.top_pipe.x, self.top_pipe.y))
    screen.blit(self.BOTTOM_PIPE_SPRITE, (self.top_pipe.x, self.bottom_pipe.y))