import pygame

from utils import getSprite
from config import SCALE, TELA_ALTURA, TELA_LARGURA

from Bird import Bird
from Pipe import Pipe
from Floor import Floor


pygame.font.init()
FONT_ARIAL = pygame.font.SysFont('arial', 50)

def screen_draw(screen, birds, pipes, floor, score):
    screen.blit(getSprite('bg.png'), (0, 0))
    for bird in birds:
        bird.draw(screen)

    for cano in pipes:
        cano.draw(screen)

    texto = FONT_ARIAL.render(f"Pontuação: {score}", 1, (255, 255, 255))
    screen.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))
    floor.draw(screen)
    pygame.display.update()

def main():
    screen = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA), pygame.SCALED)
    birds = [Bird(350)]
    floor = Floor(730)
    pipes = [Pipe(700)]
    score = 0
    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        # interação com o usuário
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_SPACE:
                for bird in birds:
                  bird.jump()
        # mover as coisas
        for bird in birds:
            bird.update()

        floor.update()
        adicionar_cano = False
        remover_canos = []
        for cano in pipes:
            for i, bird in enumerate(birds):
                if cano.colidir(bird):
                    birds.pop(i)
                if not cano.passou and bird.x > cano.x:
                    cano.passou = True
                    adicionar_cano = True
            cano.update()
            if cano.x + cano.CANO_TOPO.get_width() < 0:
                remover_canos.append(cano)

        if adicionar_cano:
            score += 1
            pipes.append(Pipe(600))

        for cano in remover_canos:
            pipes.remove(cano)
          
        for i, bird in enumerate(birds):
            if (bird.y + bird.sprite.get_height()) > floor.y or bird.y < 0:
                birds.pop(i)
        screen_draw(screen, birds, pipes, floor, score)

if __name__ == '__main__':
    main()






