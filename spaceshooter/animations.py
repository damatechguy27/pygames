import pygame
import globals
from os.path import join
from random import randint, uniform
from player import player
from obstacles import meteors
from projectiles import projectile


# Explosions 
class explosions(pygame.sprite.Sprite):
    def __init__(self, position,groups):
        super().__init__(groups)
       #explosions_frames = [join('resources','explosions',f'Explosion0{i}.png') for i in range(9)]
       #print(explosions_frames)
        # Loading Explosions image
        self.explosions_images = [pygame.image.load(join('resources','explosions',f'Explosion0{i}.png')).convert_alpha() for i in range(9)]
        
        # Getting Explosions image size
        #explosions_image = pygame.image.load(explosions_image_path).convert_alpha()
        #explosions_width, explosions_height = 64, 64
        #explosions_frms_img_size = pygame.transform.scale(explosions_images[0],(explosions_width, explosions_height))

        self.frames = self.explosions_images
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(center=position) 
    
    def update(self, dt):
        self.frame_index += 20 * dt
        if self.frame_index < len(self.frames):
            self.image = self.frames[int(self.frame_index)]
        else:
            self.kill()

