import pygame
import json
from sprites.player import Player
from sprites.platforms import Platform, Floor


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

    def generate(self, level_id=int):
        level_data = self.get_level_data(level_id)

        for dict in level_data["platforms"]:
            x = dict["plat_x"]
            y = dict["plat_y"]

            platform = Platform(x, y)
            self.platforms.add(platform)
            self.all_sprites.add(platform)

    def get_groups(self):
        return self.all_sprites, self.platforms
    
    def get_level_data(self, level_id=int):
        f = open(f"src/levels/level_{str(level_id)}.json")
        level_data = json.load(f)

        return level_data