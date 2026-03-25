import pygame
pygame.init()
pygame.display.set_caption("Platformer game")

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

FPS = 60
PLAYER_VEL = 5

WELCOME_FONT = pygame.font.SysFont("arialblack", 50)
PLAY_FONT = pygame.font.SysFont("arialblack", 60)
WELCOME_COLOR = (255,255,255)
PLAY_COLOR = (213,216,53)

button_text = "PLAY"
button_width, button_height = PLAY_FONT.size(button_text)
button_x = (SCREEN_WIDTH // 2) - (PLAY_FONT.size(button_text)[0] // 2)
button_y = 200

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    window.blit(img, (x,y))
    return img.get_rect(topleft=(x,y))

def main(window):
    clock = pygame.time.Clock()
    run = True
    while run:
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
        
        pygame.display.update()

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)