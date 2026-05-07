# Käyttöohje

Lataa projektin viimeisin [versio](https://github.com/lapatinn/ot-harjoitustyo/releases) kohdasta Assets. Projekti latautuu tällöin pakattuna tiedostona, joka täytyy purkaa.

Vaihtoehtoisesti voit myös kloonata repositorion valitsemaasi hakemistoon.

## Ennen käynnistämistä

### Python

Projekti vaatii vähintään python version 3.12.
Version voi tarkistaa komennolla:

```bash
python --version
```

tai

```bash
python3 --version
```

Jos python-versio on vanhempi kuin 3.12, seuraa [päivitysohjeita](https://ohjelmistotekniikka-hy.github.io/python/toteutus#python-versioiden-hallinta)

### Poetry

Poetry hallinnoi projektin riippuvuuksia, eikä peli toimi ilman sitä. Jos poetry puuttuu, voit vilkaista [asennusohjeita](https://ohjelmistotekniikka-hy.github.io/python/viikko2#asennus). Poetryn asentamisen jälkeen on suljettava ja avattava terminaali-ikkuna uudelleen. 

Onnistuneen asennuksen voi varmistaa komennolla:

```bash
poetry --version
```

## Pelin käynnistäminen

Ennen pelin käynnistämistä, on asennettava projektin riippuvuudet komennolla:

```bash
poetry install
```

Pelin voi käynnistää komennolla:

```bash
poetry run invoke start
```

## Pelaaminen

Pelin voi aloittaa painamalla Play-näppäintä.

Pelaaja liikkuu vasemmalle / oikealle A ja D näppäimillä. Pelaaja hyppää välilyönnillä. Lyhyt painallus saa aikaan pienen hypyn, pitkä painallus pitkän hypyn.

Pelin voi voittaa etenemällä tasolta tasolle liilojen portaalien kautta. Viimeisellä tasolla on raketti, jolla voit paeta. Muista väistää piikkipalloja!
