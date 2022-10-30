import pygame
import os

from config import SCALE, SCREEN_WIDTH, SCREEN_HEIGHT

def sprite_get(img_name: str):
    surface = pygame.image.load(
      os.path.join('imgs', img_name)
    )
    # if(img_name.startswith('bg')):
    #   width = SCREEN_WIDTH
    #   height = SCREEN_HEIGHT
    # elif(img_name.startswith('entity1')):
    #   return pygame.transform.scale2x(surface);
    # else:
    #   width = surface.get_width() * SCALE
    #   height = surface.get_height() * SCALE
    # return pygame.transform.scale(surface, (width, height));
    return pygame.transform.scale2x(surface);