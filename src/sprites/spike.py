import pygame


class Spike(pygame.sprite.Sprite):
    """Class of spike, used for damaging player."""

    def __init__(self, x, y):
        super().__init__()
        self.surface = pygame.image.load("src/assets/spike.bmp")
        self.rect = self.surface.get_rect(midbottom=(x, y))
