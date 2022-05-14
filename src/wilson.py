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

    # apumetodi, jolla luodaan lista ruuduista, joissa ei ole käyty
    def reverse_stack_builder(self, x_max, y_max):
        w = self._w
        stack = {}
        for i in range(1, x_max+1):
            x = i*w
            for j in range(1, y_max+1):
                y = j*w
                stack[(x,y)] = (1,1,1,1)
        return stack

    # apumetodi, jolla liitetään viimeksi kuljettu polku labyrinttiin ja tyhjennetään polku
    def wilson_path(self, solution, a, b):
        self._visited[(a, b)] = (1, 1, 1, 1)
        w = self._w
        self._maze.single_purple_cell(a, b)
        for cell in solution:# käydään uudelleen reitti läpi ja liitetään se valmiiseen labyrinttiin
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

    # metodi, joka luo parametrina annetulla seed-arvolla labyrintin
    def carve_Wilson_maze(self, seedling):
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
        self._not_visited = self.reverse_stack_builder(self._x_max, self._y_max)# labyrintin koko x, y
        e, f, g, h = self._not_visited[(x1, y1)]
        self._visited[(x1, y1)] = (e, f, g, h)
        self._maze.single_purple_cell(x1, y1)
        del self._not_visited[(x1, y1)]
        while len(self._not_visited) > 0:# len(self._not_visited) alussa = ruutujen lukumäärä alussa
            #len(self._visited) <= self._x_max*self._y_max:
            if (x, y) in self._not_visited:# jos ruutu on vapaa
                stack[(x, y)] = self._not_visited[(x, y)]
                del self._not_visited[(x, y)]# poista vapaiden ruutujen luettelosta
            self._maze.single_yellow_cell(x, y)
            time.sleep(Config.WILSON_MYSTEERI)
            cell_list = []

            if (x + w, y) not in stack and (x + w, y) in grid:# ei nykyisessä polussa eli ei mennä taaksepäin
                cell_list.append("right")

            if (x - w, y) not in stack and (x - w, y) in grid:
                cell_list.append("left")

            if (x , y + w) not in stack and (x , y + w) in grid:
                cell_list.append("down")

            if (x , y - w) not in stack and (x , y - w) in grid:
                cell_list.append("up")

            if len(cell_list)>0:
                cell_chosen = (random.choice(cell_list))

                if  cell_chosen == "right":
                    if (x + w, y) not in self._not_visited:# on käyty aiemmin
                        solution.append(cell_chosen)#
                        stack_keys = stack.items()
                        keys_iterator = iter(stack_keys)
                        first_key = next(keys_iterator)
                        key, value = first_key
                        a, b = key
                        solution = self.wilson_path(solution, a, b)# liittää polun labyrinttiin, tyhjentää sen
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

            elif len(cell_list)==0:# jos tullaan nykyisen polun muodostamaan umpikujaan

                n = randint(0, len(self._not_visited)-1)
                stack_keys = self._not_visited.items()
                keys_iterator = iter(stack_keys)
                next(islice(keys_iterator, n, n), None)
                wanted_key = next(keys_iterator)
                key, value = wanted_key
                x, y = key
                for cell_list in stack:# merkitään kuljetun polun ruudut takaisin ei käydyiksi
                    self._not_visited[(cell_list)] = (1, 1, 1, 1)
                stack = {}#[]# tyhjennetään polku
                solution = []# tyhjennetään piirrettävä reitti

    # testauksessa käytetty metodi, joka palauttaa labyrintin
    def get_visited(self):
        return self._visited
