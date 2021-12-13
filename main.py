import pygame
import config
from game import Game
from game_state import GameState
import os


#general setup
pygame.init()

#display surface
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("3 FAZ The Game")

clock = pygame.time.Clock()
game = Game(screen)
game.set_up()

while game.game_state == GameState.RUNNING:
    clock.tick(50)

    game.update()
    pygame.display.flip()
