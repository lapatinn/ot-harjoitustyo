## Luokkakaavio

Sovelluksen tämänhetkinen luokkarakenne:

```mermaid
 classDiagram
    main "1" -- "1" GameEventHandler
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

## Sekvenssidiagrammi

