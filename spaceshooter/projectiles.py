import pygame
import globals
from os.path import join
from general_settings import WINDOW_HEIGHT, WINDOW_WIDTH
import math
#projectiles =[]

# Lasers stuff
# Loading Laser image
# laser_image_path = join('resources','projectiles','Laser_Small.png')
# Getting meteor image size
# laser_image = pygame.image.load(laser_image_path).convert_alpha()
# laser_width, laser_height = 16, 32
# laser_image_size = pygame.transform.scale(laser_image,(laser_width, laser_height))
# # Getting meteor position
# laser_x, laser_y = 100, 500



class projectile(pygame.sprite.Sprite):
    def __init__(self, position, angle, groups):
        super().__init__(groups)

        # Lasers stuff
        # Loading Laser image
        laser_image_path = join('resources','projectiles','Laser_Small.png')
        # Getting meteor image size
        laser_image = pygame.image.load(laser_image_path).convert_alpha()
        laser_width, laser_height = 16, 32
        laser_image_size = pygame.transform.scale(laser_image,(laser_width, laser_height))

        self.image = laser_image_size
        self.rect = self.image.get_frect(midbottom = position)
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = math.radians(angle)  # Convert to radians
        self.speed = 500
    def update(self, dt):
        #moves projectile
        #self.rect.centery -= 400 * dt 
        

        self.rect.x += math.sin(self.angle) * self.speed * dt
        self.rect.y -= math.cos(self.angle) * self.speed * dt

        # destroy projectile if outside windows
        if self.rect.bottom <0:
            self.kill()
    