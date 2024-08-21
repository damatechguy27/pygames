import pygame
from os.path import join
from player import player
from general_settings import WINDOW_HEIGHT, WINDOW_WIDTH, running, clock, display_surface, game_caption

all_sprites = pygame.sprite.Group()

# creating player object
player = player(all_sprites)

# Meteors stuff
# Loading meteor image
meteor_image_path = join('resources','meteors','meteor1.png')
# Getting meteor image size
meteor_image = pygame.image.load(meteor_image_path).convert_alpha()
meteor_width, meteor_height = 64, 64
meteor_image_size = pygame.transform.scale(meteor_image,(meteor_width, meteor_height))
# Getting meteor position
meteor_x, meteor_y = 100, 200
# Creating meteor object
meteor_binding_box = meteor_image_size.get_frect(center=(meteor_x,meteor_y))


# Lasers stuff
# Loading Laser image
laser_image_path = join('resources','projectiles','Laser_Small.png')
# Getting meteor image size
laser_image = pygame.image.load(laser_image_path).convert_alpha()
laser_width, laser_height = 16, 32
laser_image_size = pygame.transform.scale(laser_image,(laser_width, laser_height))
# Getting meteor position
laser_x, laser_y = 100, 500
# Creating meteor object
laser_binding_box = laser_image_size.get_frect(center=(laser_x,laser_y))



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
   

    all_sprites.update(dt)
    #draw the game
    display_surface.fill('blue')
    display_surface.blit(bg,(bg_x,bg_y))
    display_surface.blit(laser_image_size,laser_binding_box)
    display_surface.blit(meteor_image_size,meteor_binding_box)
     
    all_sprites.draw(display_surface)
    pygame.display.update() 

#End Game
pygame.quit()
