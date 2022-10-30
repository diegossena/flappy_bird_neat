import pygame

class Entity:
  def __init__(self, x: int, y: int, sprite: pygame.Surface):
    self.x = x
    self.y = y
    self.sprite = sprite

  def get_mask(self) -> pygame.Mask:
    return pygame.mask.from_surface(self.sprite)

  def collision(self, entity) -> bool:
    self_mask = self.get_mask()
    entity_mask = entity.get_mask()

    offset = (int(entity.x - self.x), int(entity.y - self.y))

    collide = self_mask.overlap(entity_mask, offset)

    return collide
  # def collission(self, bird):
  #   bird_mask = bird.get_mask()

  #   top_mask = pygame.mask.from_surface(self.CANO_TOPO)
  #   bottom_mask = pygame.mask.from_surface(self.CANO_BASE)

  #   distancia_topo = (self.x - bird.x, self.pos_topo - round(bird.y))
  #   distancia_base = (self.x - bird.x, self.pos_base - round(bird.y))

  #   top_ponto = bird_mask.overlap(top_mask, distancia_topo)
  #   bottom_ponto = bird_mask.overlap(bottom_mask, distancia_base)

  #   if bottom_ponto or top_ponto:
  #     return True
  #   else:
  #     return False