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

# adding score
class score:
    def __init__(self):
        self.game_score = 0
        
        #this countrs score base on the time longer you survive more points you gain
        #self.current_time = pygame.time.get_ticks() // 100

    # Increase score
    def increase_score(self, amount):
        self.game_score += amount

    def display_score(self):
        comic_shark_font = join('resources','font','Comic Shark.ttf')
        cod_font = join('resources','font','CallOfOpsDutyIi-7Bgm4.ttf')
        font = pygame.font.Font(cod_font,40)
        font_display = font.render(f"Score: {self.game_score}", True, (255,251,0))
        display_surface.blit(font_display,(WINDOW_WIDTH/2,WINDOW_HEIGHT-75))

GameScore = score()  


# adding lives
class lives:
    def __init__(self):
        self.player_lives = 3

    # Increase lives
    def increase_lives(self, amount=1):
        self.player_lives += amount

    # decrease lives
    def decrease_lives(self, amount=1):
        self.player_lives -= amount


    def display_lives(self):
        comic_shark_font = join('resources','font','Comic Shark.ttf')
        cod_font = join('resources','font','CallOfOpsDutyIi-7Bgm4.ttf')
        font = pygame.font.Font(cod_font,40)
        font_display = font.render(f"Lives: {self.player_lives}", True, (255,251,0))
        display_surface.blit(font_display,(WINDOW_WIDTH/3,WINDOW_HEIGHT-75))

GameLives = lives()  



class UI:
    def __init__(self, screen_width, screen_height, border_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.border_height = border_height
        self.border_color = (50, 50, 50)  # Dark gray
        self.border_rect = pygame.Rect(0, screen_height - border_height, screen_width, border_height)

    def draw(self, surface):
        pygame.draw.rect(surface, self.border_color, self.border_rect)

HUD_boarder_height = WINDOW_HEIGHT-600
#display_HUD=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT-500))