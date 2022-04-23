import time
import random
from abmaze import Abmaze
from mysteerimaze import Mysteerimaze
from wilson import Wilson


"""
Labyrintin rakentamiseen käytettyjen algoritmien suorituskykyä ja labyrinttien rakenteita vertaileva luokka
"""
class Comparison():
    def __init__(self, algoritmi):
        self._algoritmi = algoritmi

    def test_time_complexity(self):# alustava versio algoritmin kestoa mittaavasta metodista
        statistics = []
        result = 0
        for i in range (1, 10):
            start = time.time()
            self._algoritmi.carve_AB_maze(0)
            end = time.time()
            statistics.append(end - start)
        for i in statistics:
            result += i
        result /= len(statistics)
        return result

    def test_umpikujien_lukumaarat(self):# alustava versio labyrintin rakenteita mittaavasta metodista
        pass

    def test_risteysten_lukumaarat(self):# alustava versio labyrintin rakenteita mittaavasta metodista
        pass

    def test_kaytavien_keskimaarainen_pituus(self):# alustava versio labyrintin rakenteita mittaavasta metodista
        pass

    def test_rakenneominaisuus_x(self):# alustava versio labyrintin rakenteita mittaavasta metodista
        pass

    def get_algoritmi(self):
        return self._algoritmi