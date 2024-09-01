import pygame
pygame.init()
pygame.mixer.init()
import globals
from os.path import join
from random import randint, uniform
from player import players
from obstacles import meteors, smallMeteor, MediumMeteor, LargeMeteor, create_meteor
from projectiles import projectile
import game_collisions
from general_settings import WINDOW_HEIGHT, WINDOW_WIDTH, clock, display_surface
from general_settings import game_caption, game_state, GameScore, HUD_boarder_height, UI
from general_settings import GameLives
from resources import bg_music
from powerups import PowerUp
import sys
from screens import main_menu, game_screen
#import importlib


globals.init_groups()

#surface 
surf = pygame.Surface((100,200))
surf.fill("black")


while not game_state.is_game_over:
    main_menu()

pygame.quit()

