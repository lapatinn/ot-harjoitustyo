from config import HEALTH_FONT, HEALTH_COLOR, SCREEN_WIDTH


def draw_text(window, text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    window.blit(img, (x, y))
    return img.get_rect(topleft=(x, y))


def draw_health(window, text):
    img = HEALTH_FONT.render(text, True, HEALTH_COLOR)
    x = 0.1 * img.get_width()
    y = 0.7 * img.get_height()

    window.blit(img, (x, y))
    return img.get_rect(topleft=(x, y))


def draw_level_id(window, text):
    text = f"Level: {text}"
    img = HEALTH_FONT.render(text, True, HEALTH_COLOR)
    x = SCREEN_WIDTH - img.get_width() * 1.2
    y = 0.7 * img.get_height()

    window.blit(img, (x, y))
    return img.get_rect(topleft=(x, y))
