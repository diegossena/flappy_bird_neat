from typing import *

import pygame
import neat

from utils import sprite_get
from config import SCREEN_HEIGHT, SCREEN_WIDTH, FONT_SIZE, NEAT_IS_RUNNING

from entities import Bird, BirdAI, Floor, Pipes
# setup
pygame.font.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
text_font=pygame.font.SysFont('arial', FONT_SIZE)
clock = pygame.time.Clock()
neat_generation=1
# static_entities
floor = Floor(screen=screen)

def main(
  genomas: Iterator[Tuple[int, neat.DefaultGenome]],
  config: neat.Config
):
  global neat_generation, screen, text_font, clock, neat_generation, floor
  # setup    
  score = 0
  # generation_entities
  pipes = [Pipes(screen=screen,x=700)]
  if NEAT_IS_RUNNING:
    birds = [
      BirdAI(
        screen=screen,
        genoma=genoma,
        config=config,
      )
      for _, genoma in genomas
    ]
  else:
    birds = [Bird(screen=screen)]
  # generation_run
  while len(birds):
    clock.tick(30)
    # handle inputs
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      if not NEAT_IS_RUNNING:
        if  event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            for bird in birds:
              bird.jump()
    # entities_update
    floor.update()

    for pipe in pipes:
      if not pipe.passed and birds[0].x > pipe.top_pipe.x:
        pipe.passed = True
        score += 1
        pipes.append(Pipes(screen=screen,x=600))
        if NEAT_IS_RUNNING:
          for bird in birds:
            bird.genoma.fitness += 5
      if pipe.top_pipe.x + pipe.TOP_PIPE_SPRITE.get_width() < 0:
        pipes.remove(pipe)
      pipe.update()

    next_pipe = pipes[0]
    if (
      len(pipes) > 1
      and birds[0].x > pipes[0].top_pipe.x + pipes[0].TOP_PIPE_SPRITE.get_width()
    ):
      pipes[1]

    for bird in birds:
      if NEAT_IS_RUNNING:
        bird.update(next_pipe)
      else:
        bird.update()
    # collisions
    for bird in birds:
      # bird - pipes collision
      for pipe in pipes:
        if (
          bird.collision(pipe.top_pipe)
          or bird.collision(pipe.bottom_pipe)
        ):
          if NEAT_IS_RUNNING:
            bird.genoma.fitness -= 1
          birds.remove(bird)
    for bird in birds:
      # bird - floor collision
      if (bird.y + bird.sprite.get_height()) > floor.y or bird.y < 0:
        bird.genoma.fitness -= 5
        birds.remove(bird)
    # screen_draw
    screen.blit(sprite_get('bg.png'), (0, 0))
    for bird in birds:
      bird.draw()
    for pipe in pipes:
      pipe.draw()
    text = text_font.render(f"Pontuação: {score}", 1, (255, 255, 255))
    screen.blit(text, (SCREEN_WIDTH - 10 - text.get_width(), 10))
    if NEAT_IS_RUNNING:
      text = text_font.render(f"Geração: {neat_generation}", 1, (255, 255, 255))
      screen.blit(text, (10, 10))
    floor.draw()
    pygame.display.update()
  # on fail
  if NEAT_IS_RUNNING:
    neat_generation += 1

if __name__ == '__main__':
  if NEAT_IS_RUNNING:
    config = neat.Config(
      neat.DefaultGenome,
      neat.DefaultReproduction,
      neat.DefaultSpeciesSet,
      neat.DefaultStagnation,
      "neat.ini"
    )
    population = neat.Population(config)
    population.add_reporter(
      neat.StdOutReporter(True)
    )
    population.add_reporter(
      neat.StatisticsReporter()
    )
    population.run(main, 50)
  else:
    main(None, None)
