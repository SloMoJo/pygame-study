import pygame
import sys
import numpy as np

#general setup
pygame.init()
clock = pygame.time.Clock()

#display surface
screen = pygame.display.set_mode((800,800))
second_surface = pygame.Surface([100,200])
second_surface.fill((0,0,255))

ophelia = pygame.image.load('cover_art_ophelia.png')
ophelia_rect = ophelia.get_rect(topleft = [100,200])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255,255,255))
    screen.blit(second_surface,(0,50))
    screen.blit(ophelia,ophelia_rect)
    ophelia_rect.right += 5

    pygame.display.flip()
    clock.tick(60)
