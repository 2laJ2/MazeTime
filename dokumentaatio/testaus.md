# Testaus

[![codecov](https://codecov.io/gh/2laJ2/MazeTime/branch/main/graph/badge.svg?token=obIX1oXHC8)](https://codecov.io/gh/2laJ2/MazeTime)

Testikattavuus näkyy ylläolevassa badgessa prosenttilukuna. Tällä hetkellä testikattavuus ei anna oikeaa kuvaa testauksessa, koska testaus on vielä alkuvaiheessa ja toimivia testejä on vasta kolme. Testeissä käytetään apuna Pythonin unittest-moduulin mock-kirjastoa. Testit löytyvät src/tests/ -kansiosta. 

Testien ajaminen onnistuu käynnistämällä virtuaalitila juurikansiosta antamalla komentorivillä komento
```
poetry shell
```
ja tämän jälkeen ajamalla testit komennolla

```
pytest src
```