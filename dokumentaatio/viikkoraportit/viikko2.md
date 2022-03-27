# Viikkoraportti 2
Löysin visualisointiin sopivan koodin. Muokkasin labyrintin värimaailmaa.

Alkuperäisessä koodissa käytetään metodia, joka luo labyrintin depth-first search backtracking -algoritmin iteratiivisella lähestymistavalla.

Kirjoitin oman toteutuksen Aldous-Broderin algoritmia käyttävälle metodille, joka luo labyrintin. Käytin metodin luomisessa Wikipediasta löytyvää [Aldous-Broderin algoritmia](https://en.wikipedia.org/wiki/Maze_generation_algorithm#Aldous-Broder_algorithm). Videosta ["8 Maze Generating Algorithms in 3 Minutes"](https://www.youtube.com/watch?v=sVcB8vUFlmU) oli tässä huomattavaa apua.

Metodi käyttää seed-arvoa satunnaisluvun luontiin arpoessaan ruudun, josta labyrintin piirtäminen aloitetaan. Näin voidaan toistaa joka kerta samanlainen (pseudo)satunnainen labyrintti samalla seed-arvolla. Labyrinttia ei tarvitse tallettaa sellaisenaan, koska labyrintin voi myöhemmin piirtää uudelleen täsmälleen samanlaisena samaa seed-arvoa käyttäen. Koska labyrintin lähtöpiste on satunnainen, ei ole mahdollista käyttää alkuperäisen lähteen labyrintin ratkaisun visualisointiin käytettyä metodia sellaisenaan. Labyrintin ratkaisuun voi toki tehdä yleisesti tunnettua labyrintin ratkaisuun käytettyä algoritmia soveltavan metodin. Työtunteja kertyi AB:n koodaamiseen mennessä 9,5.

Päivitin vaatimusmäärittelyä, toteutusdokumenttia, luokkajakoa, sekä lisäsin Pygamen Poetryn riippuvuuksiin ja tarkistin alustavasti koodin ulkoasua pylintin avulla. Tähän kului noin 3 tuntia.

Seuraavaksi teen oman toteutuksen jollain toisella algoritmilla (joka parhaimmin soveltuu käytettyyn visualisointiin) ja päivitän testauksen.