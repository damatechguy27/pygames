import pygame
import globals
from os.path import join
from general_settings import WINDOW_HEIGHT, WINDOW_WIDTH
from random import uniform, randint
#from globals import all_sprites

class meteors(pygame.sprite.Sprite):
    def __init__(self, position, *groups):
        super().__init__(*groups)

        
        # Meteors stuff
        # Loading meteor image
        meteor_image_path = join('resources','meteors','sm_meteor.png')
        # Getting meteor image size
        meteor_image = pygame.image.load(meteor_image_path).convert_alpha()
        meteor_width, meteor_height = 52, 56
        meteor_image_size = pygame.transform.scale(meteor_image,(meteor_width, meteor_height))

        
        self.image = meteor_image_size
        self.rect = self.image.get_frect(center = position)
        self.mask = pygame.mask.from_surface(self.image)

        # rotate meteors 
        #self.image = pygame.transform.rotate(self.image, )
        self.original_image = meteor_image_size
        self.rotation = 0
        self.rotation_spd = randint(100,200)

        # handles how long meteor is alive before being destroyed automatically
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 3000

        # handles the direction the meteor will be going after spawning
        self.direction = pygame.Vector2(uniform(-0.5,0.5),1)
        self.speed = randint(300,500)
    
    def update(self, dt):
        # updates the meteors speed 
        self.rect.center += self.direction * self.speed * dt        

        #handles rotation
        self.rotation += self.rotation_spd * dt
        self.image = pygame.transform.rotozoom(self.original_image, self.rotation,1)
        self.rect = self.image.get_frect(center=self.rect.center)

        # destroy meteor after it leaves the screen 
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()

class smallMeteor(meteors):
    def __init__(self, position):
        super().__init__(position)
        # Loading meteor image
        meteor_image_path = join('resources','meteors','sm_meteor.png')
        # Getting meteor image size
        meteor_image = pygame.image.load(meteor_image_path).convert_alpha()
        meteor_width, meteor_height = 52, 56
        meteor_image_size = pygame.transform.scale(meteor_image,(meteor_width, meteor_height))

        
        self.image = meteor_image_size
        self.rect = self.image.get_frect(center = position)
        self.mask = pygame.mask.from_surface(self.image)

class MediumMeteor(meteors):
    def __init__(self, position):
        super().__init__(position)
        # Loading meteor image
        meteor_image_path = join('resources','meteors','med_meteor.png')
        # Getting meteor image size
        meteor_image = pygame.image.load(meteor_image_path).convert_alpha()
        meteor_width, meteor_height = 76, 72
        meteor_image_size = pygame.transform.scale(meteor_image,(meteor_width, meteor_height))

        
        self.image = meteor_image_size
        self.rect = self.image.get_frect(center = position)
        self.mask = pygame.mask.from_surface(self.image)

class LargeMeteor(meteors):
    def __init__(self, position):
        super().__init__(position)
        # Loading meteor image
        meteor_image_path = join('resources','meteors','lg_meteor.png')
        # Getting meteor image size
        meteor_image = pygame.image.load(meteor_image_path).convert_alpha()
        meteor_width, meteor_height = 88, 72
        meteor_image_size = pygame.transform.scale(meteor_image,(meteor_width, meteor_height))

        
        self.image = meteor_image_size
        self.rect = self.image.get_frect(center = position)
        self.mask = pygame.mask.from_surface(self.image)