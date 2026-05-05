# Arkkitehtuurikuvaus

Projektin hakemistorakenteen ja sovelluslogiikan kuvaus.

## Hakemistorakenne

Projektin lähdekoodi on jaettu useaan moduuliin, jotka on ryhmitelty kansioihin. 

### src/

- **config.py:** Vakiomuuttujat, ikkunan koko, fps, pelaajan kiihtyvyys ja kitka, fontit, tasojen määrä.
- **event_handler.py:** Pelaajan syötteen valvonnasta vastaavat luokat.
- **game.py:** Pelisilmukka, pelin alustusfunktio.
- **level.py:** Tasojen lataaminen ja generointi. Valvoo pelaajan interaktioita portaalien ja piikkien kanssa.
- **main.py:** Pääohjelma.
- **text_renderer.py:** Tekstin piirtämisestä vastaavat funtkiot.
- **tasks.py:** Invoke-taskit.
  - Käynnistäminen, testien suorittaminen, pylint, autopep8 ja kattavuusraportin generointi.

### src/assets/

- Pelaajahahmo, platformi, lattia, portaali, raketti ja piikkipallo.
- BMP-muodossa.

### src/levels/

- Json-tiedostoja.
- Sisältävät tasokohtaiset koordinaatit platformeille, portaaleille, piikeille ja raketille.

### src/sprites/

- Pelaaja, platformi, portaali, raketti ja piikki -luokat.

### src/tests/

- Projektin yksikkötestit.
- Jaettu tiedostoihin testattavan alueen mukaan.

### src/ui/

- ui.py
- Pitää sisällään menu-silmukan ja alustusfunktion.

## Sovelluslogiikka

### Keskeisin toiminnallisuus

Projektin sovelluslogiikka on pyritty erottamaan käyttöliittymäkoodista. Logiikka perustuu lähinnä Level, GameEventHandler ja Player -luokkien yhteistyöhön. GameEventHandler valvoo käyttäjän syötteitä ja kutsuu Player-luokan metodeja niiden mukaan.

Level-luokka valvoo pelaajan siirtymiä portaalien kautta tasolta toiselle ja muodostaa uusia tasoja json-tiedostojen pohjalta. Json-tiedostot ovat vakioita, eivätkä niiden sisältämät arvot muutu pelin aikana. Tiedostot sisältävät sanakirjamaisesti tallennettuja koordinaatteja platformeille, portaaleille, piikeille ja raketille. Level-luokka lukee level_id:n mukaisen json-tiedoston ja muodostaa sen pohjalta ladattavan tason.

Player-luokka pitää sisällään pelaajan liikettä ohjaavat metodit ja suorittaa myös kollisionvalvontaa hyppyjä varten.

Main.py sisältää pelin pääsilmukan, jossa on haara jokaista pelin tilaa kohden. Pääsilmukka kutsuu joko src/ui/ui.py:ssa sijaitsevaa menu_loop-funktiota tai src/game.py:ssa sijaitsevaa game_loop-funktiota. Kutsuttava loop-funktio palauttaa merkkijonon, jos pelin tilan muuttava tapahtuma tapahtuu. Pelin alussa pääsilmukan game_state muuttuja alustetaan arvolla "menu". Esimerkiksi kun pelaaja painaa aloitusnäytön play-nappia, menu_loop palauttaa merkkijonon "game", jonka pääsilmukka tallentaa muuttujaan ja asettaa game_state muuttujan arvoksi. Tällöin pääsilmukan suoritus siirtyy seuraavaan haaraan ja aletaan kutsua game_loop-funktiota.

### Esimerkkejä toiminnallisuudesta

Pelaajan painaessa "a"-näppäintä GameEventHandler kutsuu pelaajaolion change_direction-metodia argumentilla "left", mikä vaihtaa pelaajaolion moveleft-attribuutin arvon True:ksi. Kun "a"-näppäin päästetään irti, GameEventHandler kutsuu samaa change_direction-metodia argumentilla "cancel_left", mikä muuttaa moveleft-attribuutin takaisin False:ksi.

Pelaajan törmätessä portaaliin Level-luokka tarkistaa nykyisen tason ja aloittaa toimenpiteet, mikäli seuraava taso on olemassa. Jos seuraava taso on olemassa, luokka kutsuu omaa clear_grops- metodia, joka tyhjentää edellisen tason platformit, portaalit ja piikit luokan muistista. Tämän jälkeen kutsutaan generate-metodia, joka pulestaan kutsuu get_level_data-metodia lukeakseen seuraavan tason tiedot json-tiedostosta. Generate-metodi käy läpi sanakirjaa, joka sisältää jokaisen tasolle kuuluvan esineen koordinaatit ja luo vastaavat sprite-oliot. Oliot tallennetaan Level-luokan sprite-ryhmiiin, jotka pelisilmukka lukee ja piirtää näytölle.

## Luokkakaavio

Main-tiedosto tuntee luokat MenuEventHandler, GameEventHandler ja Level. MenuEventHandler valvoo ja hallitsee käyttäjän syötteitä pelin valikkonäkymissä. GameEventHandler valvoo käyttäjän syötteitä varsinaisen pelin sisällä ja kutsuu Player-luokan metodeja pelaajan liikkeen aikaansaamiseksi. Level-luokka pitää sisällään kaiken näytölle piirrettävän ja rakentaa pelin tasot. Level-luokka luo pelaajaolion, joka välitetään myös GameEventHandler-luokalle. 

Level luokka ei kuitenkaan piirrä tarvittavia olioita näytölle, vaan piirtäminen (pygamen blit-metodilla) tapahtuu game_loop-funktiossa. Level-luokan sisältämät näytölle piirrettävät oliot perivät pygamen Sprite-luokan, ja ne on jaettu pygamen sprite groupeihin. Ryhmä all_sprites pitää sisällään kaikki oliot ja ryhmä platforms pitää sisällään oliot, joiden kanssa pelaajan odotetaan törmäävän. Game_loop piirtää jokaisella iteraatiolla all_sprites-ryhmän sisältämät oliot. 

Jokaisella tasolla voi olla yksi pelaaja, yksi lattia, yksi portaali ja ja yksi raketti. Lisäksi tasolla voi olla monta platformia ja monta piikkipalloa. 

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

Pelin alustaminen ja siirtymä mainin pääsilmukkaan:

```mermaid
 sequenceDiagram
    main->>menu_events: MenuEventHandler()
    main->>game_state: "menu"

    main->>level: Level(1)
    main->>game_events: GameEventHandler()
    main->>all_sprites: level.all_sprites
    main->>platforms: level.platforms
```

Tämän jälkeen suoritus siirtyy silmukkaan, jossa pelin tila muuttuu game_state-muuttujan mukaan. Tässä vaiheessa game_state on "menu". Menu_loop funktio ottaa parametreiksi näytölle piirrettävän tekstin, ikkunan ja MenuEventHandler-olion. Tämän ansiosta samaa funktiota voidaan käyttää pelin kaikissa valikkonäkymissä.

```mermaid
 sequenceDiagram
    main->>res: menu_loop(window, menu_events, "Main menu", "Play")
    ui.menu_loop-->>res: "game"
    res->>game_state: "game"
```

Tämän jälkeen pääohjelman suoritus siirtyy seuraavaan haaraan, jossa res-muuttujaan tallennetaan nyt game_loop-funktion palautusarvo, joka määräytyy pelaajan toiminnan mukaan. Esimerkiksi jos pelaaja kuolee, palautetaan "death", jos pelaaja pääsee raketille asti, palautetaan "victory".











Pääohjelma alustaa syötteenvalvonnasta vastaavan luokan ja pelin tilan. Kun peli aloitetaan, init_game() metodi luo tarvittavat oliot (Level, GameEventHandler, Player, Platform) ja palauttaa ne. 

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

Pelin tilan muutos "menu":sta "game":ksi siirtää suorituksen toiseen päähohjelman haaraan ja varsinainen pelisilmukka käynnistyy. Pelisilmukalle välitetään ikkuna ja luodut oliot. 

Game_loop metodissa valvotaan käyttäjän syötteitä GameEventHandler-luokan metodeilla ja likuutetaan pelaajahahmoa sen omalla metodilla. GameEventHandler muuttaa Player-olion luokkamuuttujia joiden perusteella move-metodi liikuttaa pelaajahahmoa. Lisäksi tarkistetaan törmääminen portaaleihin, raketteihin ja piikkeihin. Pääsilmukka tallentaa game_loopin palautukset muuttujaan ja tarkistaa muttujan sisällön, jos sisältö vastaa jotakin haaraehtoa, pääsilmukan haara vaihtuu ja tällöin vaihtuu myös pelin tila. 
