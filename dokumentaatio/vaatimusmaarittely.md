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
  - Maali on portaali, joka sijaitsee jossakin hankalasti tavoitettavassa paikassa TEHTY
  - Maaliin pääseminen lataa seuraavan kentän TEHTY
  - Kentät muuttuvat vaikeammiksi TEHTY
    - Enemmän piikkejä?
    - Vaikeammat hypyt?

- Käyttäjä voi edetä tasolta toiselle portaalien kautta TEHTY
  - Jokaisella tasolla yksi portaali, joka vie seuraavalle tasolle TEHTY
- Käyttäjä voi voittaa pelin pääsemällä raketille TEHTY
  - Pelin voi aloittaa uudelleen TEHTY

- Käyttäjällä on rajoitettu määrä "elämiä", joiden loppuessa peli päättyy TEHTY
  - Elämät vähenevät yksi kerrallaan, kun käyttäjä tekee kontaktia esteen kanssa TEHTY
  - Elämiä voi kerätä lisää
  - Käyttäjä voi yrittää peliä uudelleen TEHTY
- Pelissä on esteitä, jotka vähentävät käyttäjän elämiä TEHTY
  - Piikit sijaitsevat tahallaan mahdollisimman ärsyttävissä paikoissa, käyttäjän on väistettävä niitä TEHTY
- Pelikentillä on kolikoita, joita käyttäjä voi kerätä
  - Esim. 5 kolikkoa antaa käyttäjälle elämän

 
## Jatkokehitysideoita

- Vaikeustason kehitys
- Pelaajahahmon valinta
  - Käyttäjä voi valita pelihahmon muutaman joukosta
