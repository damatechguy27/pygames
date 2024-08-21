import pygame
from os.path import join
# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
game_caption = pygame.display.set_caption('Space Shooter')
clock = pygame.time.Clock()

