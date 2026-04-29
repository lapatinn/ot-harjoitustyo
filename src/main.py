import pygame
from config import (SCREEN_HEIGHT, SCREEN_WIDTH, FPS)
from game import menu_loop, game_loop, init_game, init_menu

pygame.init()
pygame.display.set_caption("Portal Bob")

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    clock = pygame.time.Clock()
    menu_events, game_state = init_menu()
    level, game_events, all_sprites, platforms = init_game()

    while True:
        clock.tick(FPS)

        if game_state == "menu":
            res = menu_loop(window, menu_events, "Main menu", "Play")
            if res == "game":
                game_state = "game"

        elif game_state == "game":
            res = game_loop(window, all_sprites, platforms, level, game_events)
            if res == "victory":
                game_state = "victory"
            elif res == "death":
                game_state = "death"

        elif game_state == "victory":
            res = menu_loop(window, menu_events, "You won!", "Main menu")
            if res == "menu":
                game_state = "menu"

        elif game_state == "death":
            res = menu_loop(window, menu_events, "You died!", "Try again")
            if res == "game":
                level, game_events, all_sprites, platforms = init_game()
                game_state = "game"

        pygame.display.update()


if __name__ == "__main__":
    main()
