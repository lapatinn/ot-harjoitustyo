from config import HEALTH_FONT, HEALTH_COLOR, SCREEN_WIDTH


def draw_text(window, text, font, text_color, x, y):
    """Draws text on screen.
    
    Args:
        window: Pygame window onto which text is to be drawn.
        text: String to be drawn.
        font: Pygame font object, determines font.
        text_color: RBG value for text.
        x: X coordinate of text to be drawn.
        y: Y coordinate of text to be drawn."""

    img = font.render(text, True, text_color)
    window.blit(img, (x, y))
    return img.get_rect(topleft=(x, y))


def draw_health(window, text):
    """Draws player health.
    
    Args:
        window: Pygame window onto which player health is to be drawn.
        text: Player health."""

    img = HEALTH_FONT.render(text, True, HEALTH_COLOR)
    x = 0.1 * img.get_width()
    y = 0.7 * img.get_height()

    window.blit(img, (x, y))
    return img.get_rect(topleft=(x, y))


def draw_level_id(window, text):
    """Draws current level id.
    
    Args:
        window: Pygame window onto which level id is to be drawn.
        text: Level id"""

    text = f"Level: {text}"
    img = HEALTH_FONT.render(text, True, HEALTH_COLOR)
    x = SCREEN_WIDTH - img.get_width() * 1.2
    y = 0.7 * img.get_height()

    window.blit(img, (x, y))
    return img.get_rect(topleft=(x, y))
