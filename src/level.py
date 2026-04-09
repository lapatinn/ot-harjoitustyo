import pygame
import json
from random import randint
from sprites.player import Player
from sprites.platforms import Platform, Floor
from config import SCREEN_HEIGHT, SCREEN_WIDTH


class Level:
    def __init__(self):
        self.player = Player()
        self.floor = Floor()
        self.platforms = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self.all_sprites.add(
            self.player,
            self.floor
        )

        self.platforms.add(self.floor)

    def generate(self):
        f = open("src/levels/level_1.json")
        plat_data = json.load(f)

        for dict in plat_data["platforms"]:
            x = dict["plat_x"]
            y = dict["plat_y"]

            platform = Platform(x, y)
            self.platforms.add(platform)
            self.all_sprites.add(platform)

    def get_groups(self):
        return self.all_sprites, self.platforms