import pygame

from utils import sprite_get
from config import SCREEN_HEIGHT, SCREEN_WIDTH, FONT_SIZE

from Bird import Bird
from Pipe import Pipe
from Floor import Floor

pygame.font.init()
FONT_ARIAL = pygame.font.SysFont('arial', FONT_SIZE)

def screen_draw(screen, birds, pipes, floor, score):
  screen.blit(sprite_get('bg.png'), (0, 0))

  for bird in birds:
    bird.draw(screen)
  for pipe in pipes:
    pipe.draw(screen)

  text = FONT_ARIAL.render(f"Pontuação: {score}", 1, (255, 255, 255))
  screen.blit(text, (SCREEN_WIDTH - 10 - text.get_width(), 10))

  floor.draw(screen)
  pygame.display.update()

def main():
    screen = pygame.display.set_mode(
      (SCREEN_WIDTH, SCREEN_HEIGHT)
    )
    # entities
    floor = Floor()
    birds = [Bird(350)]
    pipes = [Pipe(700)]
    score = 0
    clock = pygame.time.Clock()
    while len(birds):
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
      adding_pipe = False
      pipes_to_remove = []
      for pipe in pipes:
        for i, bird in enumerate(birds):
          if pipe.collission(bird):
            birds.pop(i)
          if not pipe.passed and bird.x > pipe.x:
            pipe.passed = True
            adding_pipe = True
        pipe.update()
        if pipe.x + pipe.CANO_TOPO.get_width() < 0:
          pipes_to_remove.append(pipe)

      if adding_pipe:
        score += 1
        pipes.append(Pipe(600))

      for pipe in pipes_to_remove:
        pipes.remove(pipe)

      for i, bird in enumerate(birds):
        if (bird.y + bird.sprite.get_height()) > floor.y or bird.y < 0:
          birds.pop(i)
      screen_draw(screen, birds, pipes, floor, score)

if __name__ == '__main__':
  main()
