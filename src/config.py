import pygame
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
ACC = 1
FRIC = -0.12
JUMP_FORCE = 15

TOP_FONT = pygame.font.SysFont("arialblack", 70)
BOTTOM_FONT = pygame.font.SysFont("arialblack", 60)
TOP_COLOR = (255, 255, 255)
BOTTOM_COLOR = (213, 216, 53)

HEALTH_FONT = pygame.font.SysFont("arialblack", 40)
HEALTH_COLOR = (190, 0, 0)

LEVEL_COUNT = 5
