import pygame
import globals
from os.path import join
from random import randint, uniform
from player import player
from obstacles import meteors
from projectiles import projectile
from general_settings import game_state, GameScore, GameLives
import animations
from animations import explosions
import resources
def collisions():
    # Collisions

    #check player and meteor collides if so destroy meteor
    collide_meteor = pygame.sprite.groupcollide(globals.players_group, globals.meteor_group, False, True,pygame.sprite.collide_mask)
    if collide_meteor and not GameLives.is_respawning:   
        GameLives.decrease_lives()
        GameScore.reset_score()
        GameLives.start_respawning()
        for player in collide_meteor:
            explosion = explosions(player.rect.midtop, (globals.all_sprites, globals.explosions))
            player.set_opacity(128)
            player.reset_position()
        # Pause meteors and wave timer
        globals.pause_meteors_and_waves()
        #game_state.end_game()
        #print("Loser!!!!")
    
    # check if laser collides with meteor
    collide_projectile = pygame.sprite.groupcollide(globals.meteor_group, globals.projectile_group , False, True)
    for meteor in collide_projectile:
        if meteor.meteorhit():
            meteor.kill()
            GameScore.increase_score(meteor.point_value)
            explosion = explosions(meteor.rect.midtop, (globals.all_sprites, globals.explosions))
            resources.explosion_snd.play()
        # print("explode")