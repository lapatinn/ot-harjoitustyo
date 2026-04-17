# Ot-harjoitustyo

Aineopintojen harjoitustyö, ohjelmistotekniikka

## 2D videopeli pygame-kirjastolla.

Yksinkertainen tasohyppelypeli **pygame-kirjastolla**, jossa pieni vihreä ukkeli seikkailee avaruudessa. Tarkoituksena on hyppiä platformien päällä putoamatta *loputtomaan tyhjyyteen* ja kerätä mahdollisimman paljon kolikoita. Pelaajalla on aluksi tietty määrä elämiä, jotka vähenevät törmätessä vihollisiin. Pelaaja voi voittaa pelin pääsemällä kentän loppuun. Pelin vaikeustason kehityksen toteutus on vielä toistaiseksi epäselvää.

## Linkit

- [Vaatimusmäärittely](https://github.com/lapatinn/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/lapatinn/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/lapatinn/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/lapatinn/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)


## Asennus

Komennot suoritetaan projektin juurihakemistossa.

1. Riippuvuudet asennetaan komennolla:

```bash
poetry install
```

2. Sovellus käynnistetään komennolla:

```bash
poetry run invoke start
```

## Muut komentorivitoiminnot

### Testit

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportti generoidaan komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu hakemistoon _/htmlcov_, ja sitä voi tarkastella selaimella esimerkiksi komennolla:

```bash
firefox htmlcov/index.html
```

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset suoritetaan komennolla:

```bash
poetry run invoke lint
```
