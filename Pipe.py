import pygame
import random
from utils import sprite_get

class Pipe:
  SPRITE = sprite_get('pipe.png')
  DISTANCIA = 200
  VELOCIDADE = 5
  def __init__(self, x):
    self.x = x
    self.altura = 0
    self.pos_topo = 0
    self.pos_base = 0
    self.CANO_TOPO = pygame.transform.flip(self.SPRITE, False, True)
    self.CANO_BASE = self.SPRITE
    self.passed = False
    self.set_height()

  def set_height(self):
    self.altura = random.randrange(50, 450)
    self.pos_topo = self.altura - self.CANO_TOPO.get_height()
    self.pos_base = self.altura + self.DISTANCIA

  def update(self):
    self.x -= self.VELOCIDADE

  def draw(self, screen):
    screen.blit(self.CANO_TOPO, (self.x, self.pos_topo))
    screen.blit(self.CANO_BASE, (self.x, self.pos_base))

  def collission(self, passaro):
    passaro_mask = passaro.get_mask()
    topo_mask = pygame.mask.from_surface(self.CANO_TOPO)
    base_mask = pygame.mask.from_surface(self.CANO_BASE)
    distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y))
    distancia_base = (self.x - passaro.x, self.pos_base - round(passaro.y))
    topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)
    base_ponto = passaro_mask.overlap(base_mask, distancia_base)
    if base_ponto or topo_ponto:
      return True
    else:
      return False