# Testaus

[![codecov](https://codecov.io/gh/2laJ2/MazeTime/branch/main/graph/badge.svg?token=obIX1oXHC8)](https://codecov.io/gh/2laJ2/MazeTime)

Testikattavuus näkyy ylläolevassa badgessa prosenttilukuna. Alunperin ongelmana oli suorittaa testit siten, ettei Maze-olion antama valikko käynnisty tai Pygame-ikkuna avaudu testeissä. Sovelluksen visualisointi Pygamella ja eri algoritmit piti jakaa omiin luokkiinsa, jotta testaus olisi mahdollista. Testeissä käytetään apuna Pythonin unittest-moduulin mock-kirjastoa. Testit löytyvät src/tests/ -kansiosta. 

Labyrintin rakentavien algoritmien ja apumetodien oikeanlaista toimintaa mittaavia yksikkötestejä on 18. Visualisoinnin hoitavan _maze.py_-luokan yksittäisten metodien toimintaa ei ole testattu. _maze.py_-luokan testaaminen ei liene täysin välttämätöntä, eikä luokan testaamiseen jäänyt aikaa. Rakenteiden vertailun suorittavaa _comparison.py_-luokkaa ei ole yksikkötestattu, koska luokka on rakenteellisesti keskeneräinen ja sen testaaminen yksikkötesteillä on tästä syystä toistaiseksi haastavaa. Vertailutestien oikeanlainen toiminta ja labyrintin läpi kulkevan reitin kulku on empiirisesti havaittavissa labyrintin visualisoinnin perusteella. Jotta _comparison.py_-luokan kattava yksikkötestaus onnistuisi, luokka tulisi ensin refraktoroida.

_Comparison.py_-luokassa on testejä, joilla vertaillaan Growing Tree -algoritmin viidellä eri variaatiolla luotuja erilaisia rakenteita Aldous-Broderin ja Wilsonin algoritmilla luotujen labyrinttien kanssa. Ohjelma ajaa nämä testit automaattisesti ja ilmoittaa tulokset komentoruudulla, kun käyttäjän valitseman algoritmin avulla luodun labyrintin visualisointi on valmis. Testit laskevat konfiguraatiotiedoston parametreilla ja käyttäjän valitseman algoritmin avulla luodun labyrintin ruuduista umpikujat, neljän käytävän risteykset, kolmen käytävän risteykset, mutkat, vaakasuorat käytävät ja pystysuorat käytävät ja tulostaa laskemiensa ruutujen lukumäärät komentoruudulla. Luokassa on lisäksi testit umpikujien, pystysuorien käytävien ja vaakasuorien käytävien pituuden mittausta varten. 

Koska reitin piirtäminen perustuu Dead end-filling -algoritmin käyttöön, lisäsin metodin test_umpikujien_pituudet toiminnon, jossa metodi etenee umpikujan alusta umpikujan viimeiseen, risteystä edeltävään ruutuun kuten aiemminkin, mutta reitin löytämiseksi risteyksen umpikujan puoleinen aukko muutetaan seinäksi. Tällä on vaikutusta metodin tekemiin laskelmiin umpikujien pituudesta ja mutkaisuudesta, koska metodi käy joka kerta labyrintin läpi labyrintin tallennusjärjestyksessä, jolloin aiemmin suljetulla umpikujalla on vaikutusta myöhemmin läpikäytyyn umpikujaan. 

Tämän vuoksi, jos halutaan tarkempia tietoja umpikujien koordinaateista, pituuksista ja mutkista, koodista on joko kommentoitava pois risteyksien umpikujan puoleisten aukkojen muuttaminen seinäksi tai metodia on muokattava (tai kirjoitettava kokonaan uusi metodi) siten, että metodi selvittää ensin koko labyrintin umpikujien koordinaatit, umpikujien pituudet ja mutkat, ja vasta sen jälkeen muuttaa risteysten umpikujien puoleiset aukot seiniksi. Risteykset voisi tallentaa omaksi listakseen, jonka metodi muokkaa halutulla tavalla käytyään läpi koko labyrintin. 

Tämän harjoitustyön puitteissa metodin test_umpikujien_pituudet muokkaaminen ei liene oleellista. Luokka _comparison.py_ on rakenteellisesti keskeneräinen - mm. metodissa jarjesta_ruudut_vaakasuora on bugi (ei vaikuta laskelmiin), mistä johtuen metodissa test_kaytavien_pituudet on toisteisuutta (refraktorointi ei bugin vuoksi onnistu kokonaan), metodi test_umpikujien_pituudet puolestaan tekee sikinsokin aivan liian montaa asiaa ja tulisi rakentaa kokonaan uusiksi.

Huolimatta luokan _comparison.py_ rakenteellisesta keskeneräisyydestä testit toimivat ja labyrinttien rakenteellinen vertailu harjoitustyön vaatimusten puitteissa onnistui. 

## Rakenteiden vertailu

Vertailin labyrinttien rakenteita seuraavasti:
* neliönmuotoiset labyrintit 30 x 30 (900), 50 x 50 (2500), 70 x 70 (4900)
* suorakaiteenmuotoiset labyrintit 100 x 50 vs. 50 x 100 (5000), 20 x 10 vs. 10 x 20 (200)
* iso labyrintti algoritmeilla Wilson, Growing Tree variaatio 1 (recursive backtracker), Growing Tree variaatio 3 (aina ensimmäinen); 500 x 250 (125000)
* pieni labyrintti algoritmeilla Wilson, Growing Tree variaatio 1, Growing Tree variaatio 3; 100 x 50 (5000)

Kirjasin kustakin ajosta taulukkoon kuvaajia varten seuraavat tiedot:
* umpikujien lukumäärä
* neljän käytävän risteysten lukumäärä
* kolmen käytävän risteysten lukumäärä
* mutkien lukumäärä
* vaakasuorien ruutujen lukumäärä
* pystysuorien ruutujen lukumäärä
* reitin pituus
* reitillä olevien mutkien lukumäärä
Tallensin tiedot pdf-muodossa tiedostoon [MazeTime_Data.pdf](/dokumentaatio/MazeTime_Data.pdf) ja tein kustakin vertailusta kuvaajan.

Kirjasin taulukkoon myös:
* labyrintin vaaka- ja pystysuorien käytävien pituudet ja lukumäärät
* labyrintin läpi kulkevan reitin vaaka- ja pystysuorien käytävien pituudet ja lukumäärät
Näistä en tehnyt kuvaajia, koska määrät ja pituudet kasvoivat tasaisesti suhteessa labyrintin ruutujen määrään.

### Tehdyt havainnot

Kuvaajista voi nähdä seuraavat mielenkiintoiset ilmiöt:
1. neliönmuotoisilla labyrinteilla labyrintin läpi kulkevan reitin pituus ja mutkaisuus nousee tasaisesti koon kasvaessa kaikilla algoritmeilla, paitsi Growing Tree variaatio 1:llä (recursive backtracking) reitin pituus ja mutkaisuus nousevat todella paljon
2. suorakaiteenmuotoisilla pienehköillä labyrinteilla vaaka- tai pystysuoralla asennolla ei ole merkitystä labyrintin läpi kulkevan reitin pituuteen ja mutkaisuuteen, paitsi Growing Tree variaatio 1:llä (recursive backtracking), jolla vaakasuoralla labyrintillä reitin pituus ja mutkaisuus ovat selkeästi paljon suuremmat kuin pystysuoralla, samankokoisella labyrintilla
3. pienillä (5000) labyrinteillä Wilsonin, Growing Tree variaatio 1 ja Growing Tree variaatio 3 labyrintin läpi kulkevan reitin pituus on suhteessa labyrintin kokoon paljon pidempi ja mutkaisuus on suhteessa labyrintin kokoon paljon suurempi kuin samanmuotoisilla suurilla (125000) labyrinteilla

Tässä harjoitustyössä tehty eri algoritmeilla rakennettujen labyrinttien välinen rakenteellinen vertailu on suhteellisen suppea. Vertailun tarkoitus ei ole tuottaa tieteellistä tietoa, vaan lähinnä tutkia ohjelman toimivuutta pienimuotoisena labyrinttien rakentamiseen ja visualisointiin tarkoitettuna harjoitustyönä.

### Vertailujen pohjalta tehdyt kuvaajat

Aldous-Broderin algoritmilla rakennettujen labyrinttien vertailu. 

<img src="https://github.com/2laJ2/MazeTime/blob/main/dokumentaatio/kuvat/ABnelio.png" width="500"> <img src="https://github.com/2laJ2/MazeTime/blob/main/dokumentaatio/kuvat/ABsuorakaide.png" width="500">

Wilsonin algoritmilla rakennettujen labyrinttien vertailu.

<img src="https://github.com/2laJ2/MazeTime/blob/main/dokumentaatio/kuvat/Wnelio.png" width="500"> <img src="https://github.com/2laJ2/MazeTime/blob/main/dokumentaatio/kuvat/Wsuorakaide.png" width="500">

Growing Tree variaatio 1 (recursive backtracking) -algoritmilla rakennettujen labyrinttien vertailu. Reitin pituus ja mutkaisuus kasvavat todella paljon suhteessa neliönmuotoisen labyrintin kokoon. Vaakasuoran labyrintin reitin pituus ja mutkaisuus ovat suuremmat kuin pystysuoran labyrintin.

<img src="https://github.com/2laJ2/MazeTime/blob/main/dokumentaatio/kuvat/GT1nelio.png" width="500"> <img src="https://github.com/2laJ2/MazeTime/blob/main/dokumentaatio/kuvat/GT1suorakaide.png" width="500">

Growing Tree variaatio 2 -algoritmilla rakennettujen labyrinttien vertailu.

<img src="https://github.com/2laJ2/MazeTime/blob/main/dokumentaatio/kuvat/GT2nelio.png" width="500"> <img src="https://github.com/2laJ2/MazeTime/blob/main/dokumentaatio/kuvat/GT2suorakaide.png" width="500">

Growing Tree variaatio 3 -algoritmilla rakennettujen labyrinttien vertailu.

<img src="https://github.com/2laJ2/MazeTime/blob/main/dokumentaatio/kuvat/GT3nelio.png" width="500"> <img src="https://github.com/2laJ2/MazeTime/blob/main/dokumentaatio/kuvat/GT3suorakaide.png" width="500">

Growing Tree variaatio 4 -algoritmilla rakennettujen labyrinttien vertailu.

<img src="https://github.com/2laJ2/MazeTime/blob/main/dokumentaatio/kuvat/GT4nelio.png" width="500"> <img src="https://github.com/2laJ2/MazeTime/blob/main/dokumentaatio/kuvat/GT4suorakaide.png" width="500">

Growing Tree variaatio 5 -algoritmilla rakennettujen labyrinttien vertailu.

<img src="https://github.com/2laJ2/MazeTime/blob/main/dokumentaatio/kuvat/GT5nelio.png" width="500"> <img src="https://github.com/2laJ2/MazeTime/blob/main/dokumentaatio/kuvat/GT5suorakaide.png" width="500">

Wilson, Growing Tree variaatio 1 ja Growing Tree variaatio 3 -algoritmeilla rakennettujen labyrinttien vertailu isolla ja pienellä labyrintilla. Pienemmässä samanmuotoisessa labyrintissa reittien pituuus ja mutkaisuus on suhteessa labyrintin kokoon selvästi suurempi.

<img src="https://github.com/2laJ2/MazeTime/blob/main/dokumentaatio/kuvat/W_GT1_GT3_iso.png" width="500"> <img src="https://github.com/2laJ2/MazeTime/blob/main/dokumentaatio/kuvat/W_GT1_GT3_pieni.png" width="500">

## Ohjelman yksikkötestaus

### Yksikkötestien suorittaminen

Yksikkötestien ajaminen onnistuu käynnistämällä virtuaalitila juurikansiosta antamalla komentorivillä komento
```
poetry shell
```
ja tämän jälkeen ajamalla testit komennolla

```
pytest src
```

### Testauskattavuus

Testauskattavuutta voi tarkastella codecovin avulla:

[![codecov](https://codecov.io/gh/2laJ2/MazeTime/branch/main/graph/badge.svg?token=obIX1oXHC8)](https://codecov.io/gh/2laJ2/MazeTime)


