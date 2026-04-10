import pygame
import json
from sprites.player import Player
from sprites.platforms import Platform, Floor
from sprites.portal import Portal


class Level:
    def __init__(self, level_id=int):
        self.level_id = level_id
        self.player = Player()
        self.floor = Floor()
        self.platforms = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.portal = pygame.sprite.Group()

        self.all_sprites.add(
            self.player,
            self.floor
        )

        self.platforms.add(self.floor)

    def generate(self):
        level_data = self.get_level_data()

        for dict in level_data["platforms"]:

            x = dict["plat_x"]
            y = dict["plat_y"]

            platform = Platform(x, y)
            self.platforms.add(platform)
            self.all_sprites.add(platform)

        portal = Portal(level_data["portal"]["portal_x"],
                        level_data["portal"]["portal_y"])
        self.all_sprites.add(portal)
        self.portal.add(portal)

    def get_groups(self):
        return self.all_sprites, self.platforms

    def get_level_data(self):
        f = open(f"src/levels/level_{str(self.level_id)}.json")
        level_data = json.load(f)

        return level_data

    def check_portal(self):
        collisions = pygame.sprite.spritecollide(
            self.player, self.portal, True)

        if self.level_id == 1:
            if collisions:
                self.level_id = 2
                self.clear_groups()
                self.generate()
                self.player.reset_pos()
                return True

        elif self.level_id == 2:
            if collisions:
                self.level_id = 1
                self.clear_groups()
                self.generate()
                self.player.reset_pos()
                return True

    def clear_groups(self):
        self.all_sprites.empty()
        self.all_sprites.add(
            self.player,
            self.floor
        )

        self.platforms.empty()
        self.platforms.add(self.floor)

        self.portal.empty()
