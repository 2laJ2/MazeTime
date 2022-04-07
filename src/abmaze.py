import time
import random
from random import seed
from random import randint

class Abmaze():
    def __init__(self, maze, w):
        self._maze = maze
        self._w = w
        self._grid = self._maze._grid

    # Aldous-Broder algorithm
    def carve_AB_maze(self, seedling): # luo seed-arvolla 0 labyrintin
        seed(seedling)
        w = self._w
        grid = self._grid
        x = (randint(0, w-1))*20
        y = (randint(0, w-1))*20
        visits = 0
        visited = []
        while len(visited) < 400: # labyrintin ruutujen lukumäärä
            if (x, y) not in visited: visited.append((x,y))
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
                if (x + w, y) not in visited:
                    self._maze.push_right(x, y)
                    visited.append((x + w, y))
                    visits += 1
                x = x + w

            elif cell_chosen == "left":
                if (x - w, y) not in visited:
                    self._maze.push_left(x, y)
                    visited.append((x - w, y))
                    visits += 1
                x = x - w

            elif cell_chosen == "down":
                if (x, y + w) not in visited:
                    self._maze.push_down(x, y)
                    visited.append((x, y + w))
                    visits += 1
                y = y + w

            elif cell_chosen == "up":
                if (x, y - w) not in visited:
                    self._maze.push_up(x, y)
                    visited.append((x, y - w))
                    visits += 1
                y = y - w