## Luokkakaavio

Sovelluksen tämänhetkinen luokkarakenne. Level-luokka pitää sisällään pelaajan ja kaikki spritet, joiden kanssa pelaaja voi kanssakäydä. Level-luokka tarkistaa törmäämiset esim. portaalien, rakettien ja piikkien kanssa. GameEventHandler ja MenuEventHandler -luokat vastaavat käyttäjän syötteiden valvonnasta ja hallinnasta. 

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
    Level "1" -- "*" Spike
    Level "1" -- "1" Portal
    Level "1" -- "1" Rocket
```

## Sekvenssikaavio

Pelin käynnistäminen, siirtyminen menusta pelisilmukkaan ja pelin päättyminen luokkakaaviona. 

```mermaid
 sequenceDiagram
    main->>menu_events: MenuEventHandler()
    main->>game_state: "menu"

    main->>init_game: level, game_events, all_sprites, platforms
    
    init_game->>level: Level(1)
    
    level->>level.player: Player()
    level->>level.floor: Floor()
    
    init_game->>level: level.generate()
    
    level->>platform: Platform(x, y)
    level->>portal: Portal(x, y)
    level->>rocket: Rocket(x, y)
    
    init_game->>level: level.get_groups()
    level-->>init_game: all_sprites, platforms
    
    init_game->>game_events: GameEventHandler()
    init_game-->>main: level, game_events, all_sprites, platforms
    
    main->>game_state: "game"
    
    main->>res: game_loop()
    game_loop->>game_events: handle_events()
    game_loop->>level.player: player.move()
    game_loop->>level.player: player.check_floor_collision(platforms)

    game_loop->>rocket_used: level.check_rocket()
    rocket_used-->>game_loop: True
    game_loop-->>res: "victory"
    res-->>main: "victory"

    main->>game_state: "victory"
```

Pääohjelma alustaa syötteenvalvonnasta vastaavan luokan ja pelin tilan. Kun peli aloitetaan, init_game() metodi luo tarvittavat oliot (Level, GameEventHandler, Player, Platform) ja palauttaa ne. 

Pelin tilan muutos "menu":sta "game":ksi siirtää suorituksen toiseen päähohjelman haaraan ja varsinainen pelisilmukka käynnistyy. Pelisilmukalle välitetään ikkuna ja luodut oliot. 

Game_loop metodissa valvotaan käyttäjän syötteitä GameEventHandler-luokan metodeilla ja likuutetaan pelaajahahmoa sen omalla metodilla. GameEventHandler muuttaa Player-olion luokkamuuttujia joiden perusteella move-metodi liikuttaa pelaajahahmoa. Lisäksi tarkistetaan törmääminen portaaleihin, raketteihin ja piikkeihin. Pääsilmukka tallentaa game_loopin palautukset muuttujaan ja tarkistaa muttujan sisällön, jos sisältö vastaa jotakin haaraehtoa, pääsilmukan haara vaihtuu ja tällöin vaihtuu myös pelin tila. 
