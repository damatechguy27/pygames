import pygame
import globals
from os.path import join
from general_settings import WINDOW_HEIGHT, WINDOW_WIDTH

bg_music_path= join('resources','sounds','bg-music.wav')
bg_music = pygame.mixer.Sound(bg_music_path)
bg_music.set_volume(0.09)
#bg_music.play(loops=-1)

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
