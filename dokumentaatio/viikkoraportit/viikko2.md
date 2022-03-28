# Viikkoraportti 2
Löysin visualisointiin sopivan koodin. Muokkasin labyrintin värimaailmaa.

Alkuperäisessä koodissa käytetään metodia, joka luo labyrintin depth-first search backtracking -algoritmin iteratiivisella lähestymistavalla.

Kirjoitin oman toteutuksen Aldous-Broderin algoritmia käyttävälle metodille, joka luo labyrintin. Käytin metodin luomisessa Wikipediasta löytyvää [Aldous-Broderin algoritmia](https://en.wikipedia.org/wiki/Maze_generation_algorithm#Aldous-Broder_algorithm). Videosta ["8 Maze Generating Algorithms in 3 Minutes"](https://www.youtube.com/watch?v=sVcB8vUFlmU) oli tässä huomattavaa apua.

Metodi käyttää parametrina annettua seed-arvoa satunnaisluvun luontiin arpoessaan ruudun, josta labyrintin piirtäminen aloitetaan. Näin voidaan toistaa joka kerta samanlainen (pseudo)satunnainen labyrintti samalla seed-arvolla. Labyrinttia ei tarvitse tallettaa sellaisenaan, koska labyrintin voi myöhemmin piirtää uudelleen täsmälleen samanlaisena samaa seed-arvoa käyttäen. Koska labyrintin lähtöpiste on satunnainen, ei ole mahdollista käyttää alkuperäisen lähteen labyrintin ratkaisun visualisointiin käytettyä metodia sellaisenaan. Labyrintin ratkaisuun voi toki tehdä yleisesti tunnettua labyrintin ratkaisuun käytettyä algoritmia soveltavan metodin. Työtunteja kertyi Aldous-Broderin algoritmia käyttävän metodin koodaamiseen mennessä 9,5.

Kirjoitin oman toteutuksen Wilsonin algoritmia käyttävälle metodille, joka luo abyrintin. Käytin metodin luomisessa Wikipediasta löytyvää [Wilsonin algoritmia](https://en.wikipedia.org/wiki/Maze_generation_algorithm#Wilson's_algorithm). Videosta ["8 Maze Generating Algorithms in 3 Minutes"](https://www.youtube.com/watch?v=sVcB8vUFlmU) oli myös tässä huomattavaa apua. Myös tämä metodi käyttää parametrina annettua seed-arvoa.

Muokkasin algoritmia sen verran, että ensimmäinen polku, joka päättyy oman itsensä umpikujaan, piirretään aina osaksi labyrinttia. Olisi ollut tarpeettoman hidasta odotella, josko ensimmäinen polku jonain päivänä ehkä osuisi takaisin lähtöpisteeseen. Erityisen hankalaa Wilsonin algoritmia käyttävän metodin toteuttamisessa oli koodata vaihe, jossa uusi reitti piirretään osaksi labyrinttia vain siinä tapauksessa, että polku ei pääty oman itsensä muodostamaan umpikujaan (missä tapauksessa polku tyhjennetään). Wilsonin algoritmia käyttävän metodin koodaamiseen kului noin 12 tuntia.

Päivitin vaatimusmäärittelyä, toteutusdokumenttia, luokkajakoa, sekä lisäsin Pygamen Poetryn riippuvuuksiin ja tarkistin alustavasti koodin ulkoasua pylintin avulla. Tähän kului noin 4,5 tuntia. Yhteensä koko viikkopalautukseen kului noin 26 tuntia.

Seuraavaksi refraktoroin ohjelman koodia ja päivitän metodien testauksen, joka ei tällä hetkellä sovellu Pygamea käyttävälle ohjelmalle. Tähän en toistaiseksi ole löytänyt riittävän selkeää ohjemateriaalia.