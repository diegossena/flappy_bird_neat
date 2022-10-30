import pygame
from utils import getSprite

class Floor:
    VELOCIDADE = 5
    SPRITE = getSprite('base.png')
    LARGURA = SPRITE.get_width()
    IMAGEM = SPRITE
    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.LARGURA
  
    def update(self):
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE
        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x2 + self.LARGURA
        if self.x2 + self.LARGURA < 0:
            self.x2 = self.x1 + self.LARGURA

    def draw(self, tela):
        tela.blit(self.IMAGEM, (self.x1, self.y))
        tela.blit(self.IMAGEM, (self.x2, self.y))