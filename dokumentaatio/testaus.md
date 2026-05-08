# Testaus

Pelin luokkia on testattu automatisoidusti unittest-kirjastolla. Lisäksi mock-kirjastoa on käytetty suhteellisen paljon, koska moni pelin keskeisistä toiminnallisuuksista riippuu pygame-kirjaston omista moduuleista joiden varsinainen testaaminen menee aivan liian monimutkaiseksi. 

Pelin kokonaiskattavuus on 79% ja haarautumakattavuus 75%.

![](./kuvat/coverage_report.png)

Kattavuuden ulkopuolelle on jätetty vakiomuuttujia sisältävä config.py ja valikkokäyttöliittymästä vastaava ui/ui.py. 

Pelin main.py:n pääsilmukalle ei saatu aikaiseksi testejä, mikä laskee kokonaiskattavuutta tuntuvasti. Yleisesti pygame-kirjastolla toteutettua peliä on hankala testata, mikä näkyy ehkä kattavuudessa. 

### Asennus ja järjestelmätestaus

Peli on asennettu ja pelattu alusta loppuun seuraavilla käyttöjärjestelmillä:

- Cubbli linux
- Arch linux
- WSL Ubuntu (Windows subsystem for linux, Windows 11)
- Helsingin yliopiston linux-etätyöasema (Ommnissa Horizon, selaimella)

Kyseisillä käyttöjärjestelmillä on myös suoritettu automatisoidut yksikkötestit ja generoitu kattavuusraportti.

Linux-etätyöasemalla (selainversio) pelaaminen saattaa tuntua hieman kömpelöltä, koska peli pyörii hieman hitaammin. Tämä johtunee selaimesta? Varsinaisella Horizon-clientillä peliä ei ole testattu, kenties suorituskyky olisi siellä parempi? Kuitenkin kaikilla ei-virtuaalisilla käyttöjärjestelmillä peli pyörii kuten pitääkin.

### Ohjelmaan jääneet riittämättömdyydet

Ohjelma saa pylint arvosanaksi 9.75, mutta "Either all return-statements should return and expression or none of them should"-virheitä on useampi. Virheiden korjaaminen toisi koodiin mielestäni ei-toivottua monimutkaisuutta. 

Main.py:n pääsilmukka on ehkä turhan laaja ja toteutettu ilman varsinaista luokkaa. Luokan luominen mahdollistaisi silmukan testaamisen, mutta en tässä vaiheessa koe sitä absoluuttisen välttämättömäksi, sillä ohjelman toiminnan kannalta oleellisimmat luokat tulevat testatuiksi.
