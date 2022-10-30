import math
import pygame
from utils import getSprite

class Bird:
    SPRITES = [
      getSprite(f"bird{i}.png")
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
        self.tick = 0
        self.sprite = self.SPRITES[0]
        self.sprite_tick = 0



    def jump(self):
        self.speed = -10.5
        self.tick = 0
        self.altura = self.y

    def update(self):
        # calcular o deslocamento
        self.tick += 1
        deslocamento = 1.5 * (self.tick**2) + self.speed * self.tick
        # restringir o deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2
        self.y += deslocamento
        # o angulo do passaro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angle < self.ROTACAO_MAXIMA:
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

        if self.angle <= -80:
            self.sprite = self.SPRITES[1]
            self.sprite_index = self.TRANSITION_DURATION*2
        else:
          self.sprite = self.SPRITES[sprite_index]
        # se o passaro tiver caindo eu não vou bater asa
            
        # draw a imagem
        imagem_rotacionada = pygame.transform.rotate(self.sprite, self.angle)
        pos_centro_imagem = self.sprite.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.sprite)