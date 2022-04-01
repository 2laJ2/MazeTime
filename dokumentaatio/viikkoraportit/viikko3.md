# Viikkoraportti 3
Lisäsin sovellukseen metodin main_menu(), jonka avulla käyttäjä voi valita komentorivin valikosta algoritmin, jolla labyrintti rakennetaan. Valikosta voi valita myös ohjelman lopetuksen. Algoritmien keskinäinen vertailu on tarkoitus myöhemmin lisätä tähän toimintoon siten, että suoritettuaan käyttäjän valitseman algoritmin sovellus ilmoittaa ajon aikana kerättyjä vertailutietoja komentorivillä, minkä jälkeen käyttäjä voi valita uuden toiminnon.

Metodin main_menu() kirjoittamiseen ja ohjelman muokkaamiseen metodia varten kului noin 3.5 tuntia.

Pyrin refraktoimaan koodia siten, että Maze-luokalla on konstruktori, joka luo Pygamea käyttävän olion, joka käyttää luokan metodeja luodessaan labyrintin käyttäjän tekemien valintojen mukaan. Prosessissa on noussut esiin seuraavia ongelmia:
- Jos Maze-olion konstruktori käynnistää käyttäjälle näkyvän valikon kutsumalla metodia main_menu(), niin ohjelma toimii halutulla tavalla, mutta jos virtuaalitilassa ajetaan pytestit komentoriviltä komennolla pytest src, niin testit eivät mene läpi
- Jos taas index.py luo Maze-olion ja käynnistää valikon main_menu(), niin ohjelma avaa ikkunan, mutta pysähtyy, kunnes käyttäjä klikkaa yhden kerran ikkunan oikeassa yläkulmassa olevaa punaista ristipallukkaa. Jos virtuaalitilassa ajetaan pytestit, niin käyttäjän on klikattava samaista pallukkaa yhden kerran kutakin testiä varten, minkä jälkeen ikkuna sulkeutuu ja testitulos näkyy komentorivi-ikkunassa.
- Toistaiseksi en ole onnistunut testaamaan varsinaista algoritmimetodia, vaan ainoastaan kaksi Wilsonin algoritmin apumetodia. Pytest palauttaa olion, joten testaaminen ei ole vielä löytynyt sopivaa tapaa.

Refraktorointiin, taustamateriaalien etsintään ja kahden apumetodeja testaavan testin tekemiseen kului 5 tuntia.

Seuraavaksi päivitän testausdokumentin ja pyrin muokkaamaan testejä siten, että voin testata labyrintin algoritmilla rakentavien metodien toimivuutta.

Kolmantena algoritmina on tarkoitus toteuttaa [Growing Tree Algorithm](http://www.astrolog.org/labyrnth/algrithm.htm), koska sekä Aldous-Broderin että Wilsonin algoritmit luovat rakenteeltaan yhtenäisen labyrintin, mutta growing tree -algoritmilla voi luoda rakenteellisesti erilaisia labyrintteja. Erilaisten rakenteiden luominen ja niiden ottaminen mukaan vertailuun voisi olla seuraava vaihe.