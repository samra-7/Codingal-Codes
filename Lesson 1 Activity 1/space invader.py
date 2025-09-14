import math
import random
import pygame

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_MIN_Y = 50
ENEMY_START_MAX_Y = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED = 10
COLLISION_DISTANCE = 27

# Initialize Pygame
pygame.init()

# Create Game Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load Game Icon
try:
    icon = pygame.image.load("ufo.png")
    pygame.display.set_icon(icon)
except FileNotFoundError:
    print("⚠️ Warning: 'ufo.png' not found. Using default icon.")

# Load Background Image
try:
    background = pygame.image.load("background.png")  # <-- Replace with your background image filename
except FileNotFoundError:
    background = None
    print("⚠️ Warning: 'background.jpg' not found. Background will be blank.")

running = True
while running:
    # Draw background
    if background:
        screen.blit(background, (0, 0))  # Draw at top-left corner
    else:
        screen.fill((0, 0, 0))  # Fallback: fill screen black if no background

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
