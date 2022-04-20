# Viikkoraportti 5
Refaktoroin koodia; nyt labyrintin koon määrittely tapahtuu nimenomaan konfiguraatiotiedoston _Config.py_:n avulla ja mystiset numerot on korvattu nimetyillä muuttujilla. Tämä helpottaa algoritmien testaamista. Työaikaa korjauksiin, sovelluksen toiminnan tarkistamiseen, vanhojen testien toiminnan tarkistamiseen ja dokumentoinnin päivittämiseen kului noin 2,5 tuntia.

Lisäsin mock-kirjaston avulla testit, joilla testataan, että algoritmi käy kaikissa labyrintin ruuduissa. Tarkistin koodin kirjoitusasua ja päivitin Pylintiä, jotta build ei hajoa Pylintin vuoksi, koska algoritmit ovat liian monimutkaisia ja pygamessa on rivejä, joita Pylint ei hyväksy.Tähän kului aikaa noin 3,5 tuntia.

Korjasin pieniä bugeja ja lisäsin kullekin algoritmille testausta helpottavan, labyrintin palauttavan metodin ja uusia testejä mock-kirjastoa apuna käyttäen; testit testaavat labyrintin rakentavien algoritmien oikeanlaisen toiminnan. Työaikaa kului 3 tuntia.
 
Seuraavaksi päivitän toteutus.md:n ja mahdollisesti lisään uusia testejä visualisoinnin hoitavan Maze-luokan yksittäisten metodien toiminnan testaamiseksi mock-kirjaston avulla. Maze-luokan testaaminen ei liene täysin välttämätöntä, mutta jos sattumalta löydän selkeää ohjemateriaalia, niin ainakin muutaman testin voisi kokeilumielessä kirjoittaa, jos ehdin. Tämän jälkeen päivitän testaus.md:n.

Tämän jälkeen Growing Tree -algoritmin viidellä eri variaatiolla luotujen erilaisten rakenteiden vertailu Aldous-Broderin ja Wilsonin algoritmilla luotujen labyrinttien kanssa on seuraava vaihe.

Lopuksi Wilsonin algoritmista voisi poistaa labyrintin rakentamista nopeuttavan muokkauksen (joka ei täysin noudata Wilsonin algoritmin erittäin hidasta alkuvaihetta).