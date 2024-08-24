import pygame
from os.path import join

all_sprites=None

def init_groups():
    global all_sprites
    all_sprites = pygame.sprite.Group()
