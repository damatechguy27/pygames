import pygame
from os.path import join

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
pygame.display.set_caption('Space Shooter')

player_image_path = join('resources','player','Ship_LVL_1.png')

#adding player sprites
player = pygame.image.load(player_image_path)
player_width, player_height = 64, 64
player = pygame.transform.scale(player,(player_width, player_height))
player_x, player_y = 100, 200


#surface 
surf = pygame.Surface((100,200))

while running:
    # event loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #draw the game
    display_surface.fill('blue')
    display_surface.blit(player,(player_x,player_y))
    pygame.display.update() 

pygame.quit()
