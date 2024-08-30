import pygame
from os.path import join

all_sprites=None
players_group = None
meteor_group = None
projectile_group = None
explosions = None
powerups = None

# Functions 
meteor_event = None
wave_event = None

def init_groups():
    global all_sprites, players_group, meteor_group, projectile_group, explosions, powerups
    all_sprites = pygame.sprite.Group()
    players_group = pygame.sprite.Group()
    meteor_group = pygame.sprite.Group()
    projectile_group = pygame.sprite.Group()
    explosions = pygame.sprite.Group()
    powerups = pygame.sprite.Group()

def pause_meteors_and_waves():
    global meteor_event, wave_event
    if meteor_event:
        pygame.time.set_timer(meteor_event, 0)
    if wave_event:
        pygame.time.set_timer(wave_event, 0)

def resume_meteors_and_waves(meteor_spawn_time, wave_time):
    global meteor_event, wave_event
    if meteor_event:
        pygame.time.set_timer(meteor_event, meteor_spawn_time)
    if wave_event:
        pygame.time.set_timer(wave_event, wave_time)