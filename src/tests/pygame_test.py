import unittest
import pygame
from main import draw_text


class TestPygame(unittest.TestCase):
    def setUp(self):
        self.text = "Testing"
        self.font = pygame.font.SysFont("arialblack", 50)
        self.color = (255, 255, 255)
        self.x = 640
        self.y = 320

    def test_draw_text_returns_rect(self):
        test_rect = draw_text(
            self.text, self.font, self.color, self.x, self.y)
        self.assertIsInstance(test_rect, pygame.Rect)
