# Testaus

[![codecov](https://codecov.io/gh/2laJ2/MazeTime/branch/main/graph/badge.svg?token=obIX1oXHC8)](https://codecov.io/gh/2laJ2/MazeTime)

Testikattavuus näkyy ylläolevassa badgessa prosenttilukuna. Alunperin ongelmana oli suorittaa testit siten, ettei Maze-olion antama valikko käynnisty tai Pygame-ikkuna avaudu testeissä. Sovelluksen visualisointi Pygamella ja eri algoritmit piti jakaa omiin luokkiinsa, jotta testaus olisi mahdollista. Testeissä käytetään apuna Pythonin unittest-moduulin mock-kirjastoa. Testit löytyvät src/tests/ -kansiosta. 

Labyrintin rakentavien algoritmien ja apumetodien oikeanlaista toimintaa mittaavia testejä on tällä hetkellä 18. Visualisoinnin hoitavan Maze-luokan yksittäisten metodien toimintaa ei ole testattu. Maze-luokan testaaminen ei liene täysin välttämätöntä, mutta jos sattumalta löydän selkeää ohjemateriaalia, niin ainakin muutaman testin voisi kokeilumielessä kirjoittaa, jos ehdin.

Seuraavaksi kirjoitan testejä, joilla vertaillaan Growing Tree -algoritmin viidellä eri variaatiolla luotuja erilaisia rakenteita Aldous-Broderin ja Wilsonin algoritmilla luotujen labyrinttien kanssa.

Testien ajaminen onnistuu käynnistämällä virtuaalitila juurikansiosta antamalla komentorivillä komento
```
poetry shell
```
ja tämän jälkeen ajamalla testit komennolla

```
pytest src
```