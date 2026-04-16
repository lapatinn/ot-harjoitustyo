import unittest
from unittest.mock import patch, MagicMock
import pygame
from sprites.player import Player
from sprites.platforms import Floor


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.floor = Floor()

        self.platforms = pygame.sprite.Group()
        self.platforms.add(self.floor)

        self.ACC, self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1, 1280, 720

    def test_create_player(self):
        self.assertIsInstance(self.player, Player)

    def test_move_left_changes_direction(self):
        self.player.change_direction("left")
        self.player.move()
        self.assertEqual(self.player.acc.x, -self.ACC)

    def test_move_right_changes_direction(self):
        self.player.change_direction("right")
        self.player.move()
        self.assertEqual(self.player.acc.x, self.ACC)

    def test_player_stays_in_bounds_left(self):
        self.player.pos.x = -1
        self.player.move()
        self.assertEqual(self.player.pos.x, 0)

    def test_player_stays_in_bounds_right(self):
        self.player.pos.x = self.SCREEN_WIDTH + 1
        self.player.move()
        self.assertEqual(self.player.pos.x, self.SCREEN_WIDTH)

    def test_no_jump_if_no_collision(self):
        self.player.jump(self.platforms)
        self.assertEqual(self.player.jumping, False)

    @patch("pygame.sprite.spritecollide")
    def test_jump_triggers_on_collision(self, mock_spritecollide):
        self.player.jumping = False

        mock_collision = MagicMock()  
        mock_spritecollide.return_value = [mock_collision]
        group = MagicMock()

        self.player.jump(group)

        self.assertTrue(self.player.jumping)

    @patch("pygame.sprite.spritecollide")
    def test_floor_collision_cancels_jump(self, mock_spritecollide):
        mock_collision = MagicMock()
        mock_collision.rect = MagicMock()
        mock_collision.rect.bottom = 1

        mock_spritecollide.return_value = [mock_collision]
        group = MagicMock()

        self.player.jumping = True
        self.player.vel.y = 1
        self.player.pos.y = 0
        self.player.check_floor_collision(group)

        self.assertFalse(self.player.jumping)
        self.assertEqual(self.player.vel.y, 0)

    @patch("pygame.sprite.spritecollide")
    def test_floor_collision_triggers_when_moving(self, mock_spritecollide):
        mock_collision = MagicMock()
        mock_collision.rect = MagicMock()
        mock_collision.rect.bottom = 1

        mock_spritecollide.return_value = [mock_collision]
        group = MagicMock()

        self.player.jumping = True
        self.player.vel.y = 0
        self.player.pos.y = 0
        self.player.check_floor_collision(group)

        self.assertTrue(self.player.jumping)
        self.assertEqual(self.player.vel.y, 0)

    @patch("pygame.sprite.spritecollide")
    def test_floor_collision_triggers_when_collision(self, mock_spritecollide):
        mock_collision = MagicMock()
        mock_collision.rect = MagicMock()
        mock_collision.rect.bottom = 1

        mock_spritecollide.return_value = None
        group = MagicMock()

        self.player.jumping = True
        self.player.vel.y = 1
        self.player.pos.y = 0
        self.player.check_floor_collision(group)

        self.assertTrue(self.player.jumping)

    @patch("pygame.sprite.spritecollide")
    def test_floor_collision_triggers_when_below_platform(self, mock_spritecollide):
        mock_collision = MagicMock()
        mock_collision.rect = MagicMock()
        mock_collision.rect.bottom = 1

        mock_spritecollide.return_value = [mock_collision]
        group = MagicMock()

        self.player.jumping = True
        self.player.vel.y = 1
        self.player.pos.y = 2
        self.player.check_floor_collision(group)

        self.assertTrue(self.player.jumping)

    def test_cancel_jump_sets_vel(self):
        self.player.jumping = True
        self.player.vel.y = -4
        self.player.cancel_jump()
        self.assertEqual(self.player.vel.y, -3)

    def test_cancel_jump_cancels_if_jumping(self):
        self.player.jumping = False
        self.player.vel.y = -4
        self.player.cancel_jump()
        self.assertEqual(self.player.vel.y, -4)

    def test_cancel_jump_cancels_if_moving(self):
        self.player.jumping = True
        self.player.vel.y = -2
        self.player.cancel_jump()
        self.assertEqual(self.player.vel.y, -2)

    def test_keyup_changes_dir_right(self):
        self.player.moveright = True
        self.player.change_direction("cancel_right")
        self.assertEqual(self.player.moveright, False)

    def test_keyup_changes_dir_left(self):
        self.player.moveleft = True
        self.player.change_direction("cancel_left")
        self.assertEqual(self.player.moveleft, False)

    def test_reset_pos_resets_pos(self):
        vec = pygame.math.Vector2
        self.player.pos = vec((100, 100))
        self.player.reset_pos()
        self.assertEqual(self.player.pos, pygame.math.Vector2(self.SCREEN_WIDTH - self.player.rect.width,
                                                              self.SCREEN_HEIGHT - 30))

