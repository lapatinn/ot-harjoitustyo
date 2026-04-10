import pygame


class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # self.surface = pygame.Surface((50, 50))
        self.surface = pygame.image.load("src/assets/portal.bmp")
        # self.surface.fill((0, 255, 0))
        self.rect = self.surface.get_rect(midbottom=(x, y))
