import pygame
import sys
import json
import random
from threading import Thread

try:
    from playsound import playsound
    audio_available = True
except ImportError:
    audio_available = False

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sports Quiz Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Fonts
title_font = pygame.font.Font(None, 64)
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

# Load quiz data
def load_quiz(sport, difficulty):
    with open(f"{sport}_{difficulty}_quiz.json", "r") as file:
        return json.load(file)

# Quiz data
sports = ["Football", "Basketball", "Soccer"]
difficulties = ["Basic", "Intermediate", "Advanced"]

current_sport = None
current_difficulty = None
current_quiz = None
current_question = 0
score = 0
wrong_answers = []

# Play background music if available
if audio_available:
    def play_music():
        while True:
            playsound("background_music.mp3")

    music_thread = Thread(target=play_music, daemon=True)
    music_thread.start()

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def draw_button(text, x, y, w, h, color):
    pygame.draw.rect(screen, color, (x, y, w, h))
    draw_text(text, font, BLACK, x + w // 2, y + h // 2)

def splash_screen():
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < 3000:  # Display for 3 seconds
        screen.fill(WHITE)
        draw_text("Welcome to Sports Quiz!", title_font, BLUE, WIDTH // 2, HEIGHT // 2)
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def main_menu():
    while True:
        screen.fill(WHITE)
        draw_text("Sports Quiz Game", title_font, BLACK, WIDTH // 2, 100)
        
        draw_button("Start Game", 250, 250, 300, 75, GREEN)
        draw_button("Exit", 250, 350, 300, 75, RED)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if pygame.Rect(250, 250, 300, 75).collidepoint(mouse_pos):
                    return "start"
                elif pygame.Rect(250, 350, 300, 75).collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

def select_sport():
    global current_sport
    while True:
        screen.fill(WHITE)
        draw_text("Select a Sport", font, BLACK, WIDTH // 2, 100)
        
        for i, sport in enumerate(sports):
            draw_button(sport, 250, 200 + i * 100, 300, 75, GREEN)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, sport in enumerate(sports):
                    button_rect = pygame.Rect(250, 200 + i * 100, 300, 75)
                    if button_rect.collidepoint(mouse_pos):
                        current_sport = sport
                        return

def select_difficulty():
    global current_difficulty, current_quiz
    while True:
        screen.fill(WHITE)
        draw_text(f"Select {current_sport} Difficulty", font, BLACK, WIDTH // 2, 100)
        
        for i, difficulty in enumerate(difficulties):
            draw_button(difficulty, 250, 200 + i * 100, 300, 75, GREEN)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, difficulty in enumerate(difficulties):
                    button_rect = pygame.Rect(250, 200 + i * 100, 300, 75)
                    if button_rect.collidepoint(mouse_pos):
                        current_difficulty = difficulty
                        current_quiz = load_quiz(current_sport.lower(), difficulty.lower())
                        return

def quiz_game():
    global current_question, score, wrong_answers
    current_question = 0
    score = 0
    wrong_answers = []
    
    while current_question < len(current_quiz["questions"]):
        screen.fill(WHITE)
        question = current_quiz["questions"][current_question]
        
        draw_text(question["question"], font, BLACK, WIDTH // 2, 100)
        
        for i, option in enumerate(question["options"]):
            draw_button(option, 50, 200 + i * 75, 700, 50, BLUE)
        
        draw_text(f"Question {current_question + 1}/{len(current_quiz['questions'])}", small_font, BLACK, WIDTH - 100, 50)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i in range(4):
                    button_rect = pygame.Rect(50, 200 + i * 75, 700, 50)
                    if button_rect.collidepoint(mouse_pos):
                        if i == question["correctAnswer"]:
                            score += 1
                        else:
                            wrong_answers.append((question["question"], question["options"][i], question["options"][question["correctAnswer"]], question["explanation"]))
                        current_question += 1

def results_screen():
    while True:
        screen.fill(WHITE)
        draw_text(f"Quiz Complete! Your score: {score}/{len(current_quiz['questions'])}", font, BLACK, WIDTH // 2, 50)
        
        y_offset = 100
        for i, (question, wrong_answer, correct_answer, explanation) in enumerate(wrong_answers):
            draw_text(f"Q{i+1}: {question}", small_font, BLACK, WIDTH // 2, y_offset)
            draw_text(f"Your answer: {wrong_answer}", small_font, RED, WIDTH // 2, y_offset + 30)
            draw_text(f"Correct answer: {correct_answer}", small_font, GREEN, WIDTH // 2, y_offset + 60)
            words = explanation.split()
            lines = [words[i:i+10] for i in range(0, len(words), 10)]
            for j, line in enumerate(lines):
                draw_text(" ".join(line), small_font, BLUE, WIDTH // 2, y_offset + 90 + j * 30)
            y_offset += 180
        
        draw_button("Main Menu", WIDTH // 2 - 100, HEIGHT - 100, 200, 50, GREEN)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 100, 200, 50)
                if button_rect.collidepoint(mouse_pos):
                    return

# Game loop
splash_screen()
while True:
    if main_menu() == "start":
        select_sport()
        select_difficulty()
        quiz_game()
        results_screen()