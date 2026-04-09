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

- Näppäinten painallusten valvonta siirretty omaan luokkaan
    - Ollut aikaisemmin Player-luokassa, sen jälkeen pääohjelmassa
- Piirretty ja lisätty pelaajahahmo
    - Vihreä ukko
    - Uusi hahmo-assetti joka vaihtuu kun pelaaja hyppää
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
- Peliä testattu cubbli-virtuaalityöasemalla
    - Toimiihan se
- Hyppimistä paranneltu
    - Välilyönti pohjassa = pitkä hyppy
- Törmäämisen tunnistamista parannettu hieman
    - Pelaaja pääsee platformin päälle vain jos hän ylittää sen yläreunan
    - Platfromin alareuna ei kuitenkaan toimi vielä kattona (yllättävän mutkikasta on ollut selvittää tämä)
- Vaihtoehtoinen pelaaja-asset
    - Aktivoituu kun pelaaja hyppää, deaktivoituu kun pelaaja laskeutuu
- Selkäranka pelin etenemiselle
  - Tasojen data (platformien sijainti, kolikon sijainti) luetaan json tiedostosta
  - Level-luokka alustetaan jokaista tasoa varten tason järjestysnumerolla
