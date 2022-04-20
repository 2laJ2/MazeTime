import time
import random
from random import seed
from random import randint


"""
Growing Tree -algoritmilla labyrintin rakentava luokka
"""
class Mysteerimaze():
    def __init__(self, maze, x, y, w):
        self._maze = maze
        self._x_max = x
        self._y_max = y
        self._w = w
        self._grid = self._maze._grid
        self._solution = self._maze._solution
        self._visited = []

    # apumetodi, kun option = 1: valitsee viimeisimmän lisätyn ruudun ja poistaa sen pinosta,
    # jolloin algoritmi muuttuu recursive backtracking -algoritmiksi
    def gt_always_last(self, stack, x, y):
        x, y = stack.pop()
        self._maze.single_yellow_cell(x, y)
        time.sleep(.05)
        self._maze.backtracking_cell(x, y)
        return stack, x, y

    # apumetodi, kun option = 2: poistaa ruudun pinosta ja valitsee pinosta satunnaisen ruudun
    def gt_always_random(self, stack, x, y):
        if len(stack) > 0:
            stack.remove((x, y))
            if len(stack)>0:
                x, y = (random.choice(stack))
                self._maze.single_cell(x, y)
                time.sleep(.05)
                self._maze.backtracking_cell(x, y)
        return stack, x, y

    # apumetodi, kun option = 3: poistaa ruudun pinosta ja valitsee pinon ensimmäisen ruudun
    def gt_always_first(self, stack, x, y):
        if len(stack) > 0:
            stack.remove((x, y))
            if len(stack) > 0:
                x, y = stack[0]
                self._maze.single_cell(x, y)
                time.sleep(.05)
                self._maze.backtracking_cell(x, y)
        return stack, x, y

    # apumetodi, kun option = 4: poistaa ruudun pinosta ja valitsee yleensä viimeisimmän,
    # välillä satunnaisen ruudun pinosta
    def gt_usually_last_occasionally_random(self, stack, x, y):
        if len(stack) > 0:
            choice = (randint(1, 5))
            if choice == 1:
                stack.pop()
                x, y = (random.choice(stack))
            else:
                x, y = stack.pop()
                self._maze.single_cell(x, y)
                time.sleep(.05)
                self._maze.backtracking_cell(x, y)
        return stack, x, y

    # apumetodi, kun option = 5: poistaa ruudun pinosta, valitsee satunnaisen ruudun viimeisistä ruuduista
    def gt_random_among_last_ones(self, stack, x, y):
        if len(stack) > 0:
            stack.remove((x,y))
            length = len(stack)
            latest = len(stack)//4
            wilson_list = []
            for i in range(latest, length):
                wilson_list.append((stack[i]))
                if len(wilson_list) > 0:
                    x, y = (random.choice(wilson_list))
            self._maze.single_cell(x, y)
            time.sleep(.05)
            self._maze.backtracking_cell(x, y)
        return stack, x, y

    # metodi, joka luo parametrina annetuilla seed- ja option-arvoilla labyrintin
    def carve_mysteerimaze(self, seedling, option):
        seed(seedling)
        w = self._w
        x, y = w, w
        self._maze.single_cell(x, y)
        grid = self._grid
        solution = self._solution
        stack = []
        stack.append((x,y))
        self._visited = []
        self._visited.append((x,y))
        while len(stack) > 0:
            time.sleep(.001)
            cell_list = []
            if (x + w, y) not in self._visited and (x + w, y) in grid:
                cell_list.append("right")

            if (x - w, y) not in self._visited and (x - w, y) in grid:
                cell_list.append("left")

            if (x , y + w) not in self._visited and (x , y + w) in grid:
                cell_list.append("down")

            if (x, y - w) not in self._visited and (x , y - w) in grid:
                cell_list.append("up")

            if len(cell_list) > 0:
                cell_chosen = (random.choice(cell_list))

                if cell_chosen == "right":
                    self._maze.push_right(x, y)
                    solution[(x + w, y)] = x, y
                    x = x + w
                    self._visited.append((x, y))
                    stack.append((x, y))

                elif cell_chosen == "left":
                    self._maze.push_left(x, y)
                    solution[(x - w, y)] = x, y
                    x = x - w
                    self._visited.append((x, y))
                    stack.append((x, y))

                elif cell_chosen == "down":
                    self._maze.push_down(x, y)
                    solution[(x , y + w)] = x, y
                    y = y + w
                    self._visited.append((x, y))
                    stack.append((x, y))

                elif cell_chosen == "up":
                    self._maze.push_up(x, y)
                    solution[(x , y - w)] = x, y
                    y = y - w
                    self._visited.append((x, y))
                    stack.append((x, y))

            else:
                if option == '1':
                    stack, x, y = self.gt_always_last(stack, x, y)
                if option == '2':
                    stack, x, y = self.gt_always_random(stack, x, y)
                if option == '3':
                    stack, x, y = self.gt_always_first(stack, x, y)
                if option == '4':
                    stack, x, y = self.gt_usually_last_occasionally_random(stack, x, y)
                if option == '5':
                    stack, x, y = self.gt_random_among_last_ones(stack, x, y)

    # testauksessa käytetty metodi, joka palauttaa labyrintin
    def get_visited(self):
        return self._visited
    