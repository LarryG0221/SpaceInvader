
import pygame.font
from pygame.sprite import Group

from game_functions import Ship

# show score on screen
class Scoreboard(object):

  def __init__(self, ai_setting, screen, stats):
    self.ai_setting = ai_setting
    self.screen = screen
    self.screen_rect = screen.get_rect()
    self.stats = stats
    # text color
    self.text_color = (230, 130, 30)
    self.font = pygame.font.SysFont(None, 48)
    # prepare score image
    self.prep_score()
    self.prep_lives()

  def prep_score(self):
    rounded_score = round(self.stats.score, -1)
    score_str = "Score : {}".format(rounded_score)

    self.font = pygame.font.Font(None, 34)  # default font, size 40
    self.score_image = self.font.render(score_str, True, (0, 0, 205))
    self.score_rect = self.score_image.get_rect()
    self.score_rect.right = self.screen_rect.right - 220
    self.score_rect.top = 20

  def show_score(self):
    self.screen.blit(self.score_image, self.score_rect)

  def prep_lives(self):
    lives_left = self.stats.ships_left
    lives_str = "LIVES : {}".format(lives_left)
    self.font = pygame.font.Font(None, 34)  # default font, size 40
    self.lives_image = self.font.render(lives_str, True, (0, 0, 205))
    self.lives_rect = self.lives_image.get_rect()
    self.lives_rect.centerx = self.screen_rect.centerx
    self.lives_rect.top = self.score_rect.top

  def show_lives(self):
    self.screen.blit(self.lives_image, self.lives_rect)

  def prep_elapsed_time(self):
      elapsed_time_ms = pygame.time.get_ticks() - self.stats.start_time  # Time in milliseconds
      elapsed_seconds = elapsed_time_ms // 1000  # Convert to seconds
      minutes = elapsed_seconds // 60  # Get minutes
      seconds = elapsed_seconds % 60  # Get seconds
      # 500 max score if player holds on 3 mins
      if elapsed_seconds > 180:
          self.stats.score = 500
          self.stats.result = 'win'

      elapsed_time_str = f"Time : {minutes:02}:{seconds:02}"
      self.font = pygame.font.Font(None, 34)  # default font, size 40
      self.elapsed_time_image = self.font.render(elapsed_time_str, True, (0,0,205))
      self.elapsed_time_rect = self.elapsed_time_image.get_rect()
      self.elapsed_time_rect.top = 20
      self.elapsed_time_rect.left = 260  # Position it on the left side of the screen

  def show_elapsed_time(self):
      self.screen.blit(self.elapsed_time_image, self.elapsed_time_rect)
