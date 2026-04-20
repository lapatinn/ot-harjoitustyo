import unittest
from unittest.mock import patch, MagicMock
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

    @patch("pygame.sprite.spritecollide")
    def test_check_portal_triggers_level_2(self, mock_spritecollide):
        mock_collision = MagicMock()
        mock_spritecollide.return_value = [mock_collision]

        self.assertTrue(self.level.check_portal())
        self.assertEqual(self.level.level_id, 2)

    @patch("pygame.sprite.spritecollide")
    def test_check_portal_triggers_level_1(self, mock_spritecollide):
        self.level = Level(2)
        mock_collision = MagicMock()
        mock_spritecollide.return_value = [mock_collision]

        self.assertTrue(self.level.check_portal())
        self.assertEqual(self.level.level_id, 3)

    @patch("pygame.sprite.spritecollide")
    def test_check_portal_doesnt_trigger_level_2_if_no_collision(self, mock_spritecollide):
        self.level = Level(1)
        mock_collision = MagicMock()
        mock_spritecollide.return_value = None

        self.assertFalse(self.level.check_portal())
        self.assertEqual(self.level.level_id, 1)

    @patch("pygame.sprite.spritecollide")
    def test_check_portal_doesnt_trigger_level_1_if_no_collision(self, mock_spritecollide):
        self.level = Level(2)
        mock_collision = MagicMock()
        mock_spritecollide.return_value = None

        self.assertFalse(self.level.check_portal())
        self.assertEqual(self.level.level_id, 2)

    @patch("pygame.sprite.spritecollide")
    def test_check_portal_doesnt_trigger_if_level_doesnt_exist_and_collisions(self, mock_spritecollide):
        self.level = Level(3)
        mock_collision = MagicMock()
        mock_spritecollide.return_value = [mock_collision]

        self.assertFalse(self.level.check_portal())
        self.assertEqual(self.level.level_id, 3)

    @patch("pygame.sprite.spritecollide")
    def test_check_portal_doesnt_trigger_if_level_doesnt_exist_and_no_collisions(self, mock_spritecollide):
        self.level = Level(3)
        mock_collision = MagicMock()
        mock_spritecollide.return_value = None

        self.assertFalse(self.level.check_portal())
        self.assertEqual(self.level.level_id, 3)
