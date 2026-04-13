import unittest
from unittest.mock import Mock, ANY
import pygame
from event_handler import GameEventHandler
from sprites.player import Player
from sprites.platforms import Floor
from config import ACC, SCREEN_WIDTH, SCREEN_HEIGHT

class TestEventHandler(unittest.TestCase):
    def setUp(self):
        pygame.init()
        pygame.display.set_mode((100,100))
        pygame.event.clear()

        self.eh = GameEventHandler(Player(), pygame.sprite.Group())

    def test_init(self):
        self.assertIsInstance(self.eh.player, Player)
        self.assertIsInstance(self.eh.platforms, pygame.sprite.Group)

    def test_update_platforms_changes_variable(self):
        self.eh2 = GameEventHandler(Player(), list())
        newplatforms = pygame.sprite.Group()
        self.eh2.update_platforms(newplatforms)
        self.assertIsInstance(self.eh2.platforms, pygame.sprite.Group)

    def test_event_queue(self):
        player_mock = Mock(wraps=Player())
        self.eh2 = GameEventHandler(player_mock, pygame.sprite.Group())

        self.eh2.handle_events()
        space = pygame.event.Event(pygame.KEYDOWN, {
            "key": pygame.K_SPACE,
            "mod": 0,
            "unicode": " "
        })
        pygame.event.post(space)

        self.eh2.handle_events()
        player_mock.jump.assert_called_with(ANY, ANY, ANY)
