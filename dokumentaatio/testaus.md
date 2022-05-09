# Testaus

[![codecov](https://codecov.io/gh/2laJ2/MazeTime/branch/main/graph/badge.svg?token=obIX1oXHC8)](https://codecov.io/gh/2laJ2/MazeTime)

Testikattavuus näkyy ylläolevassa badgessa prosenttilukuna. Alunperin ongelmana oli suorittaa testit siten, ettei Maze-olion antama valikko käynnisty tai Pygame-ikkuna avaudu testeissä. Sovelluksen visualisointi Pygamella ja eri algoritmit piti jakaa omiin luokkiinsa, jotta testaus olisi mahdollista. Testeissä käytetään apuna Pythonin unittest-moduulin mock-kirjastoa. Testit löytyvät src/tests/ -kansiosta. 

Labyrintin rakentavien algoritmien ja apumetodien oikeanlaista toimintaa mittaavia testejä on tällä hetkellä 18. Visualisoinnin hoitavan Maze-luokan yksittäisten metodien toimintaa ei ole testattu. Maze-luokan testaaminen ei liene täysin välttämätöntä, mutta jos sattumalta löydän selkeää ohjemateriaalia, niin ainakin muutaman testin voisi kokeilumielessä kirjoittaa, jos ehdin.

_Comparison.py_-luokassa on testejä, joilla vertaillaan Growing Tree -algoritmin viidellä eri variaatiolla luotuja erilaisia rakenteita Aldous-Broderin ja Wilsonin algoritmilla luotujen labyrinttien kanssa. Ohjelma ajaa nämä testit automaattisesti ja ilmoittaa tulokset komentoruudulla, kun käyttäjän valitseman algoritmin avulla luodun labyrintin visualisointi on valmis. Testit laskevat konfiguraatiotiedoston parametreilla ja käyttäjän valitseman algoritmin avulla luodun labyrintin ruuduista umpikujat, neljän käytävän risteykset, kolmen käytävän risteykset, mutkat, vaakasuorat käytävät ja pystysuorat käytävät ja tulostaa laskemiensa ruutujen lukumäärät komentoruudulla.

Seuraavaksi luon umpikujien, pystysuorien käytävien ja vaakasuorien käytävien pituutta mittaavat testit.

Yksikkötestien ajaminen onnistuu käynnistämällä virtuaalitila juurikansiosta antamalla komentorivillä komento
```
poetry shell
```
ja tämän jälkeen ajamalla testit komennolla

```
pytest src
```