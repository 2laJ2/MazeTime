# Viikkoraportti 4
Kirjoitin Growing Tree -algoritmia käyttävän metodin valmiiksi. Käyttäjä voi valita viidestä eri variaatiosta haluamansa. Koodissa oli pieni bugi, jonka löytäminen ei ollut helppoa, koska algoritmi on rakenteeltaan niin monimutkainen, että Visual Studio Core antoi ns. perättömiä virhemerkintöjä. Työtunteja kului noin 3,5.

Muutin luokkajakoa siten, että kukin algoritmi on oma luokkansa, jolle injektoidaan maze-olio. Erotin kunkin luokan omaan tiedoonsa. Muutin Growing Tree -algoritmia käyttävää metodia siten, että myös se käyttää parametrina annettua seed-arvoa. Lisäsin src-kansioon konfiguraatiotiedoston, jossa määritellään mm. värit, Pygamen avaaman ikkunan muuttujat ja labyrintin koko. Työtunteja kului noin 5.

Muokkasin testejä, luokkarakennetta ja metodeja siten, että voin testata labyrintin algoritmilla rakentavien metodien toimivuutta. Nyt testaus onnistuu komentoriviltä komennolla pytest ilman, että Pygame-ikkuna avautuu. Myös ohjelman käynnistys normaalisti komentoriviltä komennolla python3 src/index.py onnistuu ilman ylimääräisiä klikkailuja. Käytin testauksessa Pythonin unittest-moduulin mock-kirjastoa. Siirsin Wilsonin algoritmiä käyttävät, kahta apumetodia testaavat testit tiedostoon wilson_test.py. Loin Aldous-Broderin algoritmia käyttävälle luokalle tiedoston abmaze_test.py ja sinne yhden alustavan testin, jolla pääsen alkuun testien kirjoittamisessa mock-kirjaston avulla. Työtunteja kului noin 5.

Seuraavaksi lisään uusia testejä mock-kirjastoa apuna käyttäen.

Tämän jälkeen erilaisten rakenteiden luominen Growing Tree -algoritmin viidellä eri variaatiolla ja niiden vertailu Aldous-Broderin ja Wilsonin algoritmilla luotujen labyrinttien kanssa olisi ehkä seuraava vaihe.

Lopuksi Wilsonin algoritmista voisi poistaa labyrintin rakentamista nopeuttavan muokkauksen. Wilsonin metodin visualisointia voisi myös selkeyttää, esim. käyttämällä uuden polun luomiseen ennen labyrintin osaksi liittämistä aina uutta väriä, joko satunnaisesti tai järjestyksessä (esim. liila, sininen, vihreä, keltainen, oranssi, punainen). Tarkoituksena ei kuitenkaan ole optimoida labyrintin rakentamiseen kuluvaa aikaa, jolloin värin vaihtamiseen mahdollisesti kuluva lisäaika on epäolennaista.

Koodin ulkoasun tarkastelu Pylintin avulla antaa pitkän listan korjattavaa algoritmien monimutkaisuuden vuoksi. En osaa sanoa, mitä asialle pitäisi tehdä.