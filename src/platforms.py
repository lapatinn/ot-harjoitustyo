import pygame
from pygame.locals import *
from config import *

pygame.init()


class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface((SCREEN_WIDTH, 50))
        self.surface.fill((255, 0, 0))
        self.rect = self.surface.get_rect(
            center=(SCREEN_WIDTH//2, SCREEN_HEIGHT))


class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        super().__init__()
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color

        self.surface = pygame.surface.Surface((self.width, self.height))
        self.surface.fill(color)
        self.rect = self.surface.get_rect(center=(self.x, self.y))
