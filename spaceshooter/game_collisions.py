import pygame
import globals
from os.path import join
from random import randint, uniform
from player import player
from obstacles import meteors
from projectiles import projectile
from general_settings import game_state, GameScore
import animations
from animations import explosions
import resources
def collisions():
    # Collisions

    #check player and meteor collides if so destroy meteor
    collide_meteor = pygame.sprite.groupcollide(globals.players_group, globals.meteor_group, True, True,pygame.sprite.collide_mask)
    if collide_meteor:

        game_state.end_game()
        print("Loser!!!!")
    
    # check if laser collides with meteor
    collide_projectile = pygame.sprite.groupcollide(globals.projectile_group, globals.meteor_group, True, True, pygame.sprite.collide_mask)
    for collide in collide_projectile:
    #if collide_projectile:
        GameScore.increase_score()
        explosion = explosions(collide.rect.midtop, (globals.all_sprites, globals.explosions))
        resources.explosion_snd.play()
       # print("explode")