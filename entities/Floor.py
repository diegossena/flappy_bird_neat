import pygame

from utils import sprite_get

class Floor:
  VELOCIDADE = 5
  SPRITE = sprite_get('base.png')
  LARGURA = SPRITE.get_width()
  IMAGEM = SPRITE
  y = 730
  def __init__(self, screen: pygame.Surface):
    self.x1 = 0
    self.x2 = self.LARGURA
    self.screen = screen
  
  def update(self):
    self.x1 -= self.VELOCIDADE
    self.x2 -= self.VELOCIDADE
    if self.x1 + self.LARGURA < 0:
      self.x1 = self.x2 + self.LARGURA
    if self.x2 + self.LARGURA < 0:
      self.x2 = self.x1 + self.LARGURA

  def draw(self):
    self.screen.blit(self.IMAGEM, (self.x1, self.y))
    self.screen.blit(self.IMAGEM, (self.x2, self.y))