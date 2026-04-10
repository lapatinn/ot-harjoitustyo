# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on videopeli, jota on tarkoitus pelata. Käyttäjä etenee pelissä väistämällä vihollista, hyppimällä leijuvilla alustoilla ja keräämällä kolikoita. 

## Käyttäjät

Sovelluksella on lähtökohtaisesti yksi käyttäjä, eli yksi pelaaja.

## Perusversion tarjoama toiminnallisuus

- Käyttäjä voi käynnistää sovelluksen, jolloin peli-ikkuna aukeaa TEHTY
  - Peli alkaa aloitusnäytöstä, jossa käyttäjä voi aloittaa pelin TEHTY
- Käyttäjä voi aloittaa pelin TEHTY

- Käyttäjä voi liikkua ja hyppiä
  - A ja D näppäimet liikuttavat pelaajaa vasemmalle / oikealle TEHTY
  - Välilyönti saa pelaajan hyppäämään TEHTY
    - Lyhyt painallus = lyhyt hyppy, pitkä painallus = pitkä hyppy TEHTY
- Pelissä on painovoima, jonka vuoksi pelaaja seisoo alustoilla ja putoaa alaspäin TEHTY
  -  Alustojen välillä voi hyppiä TEHTY
  -  Alustan alareunaan törmää, mikä estää pääsemästä sen päälle suoraan alapuolelta
-  Käyttäjä pääsee seuraavalle tasolle päästyään kentän maaliin asti TEHTY
  - Maali on ovi / portaali, joka sijaitsee jossakin hankalasti tavoitettavassa paikassa TEHTY
  - Maaliin pääseminen lataa seuraavan kentän TEHTY
  - Kentät muuttuvat vaikeammiksi
    - Enemmän vihollisia?
    - Vaikeammat hypyt?

- Käyttäjällä on rajoitettu määrä "elämiä", joiden loppuessa peli päättyy
  - Elämät vähenevät yksi kerrallaan,  kun käyttäjä tekee kontaktia vihollisen kanssa
  - Elämiä voi kerätä lisää
  - Käyttäjä voi yrittää peliä uudelleen
- Käyttäjä voi voittaa pelin, eli päästä maaliin asti
  - Peli päättyy ja sen voi aloittaa uudelleen
 
## Jatkokehitysideoita

- Vaikeustason kehitys
- Pelaajahahmon valinta
  - Käyttäjä voi valita pelihahmon muutaman joukosta
