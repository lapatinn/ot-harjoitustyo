import pygame
from pygame.locals import *
from config import *
from player import Player
from platforms import Platform, Floor

pygame.init()
vec = pygame.math.Vector2
pygame.display.set_caption("Platformer game")

button_text = "PLAY"
button_width, button_height = PLAY_FONT.size(button_text)
button_x = (SCREEN_WIDTH // 2) - (PLAY_FONT.size(button_text)[0] // 2)
button_y = 200

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()
floor = Floor()
platform1 = Platform(100, 25, SCREEN_WIDTH//2, SCREEN_HEIGHT//2, (0,0,255))
platform2 = Platform(100, 25, SCREEN_WIDTH//3, SCREEN_HEIGHT//2 + 100, (125, 125, 0))

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(floor)
all_sprites.add(platform1)
all_sprites.add(platform2)

platforms = pygame.sprite.Group()
platforms.add(floor)
platforms.add(platform1)
platforms.add(platform2)

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    window.blit(img, (x,y))
    return img.get_rect(topleft=(x,y))

def main(window):
    clock = pygame.time.Clock()
    menu = True

    while menu:
        clock.tick(FPS)
        window.fill((50,0,0))
        
        draw_text("Welcome to Platformer game", WELCOME_FONT, WELCOME_COLOR, (SCREEN_WIDTH // 2) - 200, 50)
        
        mouse_x, mouse_y = pygame.mouse.get_pos()

        is_hovering = (button_x <= mouse_x <= button_x + button_width
                       and button_y <= mouse_y <= button_y + button_height)
        
        button_color = WELCOME_COLOR if is_hovering else PLAY_COLOR

        play_rect = draw_text(button_text, PLAY_FONT, button_color, button_x, button_y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if play_rect.collidepoint(event.pos):
                        print("PLAY pressed")
                        menu = False
                        game = True

        pygame.display.update()

    while game:
        clock.tick(FPS)
        window.fill((0,0,40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump(platforms)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_a]:
            player.dir = "left"
        if pressed_keys[K_d]:
            player.dir = "right"

        player.move()
        player.check_floor_collision(platforms)

        for entity in all_sprites:
            window.blit(entity.surface, entity.rect)

        pygame.display.update()       

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)