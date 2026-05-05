import pygame
from text_renderer import draw_health, draw_level_id
from event_handler import GameEventHandler
from level import Level


def init_game():
    """Generates required entities for game.

    Returns:
        Level-object, GameEventHandler-entity, platform group, all_sprites group."""

    level = Level(1)
    level.generate()

    all_sprites, platforms = level.get_groups()

    game_events = GameEventHandler(level.player, platforms)

    return level, game_events, all_sprites, platforms


def game_loop(window,
              all_sprites=pygame.sprite.Group,
              platforms=pygame.sprite.Group,
              level=Level,
              game_events=GameEventHandler):
    """Main game loop function. Blits entities and handles inputs.

    Args:
        window: Pygame window object.
        all_sprites: Sprite group containing all sprites to be drawn.
        platfomrs: Sprite group containing platfrom objects.
        level: Level object.
        game_events; GameEventHandler object.

    Returns:
        None if no events, "victory" or "death" according to events.
        """

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
