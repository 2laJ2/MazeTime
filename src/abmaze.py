import time
import random
from random import seed
from random import randint


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
        self._visited = []

    # metodi, joka luo parametrina annetulla seed-arvolla labyrintin
    def carve_AB_maze(self, seedling):
        seed(seedling)
        w = self._w
        grid = self._grid
        x = (randint(0, w-1))*20
        y = (randint(0, w-1))*20
        visits = 0
        self._visited = []
        while len(self._visited) < (self._x_max*self._y_max): # labyrintin ruutujen lukumäärä
            if (x, y) not in self._visited:
                self._visited.append((x,y))
            self._maze.single_purple_cell(x, y)
            time.sleep(.0001)
            cell_list = []
            if (x + w, y) in grid:
                cell_list.append("right")

            if (x - w, y) in grid:
                cell_list.append("left")

            if (x , y + w) in grid:
                cell_list.append("down")

            if (x , y - w) in grid:
                cell_list.append("up")

            cell_chosen = (random.choice(cell_list))

            if  cell_chosen == "right":
                if (x + w, y) not in self._visited:
                    self._maze.push_right(x, y)
                    self._visited.append((x + w, y))
                    visits += 1
                x = x + w

            elif cell_chosen == "left":
                if (x - w, y) not in self._visited:
                    self._maze.push_left(x, y)
                    self._visited.append((x - w, y))
                    visits += 1
                x = x - w

            elif cell_chosen == "down":
                if (x, y + w) not in self._visited:
                    self._maze.push_down(x, y)
                    self._visited.append((x, y + w))
                    visits += 1
                y = y + w

            elif cell_chosen == "up":
                if (x, y - w) not in self._visited:
                    self._maze.push_up(x, y)
                    self._visited.append((x, y - w))
                    visits += 1
                y = y - w
       