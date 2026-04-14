import unittest
import pygame
from sprites.player import Player
from sprites.platforms import Floor
from config import ACC, SCREEN_WIDTH, SCREEN_HEIGHT


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.floor = Floor()

        self.platforms = pygame.sprite.Group()
        self.platforms.add(self.floor)

    def test_create_player(self):
        self.assertIsInstance(self.player, Player)

    def test_move_left_changes_direction(self):
        self.player.change_direction("left")
        self.player.move()
        self.assertEqual(self.player.acc.x, -ACC)

    def test_move_right_changes_direction(self):
        self.player.change_direction("right")
        self.player.move()
        self.assertEqual(self.player.acc.x, ACC)

    def test_player_stays_in_bounds_left(self):
        self.player.pos.x = -1
        self.player.move()
        self.assertEqual(self.player.pos.x, 0)

    def test_player_stays_in_bounds_right(self):
        self.player.pos.x = SCREEN_WIDTH + 1
        self.player.move()
        self.assertEqual(self.player.pos.x, SCREEN_WIDTH)

    def test_jump_only_if_collide(self):
        self.player.jump(self.platforms)
        self.assertEqual(self.player.jumping, False)

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
        self.assertEqual(self.player.pos, pygame.math.Vector2(SCREEN_WIDTH - self.player.rect.width,
                                                              SCREEN_HEIGHT - 30))
