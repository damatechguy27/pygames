import pygame
from random import randint
from os.path import join
import resources
class PowerUp(pygame.sprite.Sprite):
    def __init__(self, image_path, image_width, image_height, position ,*groups):
        super().__init__(*groups)
        # Lasers stuff
        # Loading Laser image
        powerup_image_path = image_path
        # Getting meteor image size
        powerup_image = pygame.image.load(powerup_image_path).convert_alpha()
        powerup_image_size = pygame.transform.scale(powerup_image,(image_width, image_height))

        self.image = powerup_image_size
        #self.rect = self.image.get_frect()
        self.mask = pygame.mask.from_surface(self.image)
        

        self.rect = self.image.get_frect(center=position)
        self.speed = 100  # pixels per second

        

    def update(self, dt):
        #self.rect.y += self.speed * dt
        self.rect.centery += 400 * dt
 
        if self.rect.top > 600:  # Adjust based on your screen height
            self.kill()