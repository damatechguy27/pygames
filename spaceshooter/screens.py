import pygame
import globals
from os.path import join
from random import randint, uniform
from player import players
from obstacles import meteors, smallMeteor, MediumMeteor, LargeMeteor, create_meteor
from projectiles import projectile
import game_collisions
from general_settings import WINDOW_HEIGHT, WINDOW_WIDTH, clock, display_surface
from general_settings import game_caption, game_state, GameScore, HUD_boarder_height, UI
from general_settings import GameLives
from resources import bg_music
import resources
from powerups import PowerUp
from buttons import Button
import sys
pygame.mixer.init()
#bg_music.play(loops=-1)
globals.init_groups()
def update_background(dt):
    global bg_y1, bg_y2
    
    # Move both background images down
    bg_y1 += scroll_spd * dt
    bg_y2 += scroll_spd * dt
    
    # If the bottom of the first background has moved below the screen
    if bg_y1 > WINDOW_HEIGHT:
        bg_y1 = bg_y2 - bg_height
    
    # If the bottom of the second background has moved below the screen
    if bg_y2 > WINDOW_HEIGHT:
        bg_y2 = bg_y1 - bg_height




def display_loss():
    comic_shark_font = join('resources','font','Comic Shark.ttf')
    cod_font = join('resources','font','CallOfOpsDutyIi-7Bgm4.ttf')
    font = pygame.font.Font(cod_font,70)
    font_display = font.render(f" YOU LOST, LOSSER!!!", True, (255,251,0))
    display_surface.blit(font_display,(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

def display_win():
    comic_shark_font = join('resources','font','Comic Shark.ttf')
    cod_font = join('resources','font','CallOfOpsDutyIi-7Bgm4.ttf')
    font = pygame.font.Font(cod_font,70)
    font_display = font.render(f"CONGRATS YOU WON!!!", True, (255,251,0))
    font_display_score = font.render(f"Your Score: {GameScore.game_score}", True, (255,251,0))
    display_surface.blit(font_display,(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))
    display_surface.blit(font_display_score,(WINDOW_WIDTH/2,WINDOW_HEIGHT/1.5))

#background 
bg_image_path = join('resources','background','Background.png')
bg = pygame.image.load(bg_image_path)
bg_width, bg_height = 1280, 720
bg = pygame.transform.scale(bg,(bg_width, bg_height)).convert()
bg_x, bg_y = 0, 0
bg_height = bg.get_height()
bg_rect = bg.get_rect()

# creating to images to make a scolling effect
bg_y1 = 0
bg_y2 = -bg_height
scroll_spd = 50

# Load MAIN MENU screen image
menu_screen_path = join('resources', 'screens', 'menu_screen.jpg')
menu_screen_image = pygame.image.load(menu_screen_path)
menu_screen_image_size = pygame.transform.scale(menu_screen_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

# def create_game_objects():
#     global player
#     player = Player((globals.all_sprites, globals.players_group))
#     # Initialize other game objects here if needed
# creating player object


# def reset_game():
#     player = players((globals.all_sprites,globals.players_group))
#     wave_counter = 1
#     meteor_spawn_time = 1000
#     powerup_spawn_timer = 0
#     player.reset_upgrade()
#     GameScore.reset_score()
#     GameLives.reset_lives()
#     player.reset_position()
    



def main_menu():
    def display_menu_text():
        comic_shark_font = join('resources','font','Comic Shark.ttf')
        cod_font = join('resources','font','CallOfOpsDutyIi-7Bgm4.ttf')
        font = pygame.font.Font(cod_font,70)
        font_display = font.render(f"Space Fighter X", True, (255,251,0))
        display_surface.blit(font_display,(WINDOW_WIDTH/1.6,WINDOW_HEIGHT-120))


    play_button = Button(resources.play_screen_path,(128,64),(WINDOW_WIDTH/2,WINDOW_HEIGHT-500))
    quit_button = Button(resources.quit_screen_path,(128,64),(WINDOW_WIDTH/2,WINDOW_HEIGHT-400))
    while game_state.is_main_menu:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                if play_button.rect.collidepoint(event.pos):
                    
                    game_state.on_game()
                    game_screen()
                elif quit_button.rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        
        display_surface.fill((0,0,0))

        display_surface.blit(resources.mm_img,resources.mm_rect)

        display_menu_text()

        display_surface.blit(play_button.image, play_button.rect)
        
        
        display_surface.blit(quit_button.image, quit_button.rect)
        pygame.display.update()
    pygame.quit()
    sys.exit()


def game_screen():
    player = players((globals.all_sprites,globals.players_group))
    wave_counter = 10
    meteor_spawn_time = 100
    powerup_spawn_timer = 0
    player.reset_upgrade()
    GameScore.reset_score()
    GameLives.reset_lives()
    player.reset_position()
    GameLives.is_respawning=False

    bg_music.play(loops=-1)
    # checking for if player has won or lost the game 
    GAMEOVER = False
    GAMEWON = False
    # Powerup # Power-up spawn timer
    powerup_spawn_timer = 0
    powerup_spawn_interval = 15  # seconds



    #creating UI 
    ui = UI(WINDOW_WIDTH,WINDOW_HEIGHT+0,HUD_boarder_height)


    #handles creating the meteor event and has a meteor time to spawn set to every minute
    meteor_event = pygame.event.custom_type()
    meteor_spawn_time = 1000
    pygame.time.set_timer(meteor_event, meteor_spawn_time)
    globals.meteor_event = meteor_event

    #handles the waves 
    wave_event = pygame.event.custom_type()
    wave_time = 30000
    pygame.time.set_timer(wave_event, wave_time)
    globals.wave_event = wave_event

    wave_counter = 1 
    difficulty_increase = 100

    



    # Load loss screen image
    loss_screen_path = join('resources', 'screens', 'loss_screen.jpg')
    loss_screen_image = pygame.image.load(loss_screen_path)
    loss_screen_image_size = pygame.transform.scale(loss_screen_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    # Load Win screen image
    win_screen_path = join('resources', 'screens', 'win_screen.jpg')
    win_screen_image = pygame.image.load(win_screen_path)
    win_screen_image_size = pygame.transform.scale(win_screen_image, (WINDOW_WIDTH, WINDOW_HEIGHT))


    while game_state.is_game:
        dt=clock.tick()/1000



        # adding function for updating scrolling background
        update_background(dt)


        # event loop 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            #checks to see if meteor event has been triggered
            if event.type == meteor_event:
            #     # handles the creation of the meteors 
            #     #print("create meteor")
                met_x, met_y = randint(100,1100), randint(-200, -100)
                create_meteor((met_x,met_y),(globals.all_sprites, globals.meteor_group))
            
            if event.type == wave_event:
                #increase wave count by 1 
                wave_counter += 1

                #decreases the wave by decreasing the meteor spawn time by 100
                meteor_spawn_time = max(0, meteor_spawn_time - difficulty_increase)

                #met_x, met_y = randint(500,750), randint(-200, -100)
                pygame.time.set_timer(meteor_event, meteor_spawn_time)

                #prints the wave number out 
                print(f"Wave {wave_counter} started! Meteor spawn time: {meteor_spawn_time}ms")
        
        if not GAMEOVER and not GAMEWON:
        # Update game objects
            respawn_complete = GameLives.update()
            if respawn_complete:
                globals.resume_meteors_and_waves(meteor_spawn_time, wave_time)
                for player in globals.players_group:
                    player.set_opacity(255)  # Set opacity back to 100%

            if not GameLives.is_respawning:
                for sprite in globals.all_sprites:
                    if hasattr(sprite, 'update'):
                        if 'dt' in sprite.update.__code__.co_varnames:
                            sprite.update(dt)
                        else:
                            sprite.update()
            else:
                # Update all sprites except the player
                for sprite in globals.all_sprites:
                    if sprite not in globals.players_group:
                        if hasattr(sprite, 'update'):
                            if 'dt' in sprite.update.__code__.co_varnames:
                                sprite.update(dt)
                            else:
                                sprite.update()


            #print(GameLives.is_respawning)
            powerup_spawn_timer += dt
            if powerup_spawn_timer >= powerup_spawn_interval:
                powerup_x, powerup_y= randint(500,750), randint(-200, -100)
                PowerUp((powerup_x, powerup_y),(globals.all_sprites, globals.powerups))
                powerup_spawn_timer = 0


            #adding collisions 
            game_collisions.collisions() 
            #draw the game
            #display_surface.blit(bg,(bg_x,bg_y))

            # scrolling background
            display_surface.blit(bg,(0,bg_y1))
            display_surface.blit(bg,(0,bg_y2))

            # handles the drawing of all sprites     
            globals.all_sprites.draw(display_surface)
            #display_surface.blit(font_display,(200,100))

            
            #display_HUD.fill('blue')
            ui.draw(display_surface)
            GameScore.display_score()
            GameLives.display_lives()
            


            # Check for game over
            if GameLives.player_lives < 0:
                GAMEOVER = True
                player.kill()
                #game_state.end_game()
                loss_start_time = pygame.time.get_ticks()

            if GameLives.player_lives >= 0 and meteor_spawn_time == 0 and not GameLives.is_respawning:
                GAMEWON = True
                player.kill()
                #game_state.end_game()
                win_start_time = pygame.time.get_ticks()



        elif GAMEOVER:
            display_surface.blit(loss_screen_image_size, (0, 0))
            # Check if 5 seconds have passed
            display_loss()
            if pygame.time.get_ticks() - loss_start_time > 5000:  # 5000 ms = 5 seconds
                game_state.on_main_menu()
                main_menu()

        elif GAMEWON:
            display_surface.blit(win_screen_image_size, (0, 0))
                    # Check if 5 seconds have passed
            display_win()
            if pygame.time.get_ticks() - win_start_time > 5000:  # 5000 ms = 5 seconds
                game_state.on_main_menu()
                main_menu()

        pygame.display.update()
    #End Game
    pygame.quit()
    sys.exit()
