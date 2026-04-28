import pygame


class Rocket(pygame.sprite.Sprite):
    """Class of rocket, used to win game."""

    def __init__(self, x, y):
        super().__init__()
        self.surface = pygame.image.load("src/assets/rocket.bmp")
        self.rect = self.surface.get_rect(midbottom=(x, y))
