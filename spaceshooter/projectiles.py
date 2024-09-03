import pygame
import globals
from os.path import join
from general_settings import WINDOW_HEIGHT, WINDOW_WIDTH
import math


class projectile(pygame.sprite.Sprite):
    def __init__(self, image_path, image_width, image_height, position, angle, groups):
        super().__init__(groups)

        # Lasers stuff
        # Loading Laser image
        laser_image_path = image_path
        # Getting meteor image size
        laser_image = pygame.image.load(laser_image_path).convert_alpha()
        laser_image_size = pygame.transform.scale(laser_image,(image_width, image_height))

        self.image = laser_image_size
        self.rect = self.image.get_frect(midbottom = position)
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = math.radians(angle)  # Convert to radians
        self.speed = 500
    def update(self, dt):
        
        self.rect.x += math.sin(self.angle) * self.speed * dt
        self.rect.y -= math.cos(self.angle) * self.speed * dt

        # destroy projectile if outside windows
        if self.rect.bottom <0:
            self.kill()
    