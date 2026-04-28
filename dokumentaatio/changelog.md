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
- Portaali, josta pääsee seuraavalle kentälle
    - Toistaiseksi vaihtaa kenttien 1 ja 2 välillä
    - Portaalin sijainti määritelty jokaista kenttää kohti json-tiedostossa
    - Pelaajan positio nollaantuu kulkiessa portaalin läpi
- Testejä laajennettu hieman

# Viikko 5

- Testejä laajennettu
    - Level ja Player -luokkia testataan nyt kattavammin
    - Eventhandler sai vihdoin testit
- Tasojen lataamista muutettu
    - Ladataan seuraava taso pelaajan päästyä portaaliin
- Lisätty selkäranka raketille, jolla pelaaja voi lopettaa pelin
    - Rakettiin pääsy lopettaa pelin, avaa voittonäkymän
- Lisätty voittonäkymä
    - Voittonäkymästä pääsee takaisin päävalikkoon
    - Pelin voi aloittaa uudelleen
- Pelisilmukka refaktoroitu
    - Tilat vaihtuvat nyt sulavasti ja uusien tasojen / tilojen lisääminen helppoa

# Viikko 6

- Pelaajan elämä-systeemi
    - Aloitetaan 3:lla sydämmellä
    - Vähenee kun törmää esteeseen
    - Peli päättyy kun loppuu
- Kuolema gamestate
    - Käytännössä sama kuin menu, eri tekstit vain
    - Voi aloittaa pelin suoraan uudelleen
- Esteet (piikkipallo?)
    - Aseteltu mahdollisimman tielle, jotta peli ei olisi liian helppo
    - Törmääminen poistaa piikin, tasapainottava tekijä :)
    - Tällä hetkellä pikku bugi: Jos pelaaja tippuu esim 2:n lähekkäin olevan piikin päälle ja poistaa molemmat samanaikaisesti, pelaajalta vähennetään vain yksi elämä
- Mainin refaktorointi
    - Tekstin renderöinnistä vastaavat funktiot siirretty omaan moduuliin
    - Pääsilmukassa jatkuvasti kutsuttavat loop-metodit siirretty omaan moduuliin
- Tasojen suunnittelu
    - Yritin ajatuksella rakentaa edes jollain tavalla haastavia tasoja, jotta pelillä olisi arvoa muutenkin kuin pelkkänä harjoitustyönä
    - Tällä hetkellä tasoja on 5, niitä tulee lisää, kenties jopa 10
    - Tasot muuttuvat progressiivisesti vaikeammiksi, piikkejä tulee enemmän ja vaaditaan tarkempia ja harkitumpia hyppyjä
- Docstringit
    - Lähestulkoon kaikki luokat, metodit ja funktiot kuvailtu nyt docstringeillä.
- Käyttöohje
- Arkkitehtuurikuvausta päivitetty
    - Hakemistorakenne selitetty
    - Keskeisin toiminnallisuus selitetty
    - Konkreettisia esimerkkejä luokkien välisestä yhteistyöstä
