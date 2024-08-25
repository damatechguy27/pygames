import pygame
import globals
from os.path import join
from random import randint, uniform
from player import player
from obstacles import meteors
from projectiles import projectile
import game_collisions
from general_settings import WINDOW_HEIGHT, WINDOW_WIDTH, running, clock, display_surface, game_caption, game_state
#import importlib

#importlib.reload(globals)
globals.init_groups()
#all_sprites = pygame.sprite.Group()

# creating player object
player = player((globals.all_sprites,globals.players_group))

#handles creating the meteor event and has a meteor time to spawn set to every minute
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)



#surface 
surf = pygame.Surface((100,200))
surf.fill("yellow")

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
            #running = False
            game_state.end_game()
        
        #checks to see if meteor event has been triggered
        if event.type == meteor_event:
            # handles the creation of the meteors 
            #print("create meteor")
            met_x, met_y = randint(0,WINDOW_WIDTH), randint(-200, -100)
            # create meteor and add it to all sprite and meteor group
            meteors((met_x,met_y),(globals.all_sprites, globals.meteor_group))
   
   #adding collisions 
    game_collisions.collisions() 

    #updates delta tiem for all sprites 
    globals.all_sprites.update(dt)

      
    #draw the game
    display_surface.fill('blue')
    display_surface.blit(bg,(bg_x,bg_y))

    # handles the drawing of all sprites     
    globals.all_sprites.draw(display_surface)
    pygame.display.update() 

#End Game
pygame.quit()
