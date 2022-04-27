# MazeTime 

## Exploring mazes with Python

![GitHub Actions](https://github.com/2laJ2/MazeTime/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/2laJ2/MazeTime/branch/main/graph/badge.svg?token=obIX1oXHC8)](https://codecov.io/gh/2laJ2/MazeTime)

### Dokumentaatio

- [Määrittelydokumentti](/dokumentaatio/vaatimusmaarittely.md)
- [Käyttöohjedokumentti](/dokumentaatio/kayttoohje.md)
- [Testausdokumentti](/dokumentaatio/testaus.md)
- [Toteutusdokumentti](/dokumentaatio/toteutus.md)

#### Viikkoraportit

- [Viikkoraportti 1](/dokumentaatio/viikkoraportit/viikko1.md)
- [Viikkoraportti 2](/dokumentaatio/viikkoraportit/viikko2.md)
- [Viikkoraportti 3](/dokumentaatio/viikkoraportit/viikko3.md)
- [Viikkoraportti 4](/dokumentaatio/viikkoraportit/viikko4.md)
- [Viikkoraportti 5](/dokumentaatio/viikkoraportit/viikko5.md)
- [Viikkoraportti 6](/dokumentaatio/viikkoraportit/viikko6.md)

### Komentorivitoiminnot

#### Ohjelman asennus

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
#### Ohjelman käynnistys

Seuraavaksi siirrytään virtuaaliympäristöön komennolla

```
poetry shell
```

Ohjelman käynnistys onnistuu komentoriviltä projektin juurihakemistossa, missä kansio src ja pyproject.toml-tiedosto sijaitsevat komennolla

```
python3 src/index.py
```

Kansiossa src sijaitsee konfiguraatiotiedosto _config.py_, jossa määritellään mm. avautuvan Pygame-ikkunan ja ohjelman piirtämän labyrintin koko. Algoritmit käyttävät konfiguraatiotiedostossa määriteltyjä visualisoinnin nopeusarvoja, joita voi halutessaan itse muuttaa tai vaihtaa hitaampaan tai nopeampaan.

#### Testaus

Testit suoritetaan komentoriviltä projektin juurihakemistossa siirtymällä ensin virtuaaliympäristöön komennolla

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