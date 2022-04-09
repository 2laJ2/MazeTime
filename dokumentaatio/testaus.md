# Testaus

[![codecov](https://codecov.io/gh/2laJ2/MazeTime/branch/main/graph/badge.svg?token=obIX1oXHC8)](https://codecov.io/gh/2laJ2/MazeTime)

Testikattavuus näkyy ylläolevassa badgessa prosenttilukuna. Tällä hetkellä testikattavuus ei anna oikeaa kuvaa testauksessa, koska testaus on vielä alkuvaiheessa ja toimivia testejä on vasta kahdeksan. Ongelmana oli suorittaa testit siten, ettei Maze-olion antama valikko käynnisty tai Pygame-ikkuna avaudu testeissä. Sovelluksen visualisointi Pygamella ja eri algoritmit piti jakaa omiin luokkiinsa, jotta testaus olisi mahdollista. Testeissä käytetään apuna Pythonin unittest-moduulin mock-kirjastoa. Testit löytyvät src/tests/ -kansiosta. 

Seuraavaksi lisään uusia testejä mock-kirjastoa apuna käyttäen; tarkoituksena testata labyrintin rakentavien algoritmien oikeanlainen toiminta ja mahdollisesti visualisoinnin hoitavan Maze-luokan yksittäisten metodien toiminta. Maze-luokan testaaminen ei liene täysin välttämätöntä, mutta jos sattumalta löydän selkeää ohjemateriaalia, niin ainakin muutaman testin voisi kokeilumielessä kirjoittaa, jos ehdin.

Tämän jälkeen Growing Tree -algoritmin viidellä eri variaatiolla luotujen erilaisten rakenteiden vertailu Aldous-Broderin ja Wilsonin algoritmilla luotujen labyrinttien kanssa on seuraava vaihe.

Testien ajaminen onnistuu käynnistämällä virtuaalitila juurikansiosta antamalla komentorivillä komento
```
poetry shell
```
ja tämän jälkeen ajamalla testit komennolla

```
pytest src
```