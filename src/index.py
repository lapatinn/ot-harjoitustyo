import pygame
from pygame.locals import *

pygame.init()
vec = pygame.math.Vector2
pygame.display.set_caption("Platformer game")

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60
ACC = 1
FRIC = -0.12

WELCOME_FONT = pygame.font.SysFont("arialblack", 50)
PLAY_FONT = pygame.font.SysFont("arialblack", 60)
WELCOME_COLOR = (255,255,255)
PLAY_COLOR = (213,216,53)

button_text = "PLAY"
button_width, button_height = PLAY_FONT.size(button_text)
button_x = (SCREEN_WIDTH // 2) - (PLAY_FONT.size(button_text)[0] // 2)
button_y = 200

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface((30, 30))
        self.surface.fill((0,255,0))
        self.rect = self.surface.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT - 50))

        self.pos = vec((SCREEN_WIDTH//2, SCREEN_HEIGHT - 50))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def move(self):
        self.acc = vec(0,0)
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_a]:
            self.acc.x = -ACC
        if pressed_keys[K_d]:
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.x > SCREEN_WIDTH:
            self.pos.x = SCREEN_WIDTH

        self.rect.midbottom = self.pos

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface((SCREEN_WIDTH, 50))
        self.surface.fill((255,0,0))
        self.rect = self.surface.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT))

class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        super().__init__()
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color

        self.surface = pygame.surface.Surface((self.width, self.height))
        self.surface.fill(color)
        self.rect = self.surface.get_rect(center=(self.x, self.y))

player = Player()
floor = Floor()
platfrom1 = Platform(100, 25, SCREEN_WIDTH//2, SCREEN_HEIGHT//2, (0,0,255))


all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(floor)
all_sprites.add(platfrom1)

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

        for entity in all_sprites:
            window.blit(entity.surface, entity.rect)
        
        player.move()

        pygame.display.update()       

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)