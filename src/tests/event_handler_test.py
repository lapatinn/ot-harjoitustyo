import unittest
from unittest.mock import MagicMock, patch
import pygame
from event_handler import GameEventHandler, MenuEventHandler
from sprites.player import Player
from sprites.platforms import Floor


class TestGameEventHandler(unittest.TestCase):
    def setUp(self):
        self.mock_player = MagicMock(Player)
        self.eh = GameEventHandler(self.mock_player, pygame.sprite.Group())

    def test_init(self):
        eh = GameEventHandler(Player(), pygame.sprite.Group())
        self.assertIsInstance(eh.player, Player)
        self.assertIsInstance(eh.platforms, pygame.sprite.Group)

    def test_update_platforms_changes_variable(self):
        self.eh2 = GameEventHandler(Player(), list())
        newplatforms = pygame.sprite.Group()
        self.eh2.update_platforms(newplatforms)
        self.assertIsInstance(self.eh2.platforms, pygame.sprite.Group)

    @patch("pygame.event.get")
    @patch("sys.exit")
    def test_quit_event_quits_game(self, mock_sys_exit, mock_event_q):
        mock_event = MagicMock()
        mock_event.type = pygame.QUIT
        mock_event_q.return_value = [mock_event]

        self.eh.handle_events()

        mock_sys_exit.assert_called()

    @patch("pygame.event.get")
    def test_space_calls_jump(self, mock_event_q):
        mock_event = MagicMock()
        mock_event.type = pygame.KEYDOWN
        mock_event.key = pygame.K_SPACE
        mock_event_q.return_value = [mock_event]

        self.eh.handle_events()

        self.eh.player.jump.assert_called()

    @patch("pygame.event.get")
    def test_keyup_space_calls_cancel_jump(self, mock_event_q):
        mock_event = MagicMock()
        mock_event.type = pygame.KEYUP
        mock_event.key = pygame.K_SPACE
        mock_event_q.return_value = [mock_event]

        self.eh.handle_events()

        self.eh.player.cancel_jump.assert_called()

    @patch("pygame.event.get")
    def test_a_calls_change_direction(self, mock_event_q):
        mock_event = MagicMock()
        mock_event.type = pygame.KEYDOWN
        mock_event.key = pygame.K_a
        mock_event_q.return_value = [mock_event]

        self.eh.handle_events()

        self.eh.player.change_direction.assert_called_with("left")

    @patch("pygame.event.get")
    def test_d_calls_change_direction(self, mock_event_q):
        mock_event = MagicMock()
        mock_event.type = pygame.KEYDOWN
        mock_event.key = pygame.K_d
        mock_event_q.return_value = [mock_event]

        self.eh.handle_events()

        self.eh.player.change_direction.assert_called_with("right")

    @patch("pygame.event.get")
    def test_keyup_a_calls_change_direction(self, mock_event_q):
        mock_event = MagicMock()
        mock_event.type = pygame.KEYUP
        mock_event.key = pygame.K_a
        mock_event_q.return_value = [mock_event]

        self.eh.handle_events()

        self.eh.player.change_direction.assert_called_with("cancel_left")

    @patch("pygame.event.get")
    def test_keyup_d_calls_change_direction(self, mock_event_q):
        mock_event = MagicMock()
        mock_event.type = pygame.KEYUP
        mock_event.key = pygame.K_d
        mock_event_q.return_value = [mock_event]

        self.eh.handle_events()

        self.eh.player.change_direction.assert_called_with("cancel_right")


class TestMenuEventHandler(unittest.TestCase):
    def setUp(self):
        self.eh = MenuEventHandler()

    @patch("pygame.event.get")
    @patch("sys.exit")
    def test_quit_calls_exit(self, mock_sys_exit, mock_event_q):
        mock_event = MagicMock()
        mock_event.type = pygame.QUIT
        mock_event_q.return_value = [mock_event]

        self.eh.handle_events()

        mock_sys_exit.assert_called()

    @patch("pygame.event.get")
    def test_mouse_click_returns_menu_when_on_victory_screen(self, mock_event_q):
        mock_event = MagicMock()
        mock_event.type = pygame.MOUSEBUTTONDOWN
        mock_event_q.return_value = [mock_event]
        mock_event.button = 1

        mock_rect = MagicMock()
        mock_rect.collidepoint.return_value = True

        self.assertEqual(self.eh.handle_events("Main menu", mock_rect), "menu")

    @patch("pygame.event.get")
    def test_mouse_click_returns_game_when_dead(self, mock_event_q):
        mock_event = MagicMock()
        mock_event.type = pygame.MOUSEBUTTONDOWN
        mock_event_q.return_value = [mock_event]
        mock_event.button = 1

        mock_rect = MagicMock()
        mock_rect.collidepoint.return_value = True

        self.assertEqual(self.eh.handle_events("Try again", mock_rect), "game")

    @patch("pygame.event.get")
    def test_mouse_click_returns_game_when_in_main_menu(self, mock_event_q):
        mock_event = MagicMock()
        mock_event.type = pygame.MOUSEBUTTONDOWN
        mock_event_q.return_value = [mock_event]
        mock_event.button = 1

        mock_rect = MagicMock()
        mock_rect.collidepoint.return_value = True

        self.assertEqual(self.eh.handle_events("Play", mock_rect), "game")

    @patch("pygame.event.get")
    def test_mouse_click_returns_only_when_collide(self, mock_event_q):
        mock_event = MagicMock()
        mock_event.type = pygame.MOUSEBUTTONDOWN
        mock_event_q.return_value = [mock_event]
        mock_event.button = 1

        mock_rect = MagicMock()
        mock_rect.collidepoint.return_value = False

        self.assertEqual(self.eh.handle_events("Play", mock_rect), None)

    @patch("pygame.event.get")
    def test_mouse_click_returns_only_when_left_click(self, mock_event_q):
        mock_event = MagicMock()
        mock_event.type = pygame.MOUSEBUTTONDOWN
        mock_event_q.return_value = [mock_event]
        mock_event.button = 2

        mock_rect = MagicMock()
        mock_rect.collidepoint.return_value = True

        self.assertEqual(self.eh.handle_events("Play", mock_rect), None)

    @patch("pygame.event.get")
    def test_mouse_click_returns_only_when_correct_bottom_text(self, mock_event_q):
        mock_event = MagicMock()
        mock_event.type = pygame.MOUSEBUTTONDOWN
        mock_event_q.return_value = [mock_event]
        mock_event.button = 1

        mock_rect = MagicMock()
        mock_rect.collidepoint.return_value = True

        self.assertEqual(self.eh.handle_events(
            "Incorrect text", mock_rect), None)

    @patch("pygame.mouse.get_pos")
    def test_is_hovering_returns_correct_value(self, mock_mouse):
        mock_pos = 10, 10
        mock_mouse.return_value = mock_pos

        hover = self.eh.is_hovering(5, 5, 6, 6)

        self.assertTrue(hover)
