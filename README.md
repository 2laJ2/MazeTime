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

### Komentorivitoiminnot

#### Ohjelman käynnistys

Ohjelman käynnistys onnistuu komentoriviltä projektin juurihakemistossa, missä kansio src ja pyproject.toml-tiedosto sijaitsevat komennolla

```
python3 src/index.py
```

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