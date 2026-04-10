import pygame
from pygame.locals import *
from config import PLAY_FONT, SCREEN_HEIGHT, SCREEN_WIDTH, FPS, WELCOME_COLOR, WELCOME_FONT, PLAY_COLOR
from event_handler import GameEventHandler
from level import Level

pygame.init()
vec = pygame.math.Vector2
pygame.display.set_caption("Platformer game")

button_text = "PLAY"
button_width, button_height = PLAY_FONT.size(button_text)
button_x = (SCREEN_WIDTH // 2) - (PLAY_FONT.size(button_text)[0] // 2)
button_y = 200

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    window.blit(img, (x, y))
    return img.get_rect(topleft=(x, y))


def main(window):
    clock = pygame.time.Clock()
    menu = True

    while menu:
        clock.tick(FPS)
        window.fill((50, 0, 0))

        draw_text("Welcome to Platformer game", WELCOME_FONT,
                  WELCOME_COLOR, (SCREEN_WIDTH // 2) - 200, 50)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        is_hovering = (button_x <= mouse_x <= button_x + button_width
                       and button_y <= mouse_y <= button_y + button_height)

        button_color = WELCOME_COLOR if is_hovering else PLAY_COLOR

        play_button_rect = draw_text(button_text, PLAY_FONT,
                                     button_color, button_x, button_y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if play_button_rect.collidepoint(event.pos):
                        menu = False

                        level = Level(1)
                        level.generate()
                        all_sprites, platforms = level.get_groups()
                        game_events = GameEventHandler(level.player, platforms)

                        game = True

        pygame.display.update()

    while game:
        clock.tick(FPS)
        window.fill((0, 0, 40))

        game_events.handle_events()

        level.player.move()
        level.player.check_floor_collision(platforms)

        portal_used = level.check_portal()
        if portal_used:
            all_sprites, platforms = level.get_groups()
            game_events.update_platforms(platforms)

        for entity in all_sprites:
            window.blit(entity.surface, entity.rect)

        pygame.display.update()

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
