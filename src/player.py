import pygame
from pygame.locals import *
from config import SCREEN_WIDTH, SCREEN_HEIGHT, ACC, FRIC, JUMP_FORCE

pygame.init()
vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.image.load("src/sprites/player.png")
        self.rect = self.surface.get_rect(
            center=(SCREEN_WIDTH//2, SCREEN_HEIGHT - 50))

        self.pos = vec((SCREEN_WIDTH//2, 0))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.dir = None

    def move(self):
        self.acc = vec(0, 0.5)

        if self.dir == "left":
            self.acc.x = -ACC
        if self.dir == "right":
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.pos.x = max(self.pos.x, 0)
        self.pos.x = min(self.pos.x, SCREEN_WIDTH)

        self.rect.midbottom = self.pos
        self.dir = None

    def check_floor_collision(self, group):
        collisions = pygame.sprite.spritecollide(self, group, False)
        if collisions:
            self.pos.y = collisions[0].rect.top + 1
            self.vel.y = 0

    def jump(self, group):
        collisions = pygame.sprite.spritecollide(self, group, False)
        if collisions:
            self.vel.y = -JUMP_FORCE
