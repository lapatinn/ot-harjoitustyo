import pygame


class Rocket(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.surface = pygame.surface.Surface((50,50))
        self.surface.fill((255,0,0))
        self.rect = self.surface.get_rect(midbottom=(x, y))