import time


"""
Labyrintin rakentamiseen käytettyjen algoritmien suorituskykyä ja labyrinttien rakenteita vertaileva luokka
"""
class Comparison():
    def __init__(self, algoritmi):
        self._algoritmi = algoritmi
        self._x_max = self._algoritmi._x_max
        self._y_max = self._algoritmi._y_max
        self._w = self._algoritmi._w

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
        jarjestetty = {}
        koordinaatit_lista = self.muodosta_y_koordinaatti_lista()
        for each in koordinaatit_lista:
            jarjestetty[each] = visited[each]
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

    def test_lukumaarat(self, visited):# alustava versio labyrintin rakenteita mittaavasta metodista
        umpikujat = 0
        risteykset_4 = 0
        risteykset_3 = 0
        mutkat = 0
        kaytavat_vo = 0
        kaytavat_ya = 0

        koordinaatit_lista = self.muodosta_x_koordinaatti_lista()

        for each in koordinaatit_lista:
            a, b, c, d = visited[each]
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
        print("umpikujat:")
        print(umpikujat)
        print("risteykset, joissa ei yhtään seinää:")
        print(risteykset_4)
        print("risteykset, joissa yksi seinä:")
        print(risteykset_3)
        print("mutkia:")
        print(mutkat)
        print("vaakasuoria käytäväruutuja:")
        print(kaytavat_vo)
        print("pystysuoria käytäväruutuja:")
        print(kaytavat_ya)
        #print("ruutuja yhteensä:")
        #koko = umpikujat + risteykset_4 + risteykset_3 + mutkat + kaytavat_vo + kaytavat_ya
        #print(koko)

    def test_umpikujien_pituudet(self):# alustava versio labyrintin rakenteita mittaavasta metodista
        pass

    def test_kaytavien_pituudet(self):# alustava versio rakenteita vertailevasta metodista
        pass

    def get_algoritmi(self):
        return self._algoritmi
