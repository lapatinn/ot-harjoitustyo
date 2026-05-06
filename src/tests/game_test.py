import unittest
from unittest.mock import MagicMock, patch
import pygame
from game import init_game, game_loop
from level import Level
from event_handler import GameEventHandler


class TestGame(unittest.TestCase):
    def test_init_game_returns_objects(self):
        level, game_events, all_sprites, platforms = init_game()

        self.assertIsInstance(level, Level)
        self.assertIsInstance(game_events, GameEventHandler)
        self.assertIsInstance(all_sprites, pygame.sprite.Group)
        self.assertIsInstance(platforms, pygame.sprite.Group)

    @patch("pygame.event.get")
    def test_game_loop_returns_victory_when_rocket(self, mock_event_q):
        mock_event = MagicMock()
        mock_event_q.return_value = [mock_event]

        mock_level = MagicMock()
        mock_level.get_groups.return_value = (MagicMock(), MagicMock())
        mock_level.check_portal.return_value = False
        mock_level.check_rocket.return_value = True

        rocket = game_loop(MagicMock(), pygame.sprite.Group(),
                           pygame.sprite.Group(), mock_level, GameEventHandler())

        self.assertEqual(rocket, "victory")
