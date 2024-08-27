import pygame
import globals
from os.path import join
from random import randint, uniform
from player import player
from obstacles import meteors, smallMeteor, MediumMeteor, LargeMeteor, create_meteor
from projectiles import projectile
import game_collisions
from general_settings import WINDOW_HEIGHT, WINDOW_WIDTH, clock, display_surface
from general_settings import game_caption, game_state, GameScore, HUD_boarder_height, UI
from general_settings import GameLives
from resources import bg_music
#import importlib

#importlib.reload(globals)
globals.init_groups()
bg_music.play(loops=-1)

#all_sprites = pygame.sprite.Group()

#creating UI 
ui = UI(WINDOW_WIDTH,WINDOW_HEIGHT+0,HUD_boarder_height)

# creating player object
player = player((globals.all_sprites,globals.players_group))

#handles creating the meteor event and has a meteor time to spawn set to every minute
meteor_event = pygame.event.custom_type()
meteor_spawn_time = 1000
pygame.time.set_timer(meteor_event, meteor_spawn_time)

#handles the waves 
wave_event = pygame.event.custom_type()
wave_time = 30000
pygame.time.set_timer(wave_event, wave_time)

wave_counter = 1 
difficulty_increase = 100

#surface 
surf = pygame.Surface((100,200))
surf.fill("black")


# checking to see pygame finds all animation sprites 
#explosions_frames = [pygame.image.load(join('resources','explosions',f'Explosion0{i}.png')).convert_alpha() for i in range(9)]
#explosions_image = pygame.image.load(explosions_frames)
#print(explosions_frames)

#background 
bg_image_path = join('resources','background','Background.png')

#adding bg sprites
bg = pygame.image.load(bg_image_path)
bg_width, bg_height = 1280, 720
bg = pygame.transform.scale(bg,(bg_width, bg_height))
bg_x, bg_y = 0, 0

while not game_state.is_game_over:
    dt=clock.tick()/1000
    # event loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state.end_game()
        
        #checks to see if meteor event has been triggered
        if event.type == meteor_event:
        #     # handles the creation of the meteors 
        #     #print("create meteor")
             met_x, met_y = randint(500,750), randint(-200, -100)
             create_meteor((met_x,met_y),(globals.all_sprites, globals.meteor_group))
        
        if event.type == wave_event:
            #increase wave count by 1 
            wave_counter += 1

            #decreases the wave by decreasing the meteor spawn time by 100
            meteor_spawn_time = max(100, meteor_spawn_time - difficulty_increase)

            #met_x, met_y = randint(500,750), randint(-200, -100)
            pygame.time.set_timer(meteor_event, meteor_spawn_time)

            #prints the wave number out 
            print(f"Wave {wave_counter} started! Meteor spawn time: {meteor_spawn_time}ms")
   #adding collisions 
    game_collisions.collisions() 

    #updates delta tiem for all sprites 
    globals.all_sprites.update(dt)

      
    #draw the game
    display_surface.blit(bg,(bg_x,bg_y))

    # handles the drawing of all sprites     
    globals.all_sprites.draw(display_surface)
    #display_surface.blit(font_display,(200,100))

    
    #display_HUD.fill('blue')
    ui.draw(display_surface)
    GameScore.display_score()
    GameLives.display_lives()
    pygame.display.update() 

#End Game
pygame.quit()
