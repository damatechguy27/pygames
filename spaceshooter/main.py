import pygame
from os.path import join

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
pygame.display.set_caption('Space Shooter')
clock = pygame.time.Clock()


# Adding player sprites
# Loading player image
player_image_path = join('resources','player','Ship_1.png')
# Getting player image size
player_image = pygame.image.load(player_image_path).convert_alpha()
player_width, player_height = 64, 64
player_image_size = pygame.transform.scale(player_image,(player_width, player_height))
# Getting player position
player_x, player_y = WINDOW_WIDTH/2, WINDOW_HEIGHT/2
# Creating player object
player_binding_box = player_image_size.get_frect(center=(player_x,player_y))
# player movement 
player_direction= pygame.math.Vector2(1,-1)
player_speed = 300

# Meteors stuff
# Loading meteor image
meteor_image_path = join('resources','meteors','Meteor_10.png')
# Getting meteor image size
meteor_image = pygame.image.load(meteor_image_path).convert_alpha()
meteor_width, meteor_height = 64, 64
meteor_image_size = pygame.transform.scale(meteor_image,(meteor_width, meteor_height))
# Getting meteor position
meteor_x, meteor_y = 100, 200
# Creating meteor object
meteor_binding_box = player_image_size.get_frect(center=(meteor_x,meteor_y))


# Lasers stuff
# Loading Laser image
laser_image_path = join('resources','projectiles','Fire_Shot_2_2.png')
# Getting meteor image size
laser_image = pygame.image.load(laser_image_path).convert_alpha()
laser_width, laser_height = 16, 32
laser_image_size = pygame.transform.scale(laser_image,(laser_width, laser_height))
# Getting meteor position
laser_x, laser_y = 100, 500
# Creating meteor object
laser_binding_box = player_image_size.get_frect(center=(laser_x,laser_y))



#surface 
surf = pygame.Surface((100,200))
surf.fill("yellow")

#background 
bg_image_path = join('resources','background','BG.png')

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
    
    #draw the game
    display_surface.fill('blue')
    display_surface.blit(bg,(bg_x,bg_y))
    display_surface.blit(laser_image_size,laser_binding_box)
    display_surface.blit(meteor_image_size,meteor_binding_box)
    display_surface.blit(player_image_size,player_binding_box)
 
    player_binding_box.center += player_direction * player_speed * dt
    pygame.display.update() 

#End Game
pygame.quit()
