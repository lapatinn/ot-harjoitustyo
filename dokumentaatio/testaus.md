# Testaus

Pelin luokkia on testattu automatisoidusti unittest-kirjastolla. Lisäksi mock-kirjastoa on käytetty suhteellisen paljon, koska peli käyttää paljon pygamen omia metodeja ja luokkia. Peliä on testattu myös manuaalisesti järjestelmätasolla. 

### Testikattavuus

Pelin kokonaiskattavuus on 79% ja haarautumakattavuus 75%.

![](/.dokumentaatio/kuvat/coverage_report.png)

Kattavuuden ulkopuolelle on jätetty vakiomuuttujia sisältävä config.py ja valikkokäyttöliittymästä vastaava ui/ui.py. 

