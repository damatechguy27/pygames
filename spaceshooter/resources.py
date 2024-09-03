import pygame
import globals
from os.path import join
from general_settings import WINDOW_HEIGHT, WINDOW_WIDTH

bg_music_path= join('resources','sounds','bg-music.wav')
bg_music = pygame.mixer.Sound(bg_music_path)
bg_music.set_volume(0.09)
#bg_music.play(loops=-1)

story_music_path= join('resources','sounds','story-scene.wav')
story_music_snd = pygame.mixer.Sound(story_music_path)
story_music_snd.set_volume(0.75)

lasersnd_path= join('resources','sounds','laser-snd.wav')
laser_snd = pygame.mixer.Sound(lasersnd_path)
laser_snd.set_volume(0.05)

explosionsnd_path= join('resources','sounds','explosion-snd.wav')
explosion_snd = pygame.mixer.Sound(explosionsnd_path)
explosion_snd.set_volume(0.05)

upgradesnd_path= join('resources','sounds','upgrade-snd.wav')
upgrade_snd = pygame.mixer.Sound(upgradesnd_path)
upgrade_snd.set_volume(0.05)


# Load play button 
play_screen_path = join('resources', 'buttons', 'Play-Button.png')
play_screen_image = pygame.image.load(play_screen_path)
play_screen_image_size = pygame.transform.scale(play_screen_image, (128, 64))

# Load quit button 
quit_screen_path = join('resources', 'buttons', 'Quit-Button.png')
quit_screen_image = pygame.image.load(quit_screen_path)
quit_screen_image_size = pygame.transform.scale(quit_screen_image, (WINDOW_WIDTH, WINDOW_HEIGHT))


#Main Menu Screen
mm_image_path = join('resources', 'screens', 'main_menu.jpg')
mm = pygame.image.load(mm_image_path)
mm_width, mm_height = 1280, 720
mm_img = pygame.transform.scale(mm,(mm_width, mm_height))
mm_rect = mm_img.get_frect(topleft=(0,0))


# Load STORY MENU screen image
story_screen_path = join('resources', 'screens', 'story_screen.jpg')
story_screen_image = pygame.image.load(story_screen_path)
story_screen_image_size = pygame.transform.scale(story_screen_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
story_rect = story_screen_image_size.get_frect(topleft=(0,0))


# Adding player sprites
# Loading player image
player_image_path = join('resources','player','PlayerRed.png')
# Getting player image size
player_image = pygame.image.load(player_image_path).convert_alpha()
player_width, player_height = 64, 64
player_image_size = pygame.transform.scale(player_image,(player_width, player_height))

#Meteors

# Loading Small meteor image
sm_meteor_image_path = join('resources','meteors','sm_meteor.png')
# Getting meteor image size
meteor_image = pygame.image.load(sm_meteor_image_path).convert_alpha()
meteor_width, meteor_height = 52, 56
meteor_image_size = pygame.transform.scale(meteor_image,(meteor_width, meteor_height))



# Loading Medieum meteor image
med_meteor_image_path = join('resources','meteors','med_meteor.png')
# Getting meteor image size
meteor_image = pygame.image.load(med_meteor_image_path).convert_alpha()
meteor_width, meteor_height = 76, 72
meteor_image_size = pygame.transform.scale(meteor_image,(meteor_width, meteor_height))


# Loading Large meteor image
lg_meteor_image_path = join('resources','meteors','lg_meteor.png')
# Getting meteor image size
meteor_image = pygame.image.load(lg_meteor_image_path).convert_alpha()
meteor_width, meteor_height = 88, 72
meteor_image_size = pygame.transform.scale(meteor_image,(meteor_width, meteor_height))


#Power up images 
powerup_image_path = join('resources','powerups','Powerup_Ammo.png')
# Getting meteor image size
powerup_image = pygame.image.load(powerup_image_path).convert_alpha()
powerup_width, powerup_height = 48, 30
powerup_image_size = pygame.transform.scale(powerup_image,(powerup_width, powerup_height))


# Lasers stuff
# Loading Laser image
laser_image_path = join('resources','projectiles','Laser_Small.png')
# Getting meteor image size
laser_image = pygame.image.load(laser_image_path).convert_alpha()
laser_width, laser_height = 16, 32
laser_image_size = pygame.transform.scale(laser_image,(laser_width, laser_height))
