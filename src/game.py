import pygame
from config import (SCREEN_WIDTH, SCREEN_HEIGHT, TOP_FONT,
                    TOP_COLOR, BOTTOM_FONT, BOTTOM_COLOR)
from text_renderer import draw_text, draw_health, draw_level_id
from event_handler import MenuEventHandler, GameEventHandler
from level import Level


def init_menu():
    return MenuEventHandler(), "menu"


def init_game():
    level = Level(1)
    level.generate()

    all_sprites, platforms = level.get_groups()

    game_events = GameEventHandler(level.player, platforms)

    return level, game_events, all_sprites, platforms


def menu_loop(window,
              menu_events=MenuEventHandler,
              top_text=str,
              bottom_text=str):

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
              top_text_x,
              top_text_y)

    bottom_text_color = TOP_COLOR if menu_events.is_hovering(bottom_text_x,
                                                             bottom_text_y,
                                                             bottom_text_width,
                                                             bottom_text_height,) else BOTTOM_COLOR

    bottom_text_rect = draw_text(window,
                                 bottom_text,
                                 BOTTOM_FONT,
                                 bottom_text_color,
                                 bottom_text_x,
                                 bottom_text_y)

    return menu_events.handle_events(bottom_text, bottom_text_rect)


def game_loop(window,
              all_sprites=pygame.sprite.Group,
              platforms=pygame.sprite.Group,
              level=Level,
              game_events=GameEventHandler):

    window.fill((0, 0, 40))

    game_events.handle_events()

    level.player.move()
    level.player.check_floor_collision(platforms)

    portal_used = level.check_portal()
    if portal_used:
        all_sprites, platforms = level.get_groups()
        game_events.update_platforms(platforms)

    rocket_used = level.check_rocket()
    if rocket_used:
        return "victory"

    player_dead = level.check_damage()
    if player_dead:
        return "death"

    for entity in all_sprites:
        window.blit(entity.surface, entity.rect)

    draw_health(window, level.player.get_health_str())
    draw_level_id(window, str(level.level_id))
