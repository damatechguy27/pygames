import pygame
import globals
from os.path import join
from general_settings import WINDOW_HEIGHT, WINDOW_WIDTH
from random import uniform, randint
import random
import resources
#from globals import all_sprites

class meteors(pygame.sprite.Sprite):
    def __init__(self, position, *groups):
        super().__init__(*groups)

        # handles how long meteor is alive before being destroyed automatically
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 3000

        # handles the direction the meteor will be going after spawning
        self.direction = pygame.Vector2(uniform(-0.5,0.5),1)
        self.speed = randint(300,500)
        
        # hitpoints and score
        self.hitpoint = 1
        self.point_value = 1

    # Adds subtracting health from meteors 
    def meteorhit(self):
        self.hitpoint -= 1

        if self.hitpoint <= 0:
            return True
        return False        

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

class Meteor(meteors):
    def __init__(self, image_path, image_width, image_height, score_val, hitvalue, position, *groups):
        super().__init__(position, *groups)
        # Loading meteor image
        meteor_image_path = image_path
        # Getting meteor image size
        meteor_image = pygame.image.load(meteor_image_path).convert_alpha()
        meteor_image_size = pygame.transform.scale(meteor_image,(image_width, image_height))

        self.hitpoint = hitvalue
        self.point_value = score_val
        self.image = meteor_image_size
        self.rect = self.image.get_frect(center = position)
        self.mask = pygame.mask.from_surface(self.image)

        # rotate meteors 
        #self.image = pygame.transform.rotate(self.image, )
        self.original_image = meteor_image_size
        self.rotation = 0
        self.rotation_spd = randint(100,200)



class smallMeteor(meteors):
    def __init__(self, position, *groups):
        super().__init__(position, *groups)
        # Loading meteor image
        meteor_image_path = join('resources','meteors','sm_meteor.png')
        # Getting meteor image size
        meteor_image = pygame.image.load(meteor_image_path).convert_alpha()
        meteor_width, meteor_height = 52, 56
        meteor_image_size = pygame.transform.scale(meteor_image,(meteor_width, meteor_height))

        self.hitpoint = 1
        self.point_value = 100
        self.image = meteor_image_size
        self.rect = self.image.get_frect(center = position)
        self.mask = pygame.mask.from_surface(self.image)

        # rotate meteors 
        #self.image = pygame.transform.rotate(self.image, )
        self.original_image = meteor_image_size
        self.rotation = 0
        self.rotation_spd = randint(100,200)


class MediumMeteor(meteors):
    def __init__(self, position, *groups):
        super().__init__(position, *groups)
        # Loading meteor image
        meteor_image_path = join('resources','meteors','med_meteor.png')
        # Getting meteor image size
        meteor_image = pygame.image.load(meteor_image_path).convert_alpha()
        meteor_width, meteor_height = 76, 72
        meteor_image_size = pygame.transform.scale(meteor_image,(meteor_width, meteor_height))

        self.hitpoint = 4
        self.point_value = 200
        self.image = meteor_image_size
        self.rect = self.image.get_frect(center = position)
        self.mask = pygame.mask.from_surface(self.image)

        # rotate meteors 
        #self.image = pygame.transform.rotate(self.image, )
        self.original_image = meteor_image_size
        self.rotation = 0
        self.rotation_spd = randint(100,200)

class LargeMeteor(meteors):
    def __init__(self, position, *groups):
        super().__init__(position, *groups)
        # Loading meteor image
        meteor_image_path = join('resources','meteors','lg_meteor.png')
        # Getting meteor image size
        meteor_image = pygame.image.load(meteor_image_path).convert_alpha()
        meteor_width, meteor_height = 88, 72
        meteor_image_size = pygame.transform.scale(meteor_image,(meteor_width, meteor_height))

        self.hitpoint = 4
        self.point_value = 500
        self.image = meteor_image_size
        self.rect = self.image.get_frect(center = position)
        self.mask = pygame.mask.from_surface(self.image)

        # rotate meteors 
        #self.image = pygame.transform.rotate(self.image, )
        self.original_image = meteor_image_size
        self.rotation = 0
        self.rotation_spd = randint(100,200)

# Randomly select a meteor and spawns it
#sm_meteor = Meteor(resources.sm_meteor_image_path,52, 56,100,1)

def create_meteor(position, *groups):
    meteor_type = [smallMeteor, MediumMeteor, LargeMeteor]
    weights = [0.5,0.3,0.2]
    Meteor_class = random.choice(meteor_type)
    return Meteor_class(position, *groups)

