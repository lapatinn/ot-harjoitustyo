import sys
import pygame
from sprites.player import Player


class GameEventHandler:
    """Class for handling user inputs (events) in game loop. 
    
    Attributes:
        player: Entity of Player-class, needed for movement. 
        platforms: Group of Platform-entities, needed for collision detection in jumping.
    """

    def __init__(self, player=Player, platforms=pygame.sprite.Group):
        self.player = player
        self.platforms = platforms

    def handle_events(self):
        """Method for handling user inputs, called in gameloop."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump(self.platforms)
                if event.key == pygame.K_a:
                    self.player.change_direction("left")
                if event.key == pygame.K_d:
                    self.player.change_direction("right")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.player.cancel_jump()
                if event.key == pygame.K_a:
                    self.player.change_direction("cancel_left")
                if event.key == pygame.K_d:
                    self.player.change_direction("cancel_right")

    def update_platforms(self, platforms=pygame.sprite.Group):
        """Method for updating platform positions once new level is loaded."""

        self.platforms = platforms


class MenuEventHandler:
    """Class for handling user inputs (events) in menu loop.
    
    Attributes:
        bottom_text: Bottom text drawn in menu, deetermined in main game loop. 
        bottom_text_rect: Rect object of bottom text for collision detection.
    """

    def handle_events(self, bottom_text=str, bottom_text_rect=pygame.Rect):
        """Method for handling user inputs, called in menuloop.
        
        Returns:
            "menu" if "Main menu" button clicked. 
            "game if "Play" or "Try again" clicked.
            """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if bottom_text_rect.collidepoint(event.pos):
                        if bottom_text == "Main menu":
                            return "menu"
                        if bottom_text == "Play":
                            return "game"
                        if bottom_text == "Try again":
                            return "game"

    def is_hovering(self, bt_x, bt_y, bt_w, bt_h):
        """Checks mouse hover over button.

        Returns:
            True if hovering, otherwise False."""

        m_x, m_y = pygame.mouse.get_pos()
        return bool(bt_x <= m_x <= bt_x + bt_w and bt_y <= m_y <= bt_y + bt_h)
