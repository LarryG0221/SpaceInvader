import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Space Invader")

# Load background image
# Make sure you have 'space.png' in the same folder
background = pygame.image.load("bg.jpg")

# Game loop
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    # Draw background
    screen.blit(background, (0, 0))

    # Update display
    pygame.display.update()

pygame.quit()
sys.exit()
