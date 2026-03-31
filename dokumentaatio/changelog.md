# Viikko 3

- Lisätty peli-ikkuna
    - Ikkuna sisältää alkunäytön luurangon
    - Pelin otsikko ja Play-nappi
    - Play-nappi vaihtaa väriä, jos hiiri osoittaa sitä
- Testattu, että tekstin piirtämisestä vastaava funktio palauttaa pygame.Rect-olion
- Alkunäytöltä voi aloittaa pelin
- Ensimmäisellä tasolla on pelaaja (toistaiseksi neliö), joka voi liikkua ja hyppiä
- Ensimmäisellä tasolla on lattia ja kaksi tasoa, joiden päällä pelaaja voi seistä

# Viikko 4

- Näppäinten painallusten valvonta siirretty pääohjelmaan
    - Ollut aikaisemmin Player-luokassa
- Piirretty ja lisätty pelaajahahmo
    - Vihreä ukko
- Piirretty ja lisätty platformi
    - Kuun pinta?
- Lisätty ja konfiguroitu pylint
    - Käytössä kurssimateriaalin rc-tiedosto, johon on lisätty pygame-moduulin ignoroiva rivi
    - Herjaa edelleen pygame.locals muuttujista, korjaaaan
- Lisätty autopep8
- Lisätty taskit lintille ja formatoinnille
- Testattu Player-luokkaa
    - Luominen, liikkuminen
    - Hahmo ei liiku ikkunan rajojen yli
