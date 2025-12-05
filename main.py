import sys
import pygame
from pygame.sprite import Group
import game_functions as gf
from game_functions import Settings
from game_functions import Ship
from game_functions import GameStats
from game_functions import Button
from scoreboard import Scoreboard
import random


def run_game():
    pygame.init()
    pygame.display.set_caption('Space Invader')

    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))

    # set bg image and smoothscale it
    background = pygame.image.load("images/bg.png")
    background = pygame.transform.smoothscale(background, (ai_setting.screen_width, ai_setting.screen_height))

    # create a ship
    ship = Ship(screen, ai_setting)

    # create group for aliens and bullets
    aliens = Group()
    alien_bullets = Group()

    # save game statistics data
    stats = GameStats(ai_setting)

    # place a button at the beginning
    play_button = Button(ai_setting, screen, 'Play')

    # show score
    sb = Scoreboard(ai_setting, screen, stats)

    gf.create_fleet(ai_setting, screen, aliens, ship)
    screen.fill((0, 0, 0))
    while True:
        screen.blit(background, (0, 0))

        gf.check_events(ai_setting, screen, ship, alien_bullets, aliens, stats, play_button, sb)
        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_setting, stats, screen, aliens, ship, sb, alien_bullets)
        else:
            if stats.ships_left == 0:
                game_over_font = pygame.font.Font(None, 100)
                game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))

                # center horizontally, near the top
                x = ai_setting.screen_width // 2 - game_over_text.get_width() // 2
                # middle of screen
                y = 400
                screen.blit(game_over_text, (x, y))
        gf.update_screen(screen, ship, aliens, alien_bullets, stats, play_button, sb )

        # save score in a text file
        with open('score.txt', 'w') as f:
            f.write(str(stats.score))
        pygame.display.update()

run_game()
