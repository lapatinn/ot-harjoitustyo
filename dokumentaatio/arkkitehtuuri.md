## Luokkakaavio

Sovelluksen tämänhetkinen luokkarakenne:

```mermaid
 classDiagram
    main "1" -- "1" GameEventHandler
    main "1" -- "1" MenuEventHandler
    main "1" -- "1" Level

    GameEventHandler "1" -- "1" Player
    GameEventHandler "1" -- "*" Platform
    GameEventHandler "1" -- "1" Floor

    Level "1" -- "1" Player
    Level "1" -- "1" Floor
    Level "1" -- "*" Platform
    Level "1" -- "1" Portal
    Level "1" -- "1" Rocket
```

## Sekvenssikaavio

Sovelluksen käynnistämistä ja pelille välttämättömien luokkien alustamista kuvaava kaavio:

```mermaid
 sequenceDiagram
    main->>level: Level(1)

    level->>level.player: Player()
    level->>level.floor: Floor()

    main->>level: level.generate()

    level->>platform: Platform(x, y)
    level->>portal: Portal(x, y)
    level->>rocket: Rocket(x, y)

    main->>level: level.get_groups()
    level-->>main: level.all_sprites, level.platforms

    main->game_events: GameEventHandler(level.player, level.platforms)
```

Tämän sekvenssin jälkeen siirrytään pelisilmukkaan, jossa GameEventHandler-luokka valvoo käyttäjän syötteitä, ja välittää Player-luokalle ohjeita liikkumiseen ja hyppimiseen. 
