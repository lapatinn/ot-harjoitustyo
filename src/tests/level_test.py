import pygame
import json
import unittest
from unittest.mock import Mock, ANY
from sprites.platforms import Platform, Floor
from sprites.player import Player
from sprites.portal import Portal
from level import Level


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(1)

    def test_init_creates_correct_level(self):
        level2 = Level(2)
        self.assertEqual(level2.level_id, 2)

    def test_get_level_data_returns_dict(self):
        data = self.level.get_level_data()

        self.assertIsInstance(data, dict)

    def test_generate_group_size_all_sprites(self):
        self.level.generate()

        all_sprites, platforms = self.level.get_groups()

        self.assertEqual(len(all_sprites.sprites()), 7)
    
    def test_generate_group_size_platforms(self):
        self.level.generate()

        all_sprites, platforms = self.level.get_groups()

        self.assertEqual(len(platforms.sprites()), 5)

    def test_clear_groups_clears_groups(self):
        self.level.generate()
        all_sprites, platforms = self.level.get_groups()

        self.assertEqual(len(all_sprites.sprites()), 7)
        self.assertEqual(len(platforms.sprites()), 5)

        self.level.clear_groups()

        self.assertEqual(len(all_sprites.sprites()), 2)
        self.assertEqual(len(platforms.sprites()), 1)

