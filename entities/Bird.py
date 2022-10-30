import math
import pygame
import neat

from utils import sprite_get

class Bird:
  SPRITES = [
    sprite_get(f"bird{i}.png")
    for i in range(1, 4)
  ]
  x = 230
  def __init__(self):
    self.y = 350
    self.angle = 0
    self.speed = 0
    self.ticks = 0
    self.sprite = self.SPRITES[0]
    self.sprite_tick = 0

  def jump(self):
    self.speed = -10.5
    self.ticks = 0

  def update(self):
    # distance_calc
    self.ticks += 1
    distance = min(1.5 * (self.ticks**2) + self.speed * self.ticks, 16)
    if distance < 0:
      distance -= 2
    self.y += distance
    # bird_angle
    ANGLE_MAX = 25
    ANGLE_MIN = -90
    ANGLE_TRANSITION = 10
    if distance < 0:
      self.angle = ANGLE_MAX
    elif self.angle > ANGLE_MIN:
      self.angle = max(self.angle - ANGLE_TRANSITION, ANGLE_MIN)

  def draw(self, tela):
    SPRITE_TRANSITION_DURATION = 5
    self.sprite_tick += 1
    # select sprite
    sprite_index = math.floor(self.sprite_tick / self.SPRITE_TRANSITION_DURATION) % 3
    if(sprite_index == 0):
      self.sprite_tick = 0
    # se o passaro tiver caindo eu não vou bater asa
    if self.angle <= -80:
      self.sprite = self.SPRITES[1]
      self.sprite_index = self.SPRITE_TRANSITION_DURATION*2
    else:
      self.sprite = self.SPRITES[sprite_index]
        
    # draw a imagem
    sprite_rotated = pygame.transform.rotate(self.sprite, self.angle)
    sprite_center_position = self.sprite.get_rect(topleft=(self.x, self.y)).center
    rect = sprite_rotated.get_rect(center=sprite_center_position)
    tela.blit(sprite_rotated, rect.topleft)

  def get_mask(self):
    return pygame.mask.from_surface(self.sprite)

class BirdAI(Bird):
  def __init__(self, genoma: neat.DefaultGenome, config: neat.Config):
    self.network = neat.nn.FeedForwardNetwork.create(genoma, config)
    genoma.fitness = 0
    self.genoma = genoma