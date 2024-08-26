import pygame
from os.path import join

all_sprites=None
players_group = None
meteor_group = None
projectile_group = None
explosions = None
def init_groups():
    global all_sprites, players_group, meteor_group, projectile_group, explosions
    all_sprites = pygame.sprite.Group()
    players_group = pygame.sprite.Group()
    meteor_group = pygame.sprite.Group()
    projectile_group = pygame.sprite.Group()
    explosions = pygame.sprite.Group()
