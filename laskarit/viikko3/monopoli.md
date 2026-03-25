```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta

    Pelilauta "1" -- "26" Katu
    Katu "1" -- "1" Katu : Nimi
    Katu "1" -- "4" Talo
    Katu "1" -- "1" Hotelli
    Katu "1" -- "1" Pelaaja
    
    Pelilauta "1" -- "4" Asema
    Pelilauta "1" -- "2" Laitos
    Pelilauta "1" -- "1" Aloitusruutu
    Pelilauta "1" -- "1" Vankila
    Pelilauta "1" -- "3" Sattuma
    Sattuma "1" -- "*" Sattuma : Satunnainen kortti
    Pelilauta "1" -- "3" Yhteismaa
    Yhteismaa "1" -- "*" Yhteismaa : Satunnainen kortti

    Pelilauta "1" -- "0..8" Pelinappula

    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "1" -- "*" Raha
    Pelaaja "2..8" -- "1" Monopolipeli
```
