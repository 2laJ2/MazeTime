# Toteutus

## Ohjelman toiminta

Ohjelma on toteutettu Pythonilla ja visualisoinnissa on käytetty Pythonin Pygame-kirjastoa. Ohjelma käynnistetään tiedoston _index.py_ kautta, jolloin _maze.py_-moduulissa oleva Maze-olio luo visualisoinnin Pygame-kirjaston avulla sekä antaa käyttäjälle komentoikkunassa valikon, jonka avulla voi valita, millä algoritmilla labyrintti rakennetaan. Pygamelle annettavat muuttujat on määritelty _config.py_-tiedostossa.

Käyttäjän tehtyä haluamansa valinnat main_menu -metodi luo uuden Pygame-ikkunan metodilla reset_grid ja piirtää siihen valkoisen ruudukon metodilla build_grid. Tämän jälkeen main_menu luo uuden, käyttäjän valitseman algoritmin mukaisen algoritmiolion injektoimalla Maze-olion uudelle algoritmioliolle. Lopuksi main_menu käynnistää labyrintin rakentamisen suorittamalla algoritmiolion labyrintin rakentavan (pää)metodin. Kunkin algoritmiolion labyrintin rakentavalla päämetodilla on omat tarpeelliset apumetodinsa. Kun labyrintti on valmis, main_menu antaa komentoikkunassa valikon uudelleen, josta käyttäjä voi uudelleen valita haluamansa toiminnon, joko uuden labyrintin tai ohjelman lopetuksen. Kummassakin tapauksessa ohjelma sulkee Pygame-ikkunan. Jos käyttäjä valitsee uuden labyrintin, ohjelma avaa uuden Pygame-ikkunan.

## Käytetyt algoritmit

### Growing Tree eli virittävä puu

Growing Tree -algoritmilla on mahdollista luoda rakenteeltaan erilaisia labyrintteja.
1. Valitaan aloitusruutu, lisätään ruutu käytyjen ruutujen luetteloon ja kuljettuun polkuun ja piirretään labyrinttiin.
2. Toistetaan niin kauan, kuin labyrintissa on jäljellä ruutuja, joissa ei ole vielä käyty:
    1. Valitaan satunnainen naapuri, jossa ei ole vielä käyty:
        1. Poistetaan nykyisen ruudun ja naapuriruudun välinen seinä.
        2. Lisätään naapuri käytyjen ruutujen luetteloon.
        3. Merkitään naapuriruutu nykyiseksi ruuduksi.
        4. Lisätään ruutu kuljettuun polkuun.
    2. Jos kaikissa naapureissa on käyty, mutta labyrintissa on jäljellä ruutuja, joissa ei ole vielä käyty:
        1. Poistetaan nykyinen ruutu kuljetusta polusta.
        2. Valitaan polusta ruutu.

Algoritmi rakentaa virittävän puun, jossa kaikki ruudut ovat yhteydessä toisiinsa. Muodostuvan labyrintin rakenteeseen vaikuttaa se, millä tavalla umpikujaan tullessa valitaan jo kuljetusta polusta ruutu (ylläolevassa algoritmin kuvauksessa kohdassa 2.ii.b). Valinnan voi toteuttaa esim. seuraavin tavoin:

* Viimeiseksi polkuun lisätty eli edellinen ruutu:
    Algoritmi muuttuu rekursiiviseksi DFS-algoritmiksi (recursive backtracker).
* Satunnainen valinta kuljetusta polusta:
    Algoritmi käyttäytyy samankaltaisesti muttei täysin identtisesti kuin Primin algoritmi.
* Ensimmäiseksi polkuun lisätty ruutu:
    Labyrintin käytävissä on hyvin vähän haarautumia, jopa vähemmän kuin Primin algoritmilla luodussa labyrintissä.
* Yleensä viimeiseksi lisätty eli edellinen ruutu, mutta toisinaan satunnainen ruutu:
    Labyrintissä on lyhyitä käytäviä, joissa on paljon haarautumia.
* Satunnainen ruutu viimeiseksi lisättyjen ruutujen joukosta:
    Labyrintissä on pitkiä käytäviä, joissa on vähän haarautumia.

### Aldous-Broder

Aldous-Broderin algoritmilla voidaan luoda rakenteeltaan yhtenäisiä ja tasaisia (uniform) labyrintteja ja virittäviä puita. 
1. Valitaan satunnainen ruutu, merkitään se nykyiseksi ruuduksi ja lisätään käytyjen ruutujen luetteloon.
2. Toistetaan niin kauan, kuin labyrintissä on jäljellä ruutuja, joissa ei ole vielä käyty:
    1. Valitaan satunnainen naapuri.
    2. Jos tässä naapurissa ei ole vielä käyty:
        1. Poistetaan nykyisen ruudun ja naapuriruudun välinen seinä.
        2. Lisätään naapuriruutu käytyjen ruutujen luetteloon.
        3. Merkitään naapuriruutu nykyiseksi ruuduksi.
    3. Jos satunnaisesti valitussa naapurissa on jo käyty, valitaan uusi satunnainen naapuri.
3. Kun kaikissa ruuduissa on käyty, algoritmi on valmis.

### Wilson loop erased random walk

Myös Wilsonin algoritmilla voidaan luoda rakenteeltaan yhtenäisiä ja tasaisia labyrintteja. Wilsonin algoritmilla on se ominaisuus, että sillä, millä perusteella aloitusruudut valitaan - voidaan yhtä hyvin valita satunnainen ruutu kuin vaikkapa ensimmäinen tyhjä ruutu vasemmalta oikealle ja alhaalta ylös - ei ole vaikutusta labyrintin rakenteeseen.
1.  Valitaan aloitusruutu. Lisätään aloitusruutu polkuun, poistetaan se käymättömien ruutujen luettelosta ja merkitään osaksi labyrinttia.
2.  Toistetaan niin kauan, kuin labyrintissä on jäljellä ruutuja, joissa ei ole käyty:
    1. Valitaan satunnainen naapuri.
    2. Jos tässä naapurissa ei ole vielä käyty:
        1. Lisätään naapuri nykyisen polun listalle.
        2. Poistetaan naapuri käymättömien ruutujen luettelosta.
    3. Jos tässä naapurissa on jo käyty:
        1. Jos naapuri on osa nykyistä polkua:
            1. Kuljetun polun ruudut lisätään takaisin käymättömien ruutujen luetteloon.
            2. Polku tyhjennetään.
        2. Jos naapuri on osa labyrinttiä tai labyrintin ensimmäinen aloitusruutu:
            1. Polku lisätään labyrinttiin:
                1. Poistetaan kuljetun polun ruutujen väliset seinät.
                2. Poistetaan ruudut käymättömien ruutujen luettelosta.
            2. Polku tyhjennetään. 
                
## Algoritmien toteutus luokkien avulla

### Mysteerimaze-luokka

Konstruktori: Mysteerimaze(Maze-olio, labyrintin leveys, labyrintin korkeus, ruudun leveys, polku-lista)

#### Metodit:

1. gt_always_last(stack, x, y):
* apumetodi, kun option = 1: valitsee viimeisimmän lisätyn ruudun ja poistaa sen pinosta
* parametrina annetaan pino ja nykyisen ruudun koordinaattien x- ja y-arvot
* ottaa talteen viimeisimmän ruudun koordinaatit
* poistaa viimeisimmän ruudun koordinaatit pinosta 
* palauttaa pinon ja viimeisimmän ruudun koordinaattien x- ja y-arvot
2. gt_always_random(stack, x, y):
* apumetodi, kun option = 2: poistaa ruudun pinosta ja valitsee pinosta satunnaisen ruudun
* parametrina annetaan pino ja nykyisen ruudun koordinaattien x- ja y-arvot
* poistaa viimeisimmän ruudun koordinaatit pinosta
* valitsee pinosta satunnaisen ruudun
* palauttaa pinon ja satunnaisesti valitun ruudun koordinaattien x- ja y-arvot
3. gt_always_first(stack, x, y):
* apumetodi, kun option = 3: poistaa ruudun pinosta ja valitsee pinon ensimmäisen ruudun
* parametrina annetaan pino ja nykyisen ruudun koordinaattien x- ja y-arvot
* poistaa viimeisimmän ruudun koordinaatit pinosta
* valitsee pinon pohjalta ensimmäisen ruudun
* palauttaa pinon ja ensimmäisen ruudun koordinaattien x- ja y-arvot
4. gt_usually_last_occasionally_random(stack, x, y):
* apumetodi, kun option = 4: poistaa ruudun pinosta ja valitsee yleensä viimeisimmän, välillä satunnaisen ruudun pinosta
* parametrina annetaan pino ja nykyisen ruudun koordinaattien x- ja y-arvot
* valitsee satunnaisen luvun väliltä 1 - 5
* jos luku on yksi, valitsee satunnaisen ruudun pinosta (20% tapauksista)
* muussa tapauksessa ottaa talteen viimeisimmän ruudun koordinaatit ja poistaa viimeisimmän ruudun koordinaatit pinosta 
* palauttaa pinon ja valitun ruudun koordinaattien x- ja y-arvot
5. gt_random_among_last_ones(stack, x, y):
* apumetodi, kun option = 5: poistaa ruudun pinosta ja valitsee satunnaisen ruudun viimeisten ruutujen joukosta
* parametrina annetaan pino ja nykyisen ruudun koordinaattien x- ja y-arvot
* poistaa viimeisimmän ruudun koordinaatit pinosta
* laskee pinon koon ja jakaa tämän neljällä, jos jakolaskun tulos ei ole kokonaisluku, antaa tulokseksi desimaaliluvun kokonaiset luvut. Esim. 10/4 = 2,5, antaa tuloksen 2.
* valitsee viimeisimpien ruudun joukosta satunnaisen ruudun, esim. pinossa 10 ruutua, valitsee 10 - 2 = 8 viimeisimmästä ruudusta satunnaisen ruudun
* palauttaa pinon ja valitun ruudun koordinaattien x- ja y-arvot
6. carve_mysteerimaze(seed, option):
* metodi, joka luo parametrina annetuilla seed- ja option-arvoilla labyrintin
* tallentaa labyrintin sanakirjamuodossa (dictionary): järjestyksessä oleva lista labyrintin ruuduista, avaimena koordinaatit (x,y) x:n arvoilla 1 - x_max ja y:n arvoilla 1 - y_max ja arvona luettelo seinistä (1, 1, 1, 1), jolloin ruutua ympäröi seinä järjestyksessä vasen, oikea, ylös, alas. Pythonin uusin versio tallentaa sanakirjan järjestyksessä listana.
7. get_visited():
* testauksessa käytetty metodi, joka palauttaa labyrintin

### Abmaze-luokka

Konstruktori: Abmaze(Maze-olio, labyrintin leveys, labyrintin korkeus, ruudun leveys, polku-lista)

#### Metodit:

1. carve_AB_maze(seed):
* metodi, joka luo parametrina annetulla seed-arvolla labyrintin
* tallentaa labyrintin sanakirjamuodossa (dictionary): järjestyksessä oleva lista labyrintin ruuduista, avaimena koordinaatit (x,y) x:n arvoilla 1 - x_max ja y:n arvoilla 1 - y_max ja arvona luettelo seinistä (1, 1, 1, 1), jolloin ruutua ympäröi seinä järjestyksessä vasen, oikea, ylös, alas. 
2. get_visited():
* testauksessa käytetty metodi, joka palauttaa labyrintin

### Wilson-luokka

Konstruktori: Wilson(Maze-olio, labyrintin leveys, labyrintin korkeus, ruudun leveys, polku-lista)

#### Metodit:

1. reverse_stack_builder(x_max, y_max):
* apumetodi, jolla luodaan lista ruuduista, joissa ei ole käyty
* parametrina annetaan luotavan labyrintin suurimmat x- ja y-arvot
* palauttaa listan sanakirjamuodossa (dictionary) labyrintin ruuduista avaimena koordinaatit (x,y) x:n arvoilla 1 - x_max ja y:n arvoilla 1 - y_max ja arvona luettelo seinistä (1, 1, 1, 1), jolloin ruutua ympäröi seinä järjestyksessä vasen, oikea, ylös, alas. 
2. wilson_path(solution, a, b):
* apumetodi, jolla liitetään viimeksi kuljettu polku labyrinttiin ja tyhjennetään polku
* parametrina annetaan viimeksi kuljettu polku ja polun ensimmäisen ruudun koordinaatit (a,b)
* käy järjestyksessä läpi polun aloitusruudusta (a,b) alkaen listalle tallennetut suuntaohjeet ja poistaa ruutujen väliset seinät muuttamalla ko. seinille annetut arvot 1 (seinä) arvoksi 0 (avoin) - esim. kuljettaessa ruudusta a oikealle ruutuun b muutetaan ruudun a oikeanpuoleisen seinän arvoksi 0 ja ruudun b vasemmanpuoleisen seinän arvoksi 0 muiden seinien arvojen pysyessä ennallaan
* palauttaa tyhjän polun
3. carve_Wilson_maze(seed):
* metodi, joka luo parametrina annetulla seed-arvolla labyrintin
* luo listan käymättömistä ruuduista apumetodin rever_stack_builder avulla
* liittää kuljetun polun osaksi labyrinttia apumetodin wilson_path avulla
* tallentaa kuljetun reitin koordinaatit seinäluetteloineen (sanakirjamuotoiseen) listaan, joka voidaan palauttaa metodin get_visited avulla
4. get_visited():
* testauksessa käytetty metodi, joka palauttaa labyrintin

### Comparison-luokka

Labyrintin rakentamiseen käytettyjen algoritmien suorituskykyä ja labyrinttien rakenteita vertaileva luokka

Konstruktori: Comparison(algoritmiolio)

#### Metodit:

1. test_running_time
* mittaa algoritmiin kuluvan keskimääräisen ajan valituilla parametreilla kolmen ajon perusteella
* ajan kulumiseen vaikuttaa Pygamen visualisointi
2. jarjesta_ruudut_pystysuora(visited)
* metodi, joka järjestää ruudut ensisijaisesti x-koordinaatin, toissijaisesti y-koordinaatin perusteella
* parametrina annetaan visited-lista
* palauttaa labyrintin ruudut järjestyksessä ylhäältä alas sarake kerrallaan vasemmalta oikealle
3. jarjesta_ruudut_vaakasuora(visited)
* metodi, joka järjestää ruudut ensisijaisesti y-koordinaatin, toissijaisesti x-koordinaatin perusteella
* parametrina annetaan visited-lista
* käyttää metodia muodosta_y_koordinaatti_lista apuna luodessaan uuden listan visited-listasta
* palauttaa labyrintin ruudut järjestyksessä vasemmalta oikealle ylhäältä alas rivi kerrallaan 
4. muodosta_x_koordinaatti_lista
* metodi, joka luo listan (x, y) koordinaateista ensisijaisesti x-koordinaatin, toissijaisesti y-koordinaatin perusteella
* käyttää listan luomisessa Comparison-oliolle parametrina annetun algoritmiolion x_max-, y_max- ja w-arvoja
* palauttaa valmiin listan
5. muodosta_y_koordinaatti_lista
* metodi, joka luo listan (x, y) koordinaateista ensisijaisesti y-koordinaatin, toissijaisesti x-koordinaatin perusteella
* käyttää listan luomisessa Comparison-oliolle parametrina annetun algoritmiolion x_max-, y_max- ja w-arvoja
* palauttaa valmiin listan
6. test_lukumaarat(visited)
* metodi, joka laskee, kuinka moni labyrintin ruuduista on umpikuja, neljän käytävän risteys, kolmen käytävän risteys, mutka, vaakasuora käytävä tai pystysuora käytävä
* tulostaa laskemiensa ruutujen lukumäärät komentoruudulla
7. test_umpikujien_pituudet
* metodi, joka laskee umpikujien pituudet
8. test_kaytavien_pituudet
* metodi, joka laskee pystysuorien ja vaakasuorien käytävien pituudet
9. get_algoritmi
* metodi, joka palauttaa Comparison-oliolle annetun algoritmiolion

## Lähteet

- [Video: Python Maxe Generator Program, Davis MT](https://www.youtube.com/watch?v=Xthh4SEMA2o)
- [Lähdekoodi: Python Maze Generator Program, Davis MT](https://github.com/tonypdavis/PythonMazeGenerator/blob/master/pygame%20maze%20generator%20with%20solution.py)
- [Wikipedia, labyrinttien rakentamiseen käytetyt algoritmit](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Wikipedia, labyrinttien ratkaisemiseen käytetyt algoritmit](https://en.wikipedia.org/wiki/Maze-solving_algorithm)
- [Lisätietoa labyrinttien rakentamiseen liittyvistä koodeista](http://www.astrolog.org/labyrnth/algrithm.htm)
- [Video: 8 Maze Generating Algorithms in 3 Minutes, Ready Set Python](https://www.youtube.com/watch?v=sVcB8vUFlmU)
- [Under the Hood, The Buckblog, Jamis Buck](https://weblog.jamisbuck.org/under-the-hood/)
