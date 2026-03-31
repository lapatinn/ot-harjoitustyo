import pygame
from pygame.locals import *
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
ACC = 1
FRIC = -0.12
JUMP_FORCE = 15

WELCOME_FONT = pygame.font.SysFont("arialblack", 50)
PLAY_FONT = pygame.font.SysFont("arialblack", 60)
WELCOME_COLOR = (255, 255, 255)
PLAY_COLOR = (213, 216, 53)
