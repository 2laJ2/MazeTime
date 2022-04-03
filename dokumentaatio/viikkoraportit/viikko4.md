# Viikkoraportti 4
Kirjoitin Growing Tree -algoritmia käyttävän metodin valmiiksi. Käyttäjä voi valita viidestä eri variaatiosta haluamansa. Koodissa oli pieni bugi, jonka löytäminen ei ollut helppoa, koska algoritmi on rakenteeltaan niin monimutkainen, että Visual Studio Core antoi ns. perättömiä virhemerkintöjä. Työtunteja kului noin 3,5.

Seuraavaksi pyrin muokkaamaan testejä ja luokkarakennetta siten, että voin testata labyrintin algoritmilla rakentavien metodien toimivuutta. 

Tämän jälkeen erilaisten rakenteiden luominen Growing Tree -algoritmin viidellä eri variaatiolla ja niiden vertailu Aldous-Broderin ja Wilsonin algoritmilla luotujen labyrinttien kanssa olisi ehkä seuraava vaihe. Tätä silmälläpitäen voisi olla kannattavaa käyttää seed-arvoa myös Growing Tree -labyrinttien luomisessa.

Lopuksi Wilsonin algoritmista voisi poistaa labyrintin rakentamista nopeuttavan muokkauksen. Wilsonin metodin visualisointia voisi myös selkeyttää, esim. käyttämällä uuden polun luomiseen ennen labyrintin osaksi liittämistä aina uutta väriä, joko satunnaisesti tai järjestyksessä (esim. liila, sininen, vihreä, keltainen, oranssi, punainen). Tarkoituksena ei kuitenkaan ole optimoida labyrintin rakentamiseen kuluvaa aikaa, jolloin värin vaihtamiseen mahdollisesti kuluva lisäaika on epäolennaista.