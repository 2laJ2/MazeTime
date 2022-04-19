# Viikkoraportti 5
Refaktoroin koodia; nyt labyrintin koon määrittely tapahtuu nimenomaan konfiguraatiotiedoston _Config.py_:n avulla ja mystiset numerot on korvattu nimetyillä muuttujilla. Tämä helpottaa algoritmien testaamista. Työaikaa korjauksiin, sovelluksen toiminnan tarkistamiseen, vanhojen testien toiminnan tarkistamiseen ja dokumentoinnin päivittämiseen kului noin 2,5 tuntia.

Seuraavaksi lisään uusia testejä mock-kirjastoa apuna käyttäen; tarkoituksena testata labyrintin rakentavien algoritmien oikeanlainen toiminta ja mahdollisesti visualisoinnin hoitavan Maze-luokan yksittäisten metodien toiminta. Maze-luokan testaaminen ei liene täysin välttämätöntä, mutta jos sattumalta löydän selkeää ohjemateriaalia, niin ainakin muutaman testin voisi kokeilumielessä kirjoittaa, jos ehdin.

Tämän jälkeen Growing Tree -algoritmin viidellä eri variaatiolla luotujen erilaisten rakenteiden vertailu Aldous-Broderin ja Wilsonin algoritmilla luotujen labyrinttien kanssa on seuraava vaihe.

Lopuksi Wilsonin algoritmista voisi poistaa labyrintin rakentamista nopeuttavan muokkauksen (joka ei täysin noudata Wilsonin algoritmin erittäin hidasta alkuvaihetta).