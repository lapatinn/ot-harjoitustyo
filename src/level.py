import json
import pygame
from sprites.player import Player
from sprites.platforms import Platform, Floor
from sprites.portal import Portal
from sprites.rocket import Rocket
from sprites.spike import Spike
from config import LEVEL_COUNT


class Level:
    """Class for loading level data and handling in-game events.

    Attributes:
        level_id: Initial id of level."""

    def __init__(self, level_id=int):
        """Constructor for class. Creates and inits required groups."""

        self.level_id = level_id
        self.player = Player()
        self.floor = Floor()
        self.platforms = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.portal = pygame.sprite.Group()
        self.rocket = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()

        self.all_sprites.add(
            self.player,
            self.floor
        )

        self.platforms.add(self.floor)

    def generate(self):
        """Loads coordinates for platforms, portals, spikes and rocket for given level."""

        level_data = self.get_level_data()

        for dict in level_data["platforms"]:

            x = dict["plat_x"]
            y = dict["plat_y"]

            platform = Platform(x, y)
            self.platforms.add(platform)
            self.all_sprites.add(platform)

        if "portal" in level_data:
            portal = Portal(level_data["portal"]["portal_x"],
                            level_data["portal"]["portal_y"])

            self.all_sprites.add(portal)
            self.portal.add(portal)

        if "rocket" in level_data:
            rocket = Rocket(level_data["rocket"]["rocket_x"],
                            level_data["rocket"]["rocket_y"])

            self.all_sprites.add(rocket)
            self.rocket.add(rocket)

        if "spikes" in level_data:
            for dict in level_data["spikes"]:
                spike = Spike(dict["spike_x"], dict["spike_y"])

                self.spikes.add(spike)
                self.all_sprites.add(spike)

    def get_groups(self):
        """Updates when new level loaded.

        Returns:
            Group of all sprites, group of only platforms."""

        return self.all_sprites, self.platforms

    def get_level_data(self):
        """Reads json file from src/levels.

        Returns:
            level_data: Dict containing coordinates for objects to be loaded into groups."""

        with open(f"src/levels/level_{str(self.level_id)}.json") as f:
            level_data = json.load(f)

        return level_data

    def check_portal(self):
        """Checks collision with portal, which triggers next level.

        Returns:
            True if player collides with portal."""

        collisions = pygame.sprite.spritecollide(
            self.player, self.portal, True)

        if collisions:
            if self.level_id < LEVEL_COUNT:
                self.level_id += 1
                self.clear_groups()
                self.generate()
                self.player.reset_pos()
                return True

    def check_rocket(self):
        """Checks collision with rocket, which triggers victory.

        Returns:
            True if player collides with rocket."""

        collisions = pygame.sprite.spritecollide(
            self.player, self.rocket, True)

        if collisions:
            return True

    def check_damage(self):
        """Checks collision with spike, which triggers damage.

        Returns:
            True if player collides with spike."""

        collisions = pygame.sprite.spritecollide(
            self.player, self.spikes, True)

        if collisions:
            self.player.hit()
            if self.player.health < 1:
                return True

    def clear_groups(self):
        """Clears sprite groups when new level is to be loaded."""

        self.all_sprites.empty()
        self.all_sprites.add(
            self.player,
            self.floor
        )

        self.platforms.empty()
        self.platforms.add(self.floor)

        self.portal.empty()
        self.rocket.empty()
        self.spikes.empty()
