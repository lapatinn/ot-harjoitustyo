import pygame
from config import (PLAY_FONT, SCREEN_HEIGHT, SCREEN_WIDTH,
                    FPS, WELCOME_COLOR, WELCOME_FONT, PLAY_COLOR)
from event_handler import GameEventHandler
from level import Level

pygame.init()
pygame.display.set_caption("Portal Bob")

button_text = "PLAY"
button_width, button_height = PLAY_FONT.size(button_text)
button_x = (SCREEN_WIDTH // 2) - (PLAY_FONT.size(button_text)[0] // 2)
button_y = 200

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    window.blit(img, (x, y))
    return img.get_rect(topleft=(x, y))


def init_game():
    level = Level(3)
    level.generate()

    all_sprites, platforms = level.get_groups()

    game_events = GameEventHandler(level.player, platforms)

    return level, game_events, all_sprites, platforms


def menu_loop(top_text, bottom_text):
    window.fill((50, 0, 0))

    tt_width = WELCOME_FONT.size(top_text)[0]
    bt_width = PLAY_FONT.size(bottom_text)[0]

    draw_text(top_text, WELCOME_FONT,
              WELCOME_COLOR, (SCREEN_WIDTH // 2) - (tt_width // 2), 50)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    is_hovering = (button_x <= mouse_x <= button_x + button_width
                   and button_y <= mouse_y <= button_y + button_height)

    button_color = WELCOME_COLOR if is_hovering else PLAY_COLOR

    play_button_rect = draw_text(bottom_text, PLAY_FONT,
                                 button_color, button_x, button_y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
            exit()
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if play_button_rect.collidepoint(event.pos):
                    if top_text == "VICTORY":
                        return "menu"
                    elif top_text == "Welcome to platfromer game":
                        return "game"


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

    for entity in all_sprites:
        window.blit(entity.surface, entity.rect)


def main():
    clock = pygame.time.Clock()
    game_state = "menu"

    while True:
        clock.tick(FPS)

        if game_state == "menu":
            res = menu_loop("Welcome to platfromer game", "Play!")
            if res == "game":
                level, game_events, all_sprites, platforms = init_game()
                game_state = "game"
        elif game_state == "game":
            res = game_loop(all_sprites, platforms, level, game_events)
            if res == "victory":
                game_state = "victory"
        elif game_state == "victory":
            res = menu_loop("VICTORY", "Main menu")
            if res == "game":
                game_state = "game"
            elif res == "menu":
                game_state = "menu"

        pygame.display.update()

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
