import pygame
import os

from config import SCALE

def getSprite(img_name: str):
    surface = pygame.image.load(
      os.path.join('imgs', img_name)
    )
    # width = surface.get_width() * SCALE
    # height = surface.get_height() * SCALE
    # return pygame.transform.scale(surface, (width, height));
    return pygame.transform.scale2x(surface);