from config import (SCREEN_WIDTH, SCREEN_HEIGHT, TOP_FONT,
                    TOP_COLOR, BOTTOM_FONT, BOTTOM_COLOR)
from text_renderer import draw_text
from event_handler import MenuEventHandler


def init_menu():
    """Generates required entities for menu.

    Returns:
        MenuEventHandler-entity and inital gamestate"""

    return MenuEventHandler(), "menu"


def menu_loop(window,
              menu_events=MenuEventHandler,
              top_text=str,
              bottom_text=str):
    """Main menu loop function. Draws text and handles inputs.

    Args:
        window: Pygame window object.
        menu_events: MenuEventHandler-object.
        top_text: Text to be drawn on top.
        bottom_text: Text to be drawn on bottom.

    Returns:
        None if no inputs, "game" or "menu" if corresponding buttons pressed.
        """

    window.fill((0, 0, 40))

    top_text_width, top_text_height = TOP_FONT.size(top_text)
    bottom_text_width, bottom_text_height = BOTTOM_FONT.size(bottom_text)

    top_text_x = (SCREEN_WIDTH // 2) - (top_text_width // 2)
    top_text_y = 1.5 * top_text_height

    bottom_text_x = (SCREEN_WIDTH // 2) - (bottom_text_width // 2)
    bottom_text_y = (SCREEN_HEIGHT // 2) - (bottom_text_height // 2)

    draw_text(window,
              top_text,
              TOP_FONT,
              TOP_COLOR,
              (top_text_x, top_text_y))

    bottom_text_color = TOP_COLOR if menu_events.is_hovering(bottom_text_x,
                                                             bottom_text_y,
                                                             bottom_text_width,
                                                             bottom_text_height,) else BOTTOM_COLOR

    bottom_text_rect = draw_text(window,
                                 bottom_text,
                                 BOTTOM_FONT,
                                 bottom_text_color,
                                 (bottom_text_x, bottom_text_y))

    return menu_events.handle_events(bottom_text, bottom_text_rect)
