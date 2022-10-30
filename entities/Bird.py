import math
import pygame
from utils import sprite_get

class Bird:
  SPRITES = [
    sprite_get(f"bird{i}.png")
    for i in range(1, 4)
  ]
  x = 230
  # animações da rotação
  ROTACAO_MAXIMA = 25
  VELOCIDADE_ROTACAO = 20
  TRANSITION_DURATION = 5

  def __init__(self, coord_y):
    self.y = coord_y
    self.angle = 0
    self.speed = 0
    self.altura = self.y
    self.ticks = 0
    self.sprite = self.SPRITES[0]
    self.sprite_tick = 0

  def jump(self):
    self.speed = -10.5
    self.ticks = 0
    self.altura = self.y

  def update(self):
    # distance_calc
    self.ticks += 1
    distance = 1.5 * (self.ticks**2) + self.speed * self.ticks
    # distance_clamp
    if distance > 16:
      distance = 16
    elif distance < 0:
      distance -= 2
    self.y += distance
    # bird_angle
    print(f"distance {distance}, angle {self.angle}\n")
    if distance < 16:
      self.angle = self.ROTACAO_MAXIMA
    else:
      if self.angle > -90:
        self.angle -= self.VELOCIDADE_ROTACAO

  def draw(self, tela):
    self.sprite_tick += 1;
    # definir qual imagem do passaro vai usar
    sprite_index = math.floor(self.sprite_tick / self.TRANSITION_DURATION) % 3
    if(sprite_index == 0):
      self.sprite_tick = 0

    # se o passaro tiver caindo eu não vou bater asa
    if self.angle <= -80:
      self.sprite = self.SPRITES[1]
      self.sprite_index = self.TRANSITION_DURATION*2
    else:
      self.sprite = self.SPRITES[sprite_index]
        
    # draw a imagem
    sprite_rotated = pygame.transform.rotate(self.sprite, self.angle)
    sprite_center_position = self.sprite.get_rect(topleft=(self.x, self.y)).center
    rect = sprite_rotated.get_rect(center=sprite_center_position)
    tela.blit(sprite_rotated, rect.topleft)

  def get_mask(self):
    return pygame.mask.from_surface(self.sprite)