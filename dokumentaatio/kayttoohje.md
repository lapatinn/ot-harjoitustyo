# Käyttöohje

Lataa projektin viimeisin [versio](https://github.com/lapatinn/ot-harjoitustyo/releases) kohdasta Assets. 
Vaihtoehtoisesti voit myös kloonata repositorion. 

## Käynnistäminen

Ennen pelin käynnistämistä, on asennettava riippuvuudet komennolla:

```bash
poetry install
```

Pelin voi käynnistää komennolla:

```bash
poetry run invoke start
```

Pelin voi aloittaa painamalla Play-näppäintä.

Pelaaja liikkuu vasemmalle / oikealle A ja D näppäimillä. Pelaaja hyppää välilyönnillä. Lyhyt painallus saa aikaan pienen hypyn, pitkä painallus pitkän hypyn.

Pelin voi voittaa etenemällä tasolta tasolle liilojen portaalien kautta. Viimeisellä tasolla on raketti, jolla voit paeta. Muista väistää piikkipalloja!
