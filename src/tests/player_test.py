import unittest
from player import Player
from config import ACC, SCREEN_WIDTH


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()

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
