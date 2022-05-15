import time
import random
from random import seed
from random import randint
from config import Config


"""
Aldous-Broderin algoritmilla labyrintin rakentava luokka
"""
class Abmaze():
    def __init__(self, maze, x, y, w):
        self._maze = maze
        self._x_max = x
        self._y_max = y
        self._w = w
        self._grid = self._maze._grid
        self._visited = {}

    def carve_AB_maze(self, seedling):

        """ Metodi, joka luo ja piirtää labyrintin Pygame-ikkunan ruudukkoon Aldous-Broderin algoritmilla.
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
        x = (randint(0, self._x_max-1))*w
        y = (randint(0, self._y_max-1))*w
        visits = 0
        self._visited = {}
        while len(self._visited) < (self._x_max*self._y_max):
            if (x, y) not in self._visited:
                self._visited[(x, y)] = (1, 1, 1, 1)
            self._maze.single_purple_cell(x, y)
            time.sleep(Config.ABMAZE)
            cell_list = []
            if (x + w, y) in grid:
                cell_list.append("right")

            if (x - w, y) in grid:
                cell_list.append("left")

            if (x, y + w) in grid:
                cell_list.append("down")

            if (x, y - w) in grid:
                cell_list.append("up")

            cell_chosen = (random.choice(cell_list))

            if  cell_chosen == "right":
                if (x + w, y) not in self._visited:
                    self._maze.push_right(x, y)
                    a, b, c, d = self._visited[x, y]
                    self._visited[x, y] = (a, 0, c, d)
                    self._visited[x + w, y] = (0, 1, 1, 1)
                    visits += 1
                x = x + w

            elif cell_chosen == "left":
                if (x - w, y) not in self._visited:
                    self._maze.push_left(x, y)
                    a, b, c, d = self._visited[x, y]
                    self._visited[x, y] = (0, b, c, d)
                    self._visited[x - w, y] = (1, 0, 1, 1)
                    visits += 1
                x = x - w

            elif cell_chosen == "down":
                if (x, y + w) not in self._visited:
                    self._maze.push_down(x, y)
                    a, b, c, d = self._visited[x, y]
                    self._visited[x, y] = (a, b, c, 0)
                    self._visited[x, y + w] = (1, 1, 0, 1)
                    visits += 1
                y = y + w

            elif cell_chosen == "up":
                if (x, y - w) not in self._visited:
                    self._maze.push_up(x, y)
                    a, b, c, d = self._visited[x, y]
                    self._visited[x, y] = (a, b, 0, d)
                    self._visited[x, y - w] = (1, 1, 1, 0)
                    visits += 1
                y = y - w

    def get_visited(self):

        """ Testauksessa käytetty metodi, joka palauttaa labyrintin.

        Returns:
            algoritmin luoman ja tallentaman valmiin labyrintin sanakirjamuodossa.
        """

        return self._visited
