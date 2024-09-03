import pygame
import globals
#from globals import laser_image_size
from os.path import join
from general_settings import WINDOW_HEIGHT, WINDOW_WIDTH
from projectiles import projectile
import resources


class players(pygame.sprite.Sprite):
    def __init__(self, image_path, image_width, image_height, groups):
        super().__init__(groups)
        
        # Adding player sprites
        # Loading player image
        player_image_path = image_path
        # Getting player image size
        player_image = pygame.image.load(player_image_path).convert_alpha()
        player_image_size = pygame.transform.scale(player_image,(image_width, image_height))
        # Getting player position
        player_x, player_y = WINDOW_WIDTH/2, WINDOW_HEIGHT-120
        # Creating player object
        # player movement 
        self.direction= pygame.math.Vector2()
        self.speed = 300
        self.inital_position = (player_x, player_y)
                
        self.image = player_image_size
        self.rect = self.image.get_frect(center=(player_x,player_y))
        self.original_image = self.image.copy()
        # creating player mask
        self.mask = pygame.mask.from_surface(self.image)

        #checks how often with can fire a bullet 
        self.can_shoot = True 
        self.shoot_time = 0
        self.cooldown_duration = 200 

        self.upgrade_level = 0
        # # Lasers stuff
        # # Loading Laser image
        # laser_image_path = join('resources','projectiles','Laser_Small.png')
        # # Getting meteor image size
        # laser_image = pygame.image.load(laser_image_path).convert_alpha()
        # laser_width, laser_height = 16, 32
        # self.laser_image_size = pygame.transform.scale(laser_image,(laser_width, laser_height))

#####################################################
#  POWER UPGRADES 
#####################################################
    def shoot(self, groups):
        if self.shoot_cooldown <= 0:
            if self.upgrade_level == 0:
                self._shoot_single(groups)
            elif self.upgrade_level == 1:
                self._shoot_double(groups)
            elif self.upgrade_level == 2:
                self._shoot_triple(groups)
            else:
                self._shoot_six(groups)
            self.shoot_cooldown = self.shoot_delay

    def _shoot_single(self, groups):
        projectile(resources.laser_image_path,16,32,self.rect.midtop, 0, groups)

    def _shoot_double(self, groups):
        projectile(resources.laser_image_path,16,32,self.rect.midtop, 0, groups)
        projectile(resources.laser_image_path,16,32,(self.rect.left, self.rect.top), 0, groups)

    def _shoot_triple(self, groups):
        projectile(resources.laser_image_path,16,32,self.rect.midtop, 0, groups)
        projectile(resources.laser_image_path,16,32,(self.rect.left, self.rect.top), -15, groups)
        projectile(resources.laser_image_path,16,32,(self.rect.right, self.rect.top), 15, groups)

    def _shoot_six(self, groups):
        projectile(resources.laser_image_path,16,32,self.rect.midtop, 0, groups)
        projectile(resources.laser_image_path,16,32,(self.rect.midtop[0] + 10, self.rect.midtop[1]), 0, groups)
        projectile(resources.laser_image_path,16,32,(self.rect.left, self.rect.top), -15, groups)
        projectile(resources.laser_image_path,16,32,(self.rect.left + 10, self.rect.top), -15, groups)
        projectile(resources.laser_image_path,16,32,(self.rect.right, self.rect.top), 15, groups)
        projectile(resources.laser_image_path,16,32,(self.rect.right - 10, self.rect.top), 15, groups)

    def reset_upgrade(self):
        self.upgrade_level = 0

    def upgrade(self):
        if self.upgrade_level < 3:
            self.upgrade_level += 1

###########################################################################


    def shot_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()

            if current_time - self.shoot_time >= self.cooldown_duration:
                self.can_shoot = True
    
    def reset_position(self):
        self.rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT-200)

    #changes the opacity when player dies 
    def set_opacity(self, opacity):
            self.image = self.original_image.copy()
            self.image.set_alpha(opacity)

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
            # projectile(self.rect.midtop,(globals.all_sprites,globals.projectile_group))
            # resources.laser_snd.play()
            # self.can_shoot = False
            # self.shoot_time = pygame.time.get_ticks()


            if self.upgrade_level == 0:
                self._shoot_single((globals.all_sprites,globals.projectile_group))
                resources.laser_snd.play()
                self.can_shoot = False
                self.shoot_time = pygame.time.get_ticks()
            elif self.upgrade_level == 1:
                self._shoot_double((globals.all_sprites,globals.projectile_group))
                resources.laser_snd.play()
                self.can_shoot = False
                self.shoot_time = pygame.time.get_ticks()
            elif self.upgrade_level == 2:
                self._shoot_triple((globals.all_sprites,globals.projectile_group))
                resources.laser_snd.play()
                self.can_shoot = False
                self.shoot_time = pygame.time.get_ticks()
            else:
                self._shoot_six((globals.all_sprites,globals.projectile_group))
                resources.laser_snd.play()
                self.can_shoot = False
                self.shoot_time = pygame.time.get_ticks()
            #self.shoot_cooldown = self.shoot_delay
            self.shoot_time = pygame.time.get_ticks()

        self.shot_timer()



