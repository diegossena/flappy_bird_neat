import pygame

class Entity:
  def __init__(self, screen: pygame.Surface, sprite: pygame.Surface, x: int, y: int):
    self.x = x
    self.y = y
    self.sprite = sprite
    self.screen = screen

  def get_mask(self) -> pygame.Mask:
    return pygame.mask.from_surface(self.sprite)

  def collision(self, entity) -> bool:
    self_mask = self.get_mask()
    entity_mask = entity.get_mask()

    offset = (int(entity.x - self.x), int(entity.y - self.y))

    collide = self_mask.overlap(entity_mask, offset)

    return collide

  def draw(self):
    self.screen.blit(self.sprite, (self.x, self.y))