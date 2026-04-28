import pygame
from config import SCREEN_HEIGHT, SCREEN_WIDTH

pygame.init()


class Floor(pygame.sprite.Sprite):
    """Class for floor platform.
    
    Attributes:
        surface: Pygame surface.
        rect: Rect object for surface."""

    def __init__(self):
        """Class constructor, creates surface."""

        super().__init__()
        self.surface = pygame.Surface((SCREEN_WIDTH, 30))
        self.surface.fill((140, 140, 140))
        self.rect = self.surface.get_rect(
            midbottom=(SCREEN_WIDTH//2, SCREEN_HEIGHT))


class Platform(pygame.sprite.Sprite):
    """Class for floating platforms.
    
    Attributes:
        pos_x: X coordinate of platform.
        pos_y: Y coordinate of platform."""

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.surface = pygame.image.load("src/assets/platform.bmp")
        self.rect = self.surface.get_rect(center=(self.pos_x, self.pos_y))
