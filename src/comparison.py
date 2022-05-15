import time
from config import Config


"""
Labyrintin rakentamiseen käytettyjen algoritmien suorituskykyä ja labyrinttien rakenteita vertaileva luokka
"""
class Comparison():
    def __init__(self, algoritmi):
        self._algoritmi = algoritmi
        self._x_max = self._algoritmi._x_max
        self._y_max = self._algoritmi._y_max
        self._w = self._algoritmi._w
        self._maze = self._algoritmi._maze

    def test_running_time(self):# mittaa algoritmiin kuluvan keskimääräisen ajan valituilla parametreilla
        statistics = []
        result = 0
        for i in range (1, 3):
            start = time.time()
            self._algoritmi.carve_AB_maze(0)
            end = time.time()
            statistics.append(end - start)
        for i in statistics:
            result += i
        result /= len(statistics)
        return result

    def jarjesta_ruudut_pystysuora(self, visited):
        jarjestetty = sorted(visited.items(), key = lambda key: key [0])
        return jarjestetty

    def jarjesta_ruudut_vaakasuora(self, visited):
        new_visited = visited
        jarjestetty = {}
        koordinaatit_lista = self.muodosta_y_koordinaatti_lista()
        for each in koordinaatit_lista:
            x, y = each
            if (x, y) in new_visited:
                a, b, c, d = new_visited[(x, y)]
                jarjestetty[(x, y)] = (a, b, c, d)
        return jarjestetty

    def muodosta_x_koordinaatti_lista(self):
        x_list = []
        for i in range (1, self._x_max + 1):
            x_list.append(i*self._w)
        y_list = []
        for i in range (1, self._y_max + 1):
            y_list.append(i*self._w)
        koordinaatit_lista = []
        for x in range (0, len(x_list)):
            for y in range (0, len(y_list)):
                koordinaatit_lista.append((x_list[x],y_list[y]))
        return koordinaatit_lista

    def muodosta_y_koordinaatti_lista(self):
        x_list = []
        for i in range (1, self._x_max + 1):
            x_list.append(i*self._w)
        y_list = []
        for i in range (1, self._y_max + 1):
            y_list.append(i*self._w)
        koordinaatit_lista = []
        for y in range (0, len(x_list)):
            for x in range (0, len(y_list)):
                koordinaatit_lista.append((x_list[x],y_list[y]))
        return koordinaatit_lista

    # yleiskuvan labyrintin rakenteesta antava metodi
    def test_lukumaarat(self, visited, tulostus):
        new_visited = visited
        umpikujat = 0
        risteykset_4 = 0
        risteykset_3 = 0
        mutkat = 0
        kaytavat_vo = 0
        kaytavat_ya = 0

        koordinaatit_lista = self.muodosta_x_koordinaatti_lista()

        for each in koordinaatit_lista:
            a, b, c, d = new_visited[each]
            if a + b + c + d == 3:
                umpikujat += 1
            if a + b + c + d == 0:
                risteykset_4 += 1
            if a + b + c + d == 1:
                risteykset_3 += 1
            if a + b == 0 and c + d == 2:
                kaytavat_vo += 1
            if c + d == 0 and a + b == 2:
                kaytavat_ya += 1
            if a + b == 1 and c + d == 1:
                mutkat += 1
        if tulostus == "k":
            print("umpikujat:", umpikujat)
            print("risteykset, joissa ei yhtään seinää:", risteykset_4)
            print("risteykset, joissa yksi seinä:", risteykset_3)
            print("mutkia:", mutkat)
            print("vaakasuoria käytäväruutuja:", kaytavat_vo)
            print("pystysuoria käytäväruutuja:", kaytavat_ya)
            print("")
        return umpikujat

    # Labyrintin umpikujien mutkaisuuden ja pituuden seuraavaan risteykseen asti mittaava metodi
    def test_umpikujien_pituudet(self, visited, tulostus):
        new_visited = visited
        koordinaatit_lista = self.muodosta_x_koordinaatti_lista()
        umpikujat_lista = {}
        poistettavat_polut = []
        for each in koordinaatit_lista:
            a, b, c, d = new_visited[each]
            if a + b + c + d == 3:
                umpikujat_lista[each] = (a, b, c, d)
        umpikujat = {}
        mutkia, pituus = 0, 0
        for key, value in umpikujat_lista.items():
            a, b, c, d = value
            x, y = key
            mutkia = 0
            pituus = 1
            stack = [(x, y)]
            while stack:
                n = len(stack)-1
                x, y = stack[n]
                a, b, c, d = new_visited[(x, y)]

                if a == 0 and (x - self._w, y) not in stack and (x - self._w, y) in new_visited: # vasemmalle
                    x -= self._w
                    a, b, c, d = new_visited[(x, y)]
                    stack.append((x, y))
                    if a + b == 0 and c + d == 2:
                        pituus += 1
                    elif a == 1 and c + d == 1:
                        pituus += 1
                        mutkia += 1
                    else:
                        new_visited[(x, y)] = (a, 1, c, d)
                        #print("New wall:", x//self._w, y//self._w, a, b, c, d, visited[(x, y)])
                        if len(stack) > 1:
                            stack.pop()
                        #print("umpikuja", stack)
                        poistettavat_polut.append(stack)
                        stack = []
                elif b == 0 and (x + self._w, y) not in stack and (x + self._w, y) in new_visited: # oikealle
                    x += self._w
                    a, b, c, d = new_visited[(x, y)]
                    stack.append((x, y))
                    if a + b == 0 and c + d == 2:
                        pituus += 1
                    elif b == 1 and c + d == 1:
                        pituus += 1
                        mutkia += 1
                    else:
                        new_visited[(x, y)] = (1, b, c, d)
                        #print("New wall:", x//self._w, y//self._w, a, b, c, d, visited[(x, y)])
                        if len(stack) > 1:
                            stack.pop()
                        #print("umpikuja", stack)
                        poistettavat_polut.append(stack)
                        stack = []
                elif c == 0 and (x, y - self._w) not in stack and (x, y - self._w) in new_visited: # ylös
                    y -= self._w
                    a, b, c, d = new_visited[(x, y)]
                    stack.append((x, y))
                    if c + d == 0 and a + b == 2:
                        pituus += 1
                    elif c == 1 and a + b == 1:
                        pituus += 1
                        mutkia += 1
                    else:
                        new_visited[(x, y)] = (a, b, c, 1)
                        #print("New wall:", x//self._w, y//self._w, a, b, c, d, visited[(x, y)])
                        if len(stack) > 1:
                            stack.pop()
                        #print("umpikuja", stack)
                        poistettavat_polut.append(stack)
                        stack = []
                elif d == 0 and (x, y + self._w) not in stack and (x, y + self._w) in new_visited: # alas
                    y += self._w
                    a, b, c, d = new_visited[(x, y)]
                    stack.append((x, y))
                    if c + d == 0 and a + b == 2:
                        pituus += 1
                    elif d == 1 and a + b == 1:
                        pituus += 1
                        mutkia += 1
                    else:
                        new_visited[(x, y)] = (a, b, 1, d)
                        #print("New wall:", x//self._w, y//self._w, a, b, c, d, visited[(x, y)])
                        if len(stack) > 1:
                            stack.pop()
                        #print("umpikuja", stack)
                        poistettavat_polut.append(stack)
                        stack = []
            umpikujat[key] = (mutkia, pituus) # mutkia / umpikujan pituus
        if tulostus == "k":
            print("Labyrintin umpikujat; koordinaatit, mutkat ja pituus:")
            for key, value in umpikujat.items():
                i, j = value
                x, y = key
                print("(",x//self._w,",",y//self._w,") ", i, j)
            print("")
        return poistettavat_polut

    def etsi_reitti(self, visited):
        new_visited = visited
        umpikujien_lkm = self.test_lukumaarat(new_visited, ".")
        counter = umpikujien_lkm
        while counter > 0:
            poistettavat_polut = self.test_umpikujien_pituudet(new_visited, "k")
            for each in poistettavat_polut:
                for i in range(0, len(each)):
                    x, y = each[i]
                    if (x, y) in new_visited.keys():
                        del new_visited[(x, y)]
                counter -= 1
        return new_visited

    def piirra_reitti(self, visited):
        new_visited = visited
        reitti = []
        a, b, c, d = new_visited[(self._w, self._w)]
        new_visited[(self._w, self._w)] = (0, b, c, d)
        n = len(new_visited)
        x = (n // self._y_max) * self._w
        y = (n // self._y_max) * self._w
        a, b, c, d = new_visited[(x, y)]
        new_visited[(x, y)] = (a, 0, c, d)
        new_visited = self.etsi_reitti(new_visited)
        for each in new_visited:
            x, y = each
            reitti.append((x//self._w, y//self._w))
            self._maze.single_cell(x, y)
            time.sleep(Config.RATKAISU)
        print("labyrintin läpi ruudusta 1 , 1 ruutuun", self._x_max, ",", self._y_max,
        "kulkevan reitin pituus on", len(reitti), "ruutua:")
        print(reitti)
        print("")

    def mittaa_pituudet(self, visited):
        new_visited = visited
        mutkat = 0
        kaytavat = {}
        pituus, lkm = 1, 1
        for each in new_visited:
            key, value = each
            a, b, c, d = value
            if d == 0:
                pituus += 1
            else:
                if pituus in kaytavat:
                    lkm = kaytavat[pituus]
                    lkm += 1
                else:
                    lkm = 1
                if pituus > 1:
                    kaytavat[pituus] = lkm
                pituus = 1
                lkm = 1
        for key, value in kaytavat.items():
            mutkat += value
        return kaytavat, mutkat

    def test_kaytavien_pituudet(self, visited, tulostus):
        new_visited = visited
        mutkat = 0
        pystysuora = self.jarjesta_ruudut_pystysuora(new_visited)
        kaytavat, mutkat = self.mittaa_pituudet(pystysuora)
        print("pystysuorien käytävien lukumäärät:")
        sorted_kaytavat = sorted(kaytavat.items(), key = lambda item: item[0])
        for each in sorted_kaytavat:
            pituus, lkm = each
            print("pituus:", pituus, ":", lkm, "kpl")
        print("")
        vaakasuora = self.jarjesta_ruudut_vaakasuora(new_visited)
        a, b, c, d = vaakasuora[(self._x_max * self._w, self._y_max * self._w)]
        vaakasuora[(self._x_max * self._w, self._y_max * self._w)] = (a, 1, c, d)
        kaytavat = {}
        pituus, lkm = 1, 1
        for each in vaakasuora:
            x, y = each
            a, b, c, d = vaakasuora[(x, y)]
            if b == 0:
                pituus += 1
            else:
                if pituus in kaytavat:
                    lkm = kaytavat[pituus]
                    lkm += 1
                else:
                    lkm = 1
                if pituus > 1:
                    kaytavat[pituus] = lkm
                pituus = 1
                lkm = 1
        for key, value in kaytavat.items():
            mutkat += value
        mutkat -= 1
        print("vaakasuorien käytävien lukumäärät:")
        sorted_kaytavat = sorted(kaytavat.items(), key = lambda item: item[0])
        for each in sorted_kaytavat:
            pituus, lkm = each
            print("pituus:", pituus, ":", lkm, "kpl")
        if tulostus == "k":
            print("")
            print("mutkia on yhteensä", mutkat, "kpl")
        print("")

    def get_algoritmi(self):
        return self._algoritmi
