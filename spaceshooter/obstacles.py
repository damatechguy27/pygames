import pygame
from os.path import join
from general_settings import WINDOW_HEIGHT, WINDOW_WIDTH
from random import uniform, randint
#from globals import all_sprites

class meteors(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)

        # Meteors stuff
        # Loading meteor image
        meteor_image_path = join('resources','meteors','meteor1.png')
        # Getting meteor image size
        meteor_image = pygame.image.load(meteor_image_path).convert_alpha()
        meteor_width, meteor_height = 64, 64
        meteor_image_size = pygame.transform.scale(meteor_image,(meteor_width, meteor_height))

        
        self.image = meteor_image_size
        self.rect = self.image.get_frect(center = position)
        
        # handles how long meteor is alive before being destroyed automatically
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 3000

        # handles the direction the meteor will be going after spawning
        self.direction = pygame.Vector2(uniform(-0.5,0.5),1)
        self.speed = randint(300,500)
    
    def update(self, dt):
        # updates the meteors speed 
        self.rect.center += self.direction * self.speed * dt        
 
        #destroy meteor after it leaves the screen 
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()
