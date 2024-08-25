import pygame
from os.path import join
# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
game_caption = pygame.display.set_caption('Space Shooter')
clock = pygame.time.Clock()


# game_state.py
class GameState:
    def __init__(self):
        self.is_game_over = False

    def end_game(self):
        self.is_game_over = True


game_state = GameState()
