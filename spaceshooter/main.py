import pygame
import globals
from os.path import join
from random import randint, uniform
from player import player
from obstacles import meteors
from projectiles import projectile
from general_settings import WINDOW_HEIGHT, WINDOW_WIDTH, running, clock, display_surface, game_caption

globals.init_groups()
#all_sprites = pygame.sprite.Group()

# creating player object
player = player(globals.all_sprites)

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

while running:
    dt=clock.tick()/1000
    # event loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #checks to see if meteor event has been triggered
        if event.type == meteor_event:
            # handles the creation of the meteors 
            print("create meteor")
            met_x, met_y = randint(0,WINDOW_WIDTH), randint(-200, -100)
            meteors((met_x,met_y),globals.all_sprites)
   
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
