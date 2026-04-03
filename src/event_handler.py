import pygame
from player import Player

class GameEventHandler:
    def __init__(self, player=Player, platforms=pygame.sprite.Group):
        self.player = player
        self.platforms = platforms

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump(self.platforms)
                if event.key == pygame.K_a:
                    self.player.change_direction("left")
                if event.key == pygame.K_d:
                    self.player.change_direction("right")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.player.cancel_jump()
                if event.key == pygame.K_a:
                    self.player.change_direction("cancel_left")
                if event.key == pygame.K_d:
                    self.player.change_direction("cancel_right")
