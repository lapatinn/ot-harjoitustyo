import pygame
from pygame.locals import *
from config import SCREEN_HEIGHT, SCREEN_WIDTH

pygame.init()


class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface((SCREEN_WIDTH, 50))
        self.surface.fill((140, 140, 140))
        self.rect = self.surface.get_rect(
            center=(SCREEN_WIDTH//2, SCREEN_HEIGHT))


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.surface = pygame.image.load("src/assets/platform.bmp")
        self.rect = self.surface.get_rect(center=(self.pos_x, self.pos_y))
