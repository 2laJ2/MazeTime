# Käyttöohje

## Ohjelman asennus

Ohjelman voi kopioida omalle koneelle luomalla ensin kansion, johon repositorion haluaa kopioida. Tämän jälkeen siirrytään uuteen kansioon ja alustetaan git komentorivikomennolla

```
git init
```
Tämän jälkeen kopioidaan repositorio omalle koneelle komennolla 

```
git clone https://github.com/2laJ2/MazeTime
```
Sitten siirrytään uuteen kansioon MazeTime, projektin juurihakemistoon, missä kansio src ja pyproject.toml-tiedosto sijaitsevat ja alustetaan Poetry komennolla 

```
poetry install
```
### Ohjelman käynnistys

Seuraavaksi siirrytään virtuaaliympäristöön komennolla

```
poetry shell
```

Ohjelman käynnistys onnistuu komentoriviltä projektin juurihakemistossa, missä kansio src ja pyproject.toml-tiedosto sijaitsevat komennolla

```
python3 src/index.py
```

Kansiossa src sijaitsee konfiguraatiotiedosto _config.py_, jossa määritellään mm. avautuvan Pygame-ikkunan ja ohjelman piirtämän labyrintin koko. Algoritmit käyttävät konfiguraatiotiedostossa määriteltyjä visualisoinnin nopeusarvoja, joita voi halutessaan itse muuttaa tai vaihtaa hitaampaan tai nopeampaan. Konfiguraatiotiedostossa voi määritellä myös ns. seed-arvon, jota algoritmi käyttää valitessaan ruudun (pseudo)satunnaisesti. 

Samalla seed-arvolla algoritmi tekee joka kerta identtisen (pseudo)satunnaisen valinnan, jolloin samoilla leveys- ja korkeusarvoilla saadaan aina täsmälleen samanlainen labyrintti. Tämä helpottaa vertailujen tekemistä, kun satunnaisten valintojen satunnanvaraisuus ei vaikuta labyrintin rakenteeseen.

Käynnistyksen jälkeen ohjelma antaa komentoruudulla valikon, josta käyttäjä voi valita haluamansa algoritmin. Vaihtoehtoja on neljä:
1. Mysteerialgoritmi
2. Aldous-Broder
3. Wilson
4. Lopetus

Mysteerialgoritmi on Growing Tree -algoritmi. Jos käyttäjä valitsee vaihtoehdon yksi, ohjelma kysyy lukua yhdestä viiteen. Luvut tarkoittavat seuraavia Growing Tree -algoritmin variaatioita:
Tultaessa umpikujaan, algoritmi valitsee jo kuljetusta polusta ruudun, joka on
1. viimeiseksi polkuun lisätty eli edellinen ruutu: algoritmi muuttuu rekursiiviseksi DFS-algoritmiksi (recursive backtracker).
2. satunnainen valinta kuljetusta polusta: algoritmi käyttäytyy samankaltaisesti muttei täysin identtisesti kuin Primin algoritmi.
3. ensimmäiseksi polkuun lisätty ruutu: labyrintin käytävissä on hyvin vähän haarautumia, jopa vähemmän kuin Primin algoritmilla luodussa labyrintissä.
4. yleensä viimeiseksi lisätty eli edellinen ruutu, mutta toisinaan satunnainen ruutu: labyrintissä on lyhyitä käytäviä, joissa on paljon haarautumia.
5. satunnainen ruutu viimeiseksi lisättyjen ruutujen joukosta: labyrintissä on pitkiä käytäviä, joissa on vähän haarautumia.
Käyttäjän annettua numeron 1, 2, 3, 4 tai 5, ohjelma piirtää labyrintin näytölle avautuvaan Pygame-ikkunaan.

Lopuksi ohjelma suorittaa vertailevat laskelmat ja tulostaa seuraavat tulokset komentoruudulle:
* umpikujien lukumäärä
* neljän käytävän risteyksien lukumäärä
* kolmen käytävän risteyksien lukumäärä
* mutkien lukumäärä
* vaakasuorien käytäväruutujen lukumäärä
* pystysuorien käytäväruutujen lukumäärä
* labyrintin pystysuorien käytävien pituudet ja lukumäärät
* labyrintin vaakasuorien käytävien pituudet ja lukumäärät
* labyrintin umpikujien koordinaatit, mutkat ja pituus
* labyrintin läpi kulkevan reitin pituus
* labyrintin läpi kulkevan reitin koordinaatit luettelona
* labyrintin läpi kulkevan reitin pystysuorien käytävien pituudet ja lukumäärät
* labyrintin läpi kulkevan reitin vaakasuorien käytävien pituudet ja lukumäärät
* labyrintin läpi kulkevan reitin mutkien lukumäärä

Labyrintin umpikujien koordinaattien, mutkien ja pituuksien mittauksesta on kerrottu enemmän [testausdokumentissa](/dokumentaatio/testaus.md).

Kun ohjelma on valmis, ohjelma antaa valikon uudelleen komentoruudulla.

Labyrintin leveyttä, korkeutta, väriä, seed-arvoa tai visualisoinnin nopeuden säätäminen onnistuu lopettamalla ohjelma valinnalla q, avaamalla konfiguraatiotiedosto, tekemällä sinne halutut muutokset minkä jälkeen konfiguraatiotiedosto tallennetaan. Tämän jälkeen ohjelma käynnistetään uudelleen antamalla komentoruudulla komento

```
python3 src/index.py
```
### 

### Yksikkötestaus

Yksikkötestit suoritetaan komentoriviltä projektin juurihakemistossa siirtymällä ensin virtuaaliympäristöön komennolla

```
poetry shell
```
Tämän jälkeen koodin toimintaa tutkivien testien suoritus onnistuu komennolla

```
pytest
```
Koodin ulkoasun laatua tarkastelevien testien suoritus onnistuu komennolla

```
pylint src
```