import time
import random
from random import seed
from random import randint
from itertools import islice
from config import Config

"""
Wilsonin algoritmilla labyrintin rakentava luokka
"""
class Wilson():
    def __init__(self, maze, x, y, w):
        self._maze = maze
        self._x_max = x
        self._y_max = y
        self._w = w
        self._grid = self._maze._grid
        self._not_visited = {}
        self._visited = {}

    def reverse_stack_builder(self, x_max, y_max):

        """ Apumetodi, jolla luodaan lista ruuduista, joissa ei ole käyty.

        Args:
            x_max: haluttu labyrintin leveys annetaan x-koordinaattien lukumääränä.
            y_max: haluttu labyrintin korkeus annetaan y-koordinaattien lukumääränä.
        Returns:
            sanakirjamuodossa oleva lista ruuduista, joissa ei ole käyty. Kaikilla
            koordinaatistossa olevilla ruuduilla on neljä seinää.
        """

        w = self._w
        stack = {}
        for i in range(1, x_max+1):
            x = i * w
            for j in range(1, y_max+1):
                y = j * w
                stack[(x, y)] = (1, 1, 1, 1)
        return stack

    def wilson_path(self, solution, a, b):

        """ Apumetodi, jolla liitetään viimeksi kuljettu polku labyrinttiin ja tyhjennetään polku.
            Käy kuljetun reitin uudelleen läpi ruutu kerrallaan, piirtää Pygame-ikkunan ruudukkoon
            kulkureitin poistamalla reitillä olevien ruutujen ruutujen väliset seinät ja liittää
            reitin valmiiseen labyrinttiin sanakirjamuodossa.

        Args:
            solution: lista stringinä tallennetuista kulkusuunnista,
            a: polun ensimmäisen ruudun x-koordinaatti,
            b: polun ensimmäisen ruudun y-koordinaatti.
        Returns:
            tyhjän polun.
        """

        self._visited[(a, b)] = (1, 1, 1, 1)
        w = self._w
        self._maze.single_purple_cell(a, b)
        for cell in solution:
            if  cell == "right":
                self._maze.push_right(a, b)
                if (a, b) in self._visited:
                    e, f, g, h = self._visited[(a, b)]
                else:
                    e, f, g, h = 1, 1, 1, 1
                self._visited[(a, b)] = (e, 0, g, h)
                a += w
                if (a, b) in self._visited:
                    e, f, g, h = self._visited[(a, b)]
                else:
                    e, f, g, h = 1, 1, 1, 1
                self._visited[(a, b)] = (0, f, g, h)
            if cell == "left":
                self._maze.push_left(a, b)
                if (a, b) in self._visited:
                    e, f, g, h = self._visited[(a, b)]
                else:
                    e, f, g, h = 1, 1, 1, 1
                self._visited[(a, b)] = (0, f, g, h)
                a -= w
                if (a, b) in self._visited:
                    e, f, g, h = self._visited[(a, b)]
                else:
                    e, f, g, h = 1, 1, 1, 1
                self._visited[(a, b)] = (e, 0, g, h)
            if cell == "down":
                self._maze.push_down(a, b)
                if (a, b) in self._visited:
                    e, f, g, h = self._visited[(a, b)]
                else:
                    e, f, g, h = 1, 1, 1, 1
                self._visited[(a, b)] = (e, f, g, 0)
                b += w
                if (a, b) in self._visited:
                    e, f, g, h = self._visited[(a, b)]
                else:
                    e, f, g, h = 1, 1, 1, 1
                self._visited[(a, b)] = (e, f, 0, h)
            if cell == "up":
                self._maze.push_up(a, b)
                if (a, b) in self._visited:
                    e, f, g, h = self._visited[(a, b)]
                else:
                    e, f, g, h = 1, 1, 1, 1
                self._visited[(a, b)] = (e, f, 0, h)
                b -= w
                if (a, b) in self._visited:
                    e, f, g, h = self._visited[(a, b)]
                else:
                    e, f, g, h = 1, 1, 1, 1
                self._visited[(a, b)] = (e, f, g, 0)

        return []

    def carve_Wilson_maze(self, seedling):

        """ Metodi, joka luo ja piirtää labyrintin Pygame-ikkunan ruudukkoon Wilsonin algoritmilla.
            Labyrintti tallennetaan muodossa (x, y) = (a, b, c, d), missä (x, y) on ruudun koordinaatti
            tuplé-muodossa ja arvot a, b, c ja d vastaavat kyseisen ruudun seiniä järjestyksessä vasen,
            oikea, ylös ja alas. Seinää vastaa arvo 1, avointa kulkua arvo 0.

        Args:
            seedling:   Seed-arvo, joka on määritelty config.py-tiedostossa. Käyttäjä voi halutessaan vaihtaa
                        algoritmin käyttämää seed-arvoa konfiguraatiotiedostossa.
        """

        seed(seedling)
        w = self._w
        grid = self._grid
        solution = []
        stack = {}
        x1 = self._x_max//2*w
        y1 = self._y_max//2*w
        x = (randint(0, self._x_max-1))*w
        y = (randint(0, self._y_max-1))*w
        a = x
        b = y
        self._not_visited = self.reverse_stack_builder(self._x_max, self._y_max)
        e, f, g, h = self._not_visited[(x1, y1)]
        self._visited[(x1, y1)] = (e, f, g, h)
        self._maze.single_purple_cell(x1, y1)
        del self._not_visited[(x1, y1)]
        while len(self._not_visited) > 0:
            if (x, y) in self._not_visited:
                stack[(x, y)] = self._not_visited[(x, y)]
                del self._not_visited[(x, y)]
            self._maze.single_yellow_cell(x, y)
            time.sleep(Config.WILSON_MYSTEERI)
            cell_list = []

            if (x + w, y) not in stack and (x + w, y) in grid:# ei nykyisessä polussa eli ei mennä taaksepäin
                cell_list.append("right")

            if (x - w, y) not in stack and (x - w, y) in grid:
                cell_list.append("left")

            if (x, y + w) not in stack and (x, y + w) in grid:
                cell_list.append("down")

            if (x, y - w) not in stack and (x, y - w) in grid:
                cell_list.append("up")

            if len(cell_list) > 0:
                cell_chosen = (random.choice(cell_list))

                if  cell_chosen == "right":
                    if (x + w, y) not in self._not_visited:# on käyty aiemmin
                        solution.append(cell_chosen)#
                        stack_keys = stack.items()
                        keys_iterator = iter(stack_keys)
                        first_key = next(keys_iterator)
                        key, value = first_key
                        a, b = key
                        solution = self.wilson_path(solution, a, b)
                        stack = {}
                        if len(self._not_visited) != 0:
                            n = randint(0, len(self._not_visited)-1)
                            stack_keys = self._not_visited.items()
                            keys_iterator = iter(stack_keys)
                            next(islice(keys_iterator, n, n), None)
                            wanted_key = next(keys_iterator)
                            key, value = wanted_key
                            x, y = key
                        a, b = x, y
                    elif (x + w, y) in self._not_visited:# ei ole käyty aiemmin
                        x += w
                        del self._not_visited[(x, y)]
                        stack[(x, y)] = (0, 1, 1, 1)
                        solution.append(cell_chosen)# lisätään ruutu reittiin

                elif cell_chosen == "left":
                    if (x - w, y) not in self._not_visited:
                        solution.append(cell_chosen)
                        stack_keys = stack.items()
                        keys_iterator = iter(stack_keys)
                        first_key = next(keys_iterator)
                        key, value = first_key
                        a, b = key
                        solution = self.wilson_path(solution, a, b)
                        stack = {}
                        if len(self._not_visited) != 0:
                            n = randint(0, len(self._not_visited)-1)
                            stack_keys = self._not_visited.items()
                            keys_iterator = iter(stack_keys)
                            next(islice(keys_iterator, n, n), None)
                            wanted_key = next(keys_iterator)
                            key, value = wanted_key
                            x, y = key
                        a, b = x, y
                    elif (x - w, y) in self._not_visited:
                        x -= w
                        del self._not_visited[(x, y)]
                        stack[(x, y)] = (1, 0, 1, 1)
                        solution.append(cell_chosen)

                elif cell_chosen == "down":
                    if (x, y + w) not in self._not_visited:
                        solution.append(cell_chosen)
                        stack_keys = stack.items()
                        keys_iterator = iter(stack_keys)
                        first_key = next(keys_iterator)
                        key, value = first_key
                        a, b = key
                        solution = self.wilson_path(solution, a, b)
                        stack = {} #[]
                        if len(self._not_visited) != 0:
                            n = randint(0, len(self._not_visited)-1)
                            stack_keys = self._not_visited.items()
                            keys_iterator = iter(stack_keys)
                            next(islice(keys_iterator, n, n), None)
                            wanted_key = next(keys_iterator)
                            key, value = wanted_key
                            x, y = key
                        a, b = x, y
                    elif (x, y + w) in self._not_visited:
                        y += w
                        del self._not_visited[(x, y)]
                        stack[(x, y)] = (1, 0, 1, 1)
                        solution.append(cell_chosen)

                elif cell_chosen == "up":
                    if (x, y - w) not in self._not_visited:
                        solution.append(cell_chosen)
                        stack_keys = stack.items()
                        keys_iterator = iter(stack_keys)
                        first_key = next(keys_iterator)
                        key, value = first_key
                        a, b = key
                        solution = self.wilson_path(solution, a, b)
                        stack = {}
                        if len(self._not_visited) != 0:
                            n = randint(0, len(self._not_visited)-1)
                            stack_keys = self._not_visited.items()
                            keys_iterator = iter(stack_keys)
                            next(islice(keys_iterator, n, n), None)
                            wanted_key = next(keys_iterator)
                            key, value = wanted_key
                            x, y = key
                        a, b = x, y
                    elif (x, y - w) in self._not_visited:
                        y -= w
                        del self._not_visited[(x, y)]
                        stack[(x, y)] = (1, 0, 1, 1)
                        solution.append(cell_chosen)

            elif len(cell_list) == 0:# jos tullaan nykyisen polun muodostamaan umpikujaan

                n = randint(0, len(self._not_visited)-1)
                stack_keys = self._not_visited.items()
                keys_iterator = iter(stack_keys)
                next(islice(keys_iterator, n, n), None)
                wanted_key = next(keys_iterator)
                key, value = wanted_key
                x, y = key
                for cell_list in stack:
                    self._not_visited[(cell_list)] = (1, 1, 1, 1)
                stack = {}
                solution = []

    def get_visited(self):

        """ Testauksessa käytetty metodi, joka palauttaa labyrintin.

        Returns:
            algoritmin luoman ja tallentaman valmiin labyrintin sanakirjamuodossa.
        """

        return self._visited
