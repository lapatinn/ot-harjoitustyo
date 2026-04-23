import pygame
from config import (BOTTOM_FONT, SCREEN_HEIGHT, SCREEN_WIDTH,
                    FPS, TOP_COLOR, TOP_FONT, BOTTOM_COLOR,
                    HEALTH_FONT, HEALTH_COLOR)
from event_handler import GameEventHandler, MenuEventHandler
from level import Level

pygame.init()
pygame.display.set_caption("Portal Bob")

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    window.blit(img, (x, y))
    return img.get_rect(topleft=(x, y))


def draw_health(text):
    img = HEALTH_FONT.render(text, True, HEALTH_COLOR)
    x = 0.1 * img.get_width()
    y = 0.7 * img.get_height()

    window.blit(img, (x, y))
    return img.get_rect(topleft=(x, y))


def init_game():
    level = Level(5)
    level.generate()

    all_sprites, platforms = level.get_groups()

    game_events = GameEventHandler(level.player, platforms)

    return level, game_events, all_sprites, platforms


def menu_loop(menu_events=MenuEventHandler,
              top_text=str,
              bottom_text=str):

    window.fill((0, 0, 40))

    top_text_width, top_text_height = TOP_FONT.size(top_text)
    bottom_text_width, bottom_text_height = BOTTOM_FONT.size(bottom_text)

    top_text_x = (SCREEN_WIDTH // 2) - (top_text_width // 2)
    top_text_y = 1.5 * top_text_height

    bottom_text_x = (SCREEN_WIDTH // 2) - (bottom_text_width // 2)
    bottom_text_y = (SCREEN_HEIGHT // 2) - (bottom_text_height // 2)

    draw_text(top_text,
              TOP_FONT,
              TOP_COLOR,
              top_text_x,
              top_text_y)

    bottom_text_color = TOP_COLOR if menu_events.is_hovering(bottom_text_x,
                                                             bottom_text_y,
                                                             bottom_text_width,
                                                             bottom_text_height,) else BOTTOM_COLOR

    bottom_text_rect = draw_text(bottom_text,
                                 BOTTOM_FONT,
                                 bottom_text_color,
                                 bottom_text_x,
                                 bottom_text_y)

    return menu_events.handle_events(bottom_text, bottom_text_rect)


def game_loop(all_sprites=pygame.sprite.Group,
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

    draw_health(level.player.get_health_str())


def main():
    clock = pygame.time.Clock()
    game_state = "menu"
    menu_events = MenuEventHandler()

    while True:
        clock.tick(FPS)

        if game_state == "menu":
            res = menu_loop(menu_events, "Main menu", "Play")
            if res == "game":
                level, game_events, all_sprites, platforms = init_game()
                game_state = "game"

        elif game_state == "game":
            res = game_loop(all_sprites, platforms, level, game_events)
            if res == "victory":
                game_state = "victory"
            elif res == "death":
                game_state = "death"

        elif game_state == "victory":
            res = menu_loop(menu_events, "You won!", "Main menu")
            if res == "menu":
                game_state = "menu"

        elif game_state == "death":
            res = menu_loop(menu_events, "You died!", "Try again")
            if res == "game":
                level, game_events, all_sprites, platforms = init_game()
                game_state = "game"

        pygame.display.update()


if __name__ == "__main__":
    main()
