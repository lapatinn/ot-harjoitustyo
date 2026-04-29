import unittest
import pygame
from text_renderer import draw_text


class TestPygame(unittest.TestCase):
    def setUp(self):
        self.text = "Testing"
        self.font = pygame.font.SysFont("arialblack", 50)
        self.color = (255, 255, 255)
        self.x = 640
        self.y = 320

    def test_draw_text_returns_rect(self):
        window = pygame.display.set_mode((1280, 720))
        test_rect = draw_text(
            window, self.text, self.font, self.color, self.x, self.y)
        self.assertIsInstance(test_rect, pygame.Rect)
