import pygame
import globals
#from globals import laser_image_size
from os.path import join
from general_settings import WINDOW_HEIGHT, WINDOW_WIDTH
from projectiles import projectile


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
        #player_binding_box = player_image_size.get_frect(center=(player_x,player_y))
        # player movement 
        self.direction= pygame.math.Vector2()
        self.speed = 300
        
        #self.laser = projectile()
        #self.laser_proj = laser_image_size
        
        self.image = player_image_size
        self.rect = self.image.get_frect(center=(player_x,player_y))
    

        self.can_shoot = True 
        self.shoot_time = 0
        self.cooldown_duration = 300 


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

        
        if action_key[pygame.K_SPACE] and self.can_shoot:
            print("Fire")
            projectile(self.rect.midtop,(globals.all_sprites,globals.projectile_group))
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

        self.shot_timer()



