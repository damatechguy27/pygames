import pygame
import globals
from os.path import join

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