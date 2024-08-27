import pygame
import globals
#from globals import laser_image_size
from os.path import join
from general_settings import WINDOW_HEIGHT, WINDOW_WIDTH
from projectiles import projectile
import resources


class player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        
        # Adding player sprites
        # Loading player image
        player_image_path = join('resources','player','PlayerRed.png')
        # Getting player image size
        player_image = pygame.image.load(player_image_path).convert_alpha()
        player_width, player_height = 64, 64
        player_image_size = pygame.transform.scale(player_image,(player_width, player_height))
        # Getting player position
        player_x, player_y = WINDOW_WIDTH/2, WINDOW_HEIGHT/2
        # Creating player object
        # player movement 
        self.direction= pygame.math.Vector2()
        self.speed = 300
                
        self.image = player_image_size
        self.rect = self.image.get_frect(center=(player_x,player_y))
    
        # creating player mask
        self.mask = pygame.mask.from_surface(self.image)

        #checks how often with can fire a bullet 
        self.can_shoot = True 
        self.shoot_time = 0
        self.cooldown_duration = 100 


        # # Lasers stuff
        # # Loading Laser image
        # laser_image_path = join('resources','projectiles','Laser_Small.png')
        # # Getting meteor image size
        # laser_image = pygame.image.load(laser_image_path).convert_alpha()
        # laser_width, laser_height = 16, 32
        # self.laser_image_size = pygame.transform.scale(laser_image,(laser_width, laser_height))


    def shot_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()

            if current_time - self.shoot_time >= self.cooldown_duration:
                self.can_shoot = True
    
    def update(self,dt):
        # Getting Input 
        movement_key = pygame.key.get_pressed()  
        action_key = pygame.key.get_just_pressed()
        self.direction.x = int(movement_key[pygame.K_RIGHT]) - int(movement_key[pygame.K_LEFT])
        self.direction.y = int(movement_key[pygame.K_DOWN]) - int(movement_key[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WINDOW_HEIGHT-120:
            self.rect.bottom = WINDOW_HEIGHT-120



        if action_key[pygame.K_SPACE] and self.can_shoot:
            #print("Fire")
            projectile(self.rect.midtop,(globals.all_sprites,globals.projectile_group))
            resources.laser_snd.play()
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

        self.shot_timer()



