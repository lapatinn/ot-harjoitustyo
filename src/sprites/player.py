import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, ACC, FRIC, JUMP_FORCE

pygame.init()
vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.image.load("src/assets/player.bmp")
        self.rect = self.surface.get_rect(
            midbottom=(SCREEN_WIDTH//2, SCREEN_HEIGHT - 30))

        self.pos = vec((SCREEN_WIDTH - self.rect.width,
                       SCREEN_HEIGHT - 30))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

        self.jumping = False

        self.moveleft = False
        self.moveright = False

        self.health = 3

    def move(self):
        self.acc = vec(0, 0.5)

        if self.moveright:
            self.acc.x = ACC
        if self.moveleft:
            self.acc.x = -ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.pos.x = max(self.pos.x, 0)
        self.pos.x = min(self.pos.x, SCREEN_WIDTH)

        self.rect.midbottom = self.pos

    def check_floor_collision(self, group):
        collisions = pygame.sprite.spritecollide(self, group, False)

        if self.vel.y > 0:
            if collisions:
                if self.pos.y < collisions[0].rect.bottom:
                    self.pos.y = collisions[0].rect.top + 1
                    self.vel.y = 0
                    self.jumping = False
                    self.surface = pygame.image.load("src/assets/player.bmp")

    def jump(self, group):
        collisions = pygame.sprite.spritecollide(self, group, False)
        if collisions and not self.jumping:
            self.jumping = True
            self.vel.y = -JUMP_FORCE
            self.surface = pygame.image.load("src/assets/player2.bmp")

    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def change_direction(self, dir):
        if dir == "left":
            self.moveleft = True
        if dir == "right":
            self.moveright = True
        if dir == "cancel_right":
            self.moveright = False
        if dir == "cancel_left":
            self.moveleft = False

    def reset_pos(self):
        self.pos = vec((SCREEN_WIDTH - self.rect.width,
                       SCREEN_HEIGHT - 30))

    def get_health_str(self):
        string = f"Health: {self.health * "* "}"
        return string

    def hit(self):
        self.health -= 1
