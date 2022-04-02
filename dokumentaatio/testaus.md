# Testaus

[![codecov](https://codecov.io/gh/2laJ2/MazeTime/branch/main/graph/badge.svg?token=obIX1oXHC8)](https://codecov.io/gh/2laJ2/MazeTime)

Testikattavuus näkyy ylläolevassa badgessa prosenttilukuna. Tällä hetkellä testikattavuus ei anna oikeaa kuvaa testauksessa, koska testaus on vielä alkuvaiheessa ja toimivia testejä on vasta kaksi. Testit löytyvät src/tests/ -kansiosta. 

Testauksessa on ongelmaksi noussut se, että koska sovellus käyttää visualisointiin Pygamea, niin käyttöliittymä ja visualisointi tulisi jakaa eri luokkiin kuin itse labyrintin rakentamisen toteuttavat algoritmit, jotta testauksen saisi toimimaan mielekkäällä tavalla. Tämä työ on vielä toistaiseksi kesken.

Toistaiseksi testien ajaminen onnistuu käynnistämällä virtuaalitila juurikansiosta antamalla komentorivillä komento
```
pytest src
```
Tämän jälkeen ohjelma käynnistää Pygame-ikkunan. Kun käyttäjä klikkaa oikean yläkulman punaista palloa, jossa on rasti, yhden kerran jokaista testiä kohden, poetry ajaa jokaisen klikkauksen jälkeen yhden testin. Kun kaikki testit on tehty, testitulokset näkyvät komentorivillä.

Tavoitteena on muokata testausta siten, että Pygame-ikkuna ei avaudu ja testit voisi ajaa läpi ilman käyttäjän klikkailuja tavalliseen tapaan. Tämän lisäksi tulisi löytää toimiva tapa testata itse labyrintin rakentamisen toteuttavat algoritmit. 