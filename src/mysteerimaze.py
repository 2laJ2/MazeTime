import time
import random
from random import seed
from random import randint
from config import Config

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
        self._visited = {}

    # apumetodi, kun option = 1: valitsee viimeisimmän lisätyn ruudun ja poistaa sen pinosta,
    # jolloin algoritmi muuttuu recursive backtracking -algoritmiksi
    def gt_always_last(self, stack, x, y):
        stack_keys = stack.items()
        keys_iterator = iter(stack_keys)
        n = len(stack)
        for i in range (0, n):
            wanted_key = next(keys_iterator)
        key, value = wanted_key
        x, y = key
        del stack[(key)]
        #x, y = stack.pop()
        self._maze.single_yellow_cell(x, y)
        time.sleep(Config.WILSON_MYSTEERI)
        self._maze.backtracking_cell(x, y)
        return stack, x, y

    # apumetodi, kun option = 2: poistaa ruudun pinosta ja valitsee pinosta satunnaisen ruudun
    def gt_always_random(self, stack, x, y):
        if (x, y) in stack:
            wanted_key = (x, y), stack[(x, y)]
            del stack[(x, y)]
            #stack.remove((x, y))
        if len(stack) > 0:
            n = randint(0, len(stack))
            stack_keys = stack.items()
            keys_iterator = iter(stack_keys)
            for i in range (0, n):
                wanted_key = next(keys_iterator)
            key, value = wanted_key
            x, y = key
            #x, y = (random.choice(stack))
            self._maze.single_cell(x, y)
            time.sleep(Config.WILSON_MYSTEERI)
            self._maze.backtracking_cell(x, y)
        return stack, x, y

    # apumetodi, kun option = 3: poistaa ruudun pinosta ja valitsee pinon ensimmäisen ruudun
    def gt_always_first(self, stack, x, y):
        if (x, y) in stack:
            wanted_key = (x, y), stack[(x, y)]
            del stack[(x, y)]
            #stack.remove((x, y))
            if len(stack) > 0:
                stack_keys = stack.items()
                keys_iterator = iter(stack_keys)
                wanted_key = next(keys_iterator)
                key, value = wanted_key
                x, y = key
            #x, y = stack[0]
            self._maze.single_cell(x, y)
            time.sleep(Config.WILSON_MYSTEERI)
            self._maze.backtracking_cell(x, y)
        return stack, x, y

    # apumetodi, kun option = 4: poistaa ruudun pinosta ja valitsee yleensä viimeisimmän,
    # välillä satunnaisen ruudun pinosta
    def gt_usually_last_occasionally_random(self, stack, x, y):
        if (x, y) in stack:
            wanted_key = (x, y), stack[(x, y)]
            del stack[(x, y)]
        if len(stack) > 0:
            choice = (randint(1, 5))
            if choice == 1:
                n = randint(0, len(stack))
                stack_keys = stack.items()
                keys_iterator = iter(stack_keys)
                for i in range (0, n):
                    wanted_key = next(keys_iterator)
                    key, value = wanted_key
                    x, y = key
            #stack.pop()
            #x, y = (random.choice(stack))
            else:
                stack_keys = stack.items()
                keys_iterator = iter(stack_keys)
                n = len(stack)
                for i in range (0, n):
                    wanted_key = next(keys_iterator)
                key, value = wanted_key
                x, y = key
                del stack[(key)]
                #x, y = stack.pop()
                self._maze.single_cell(x, y)
                time.sleep(Config.WILSON_MYSTEERI)
                self._maze.backtracking_cell(x, y)
        return stack, x, y

    # apumetodi, kun option = 5: poistaa ruudun pinosta, valitsee satunnaisen ruudun viimeisistä ruuduista
    def gt_random_among_last_ones(self, stack, x, y):
        if (x, y) in stack:
            wanted_key = (x, y), stack[(x, y)]
        if len(stack) > 0:
            del stack[(x, y)]
            #stack.remove((x,y))
        if len(stack) > 0:
            length = len(stack)
            latest = len(stack)//4
            mysteeri_list = {}
            stack_keys = stack.items()
            keys_iterator = iter(stack_keys)
            for i in range(latest, length):
                wanted_key = next(keys_iterator)
            key, value = wanted_key
            x, y = key
            mysteeri_list[(key)] = stack[(key)]
            #mysteeri_list.append((stack[i]))
            if len(mysteeri_list) > 0:
                n = randint(0, len(mysteeri_list))
                mysteeri_keys = mysteeri_list.items()
                keys_iterator = iter(mysteeri_keys)
                for i in range (0, n):
                    wanted_key = next(keys_iterator)
                key, value = wanted_key
                x, y = key
                #x, y = (random.choice(mysteeri_list))
            self._maze.single_cell(x, y)
            time.sleep(Config.WILSON_MYSTEERI)
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
        stack = {}
        stack[(x, y)] = (1, 1, 1, 1)
        self._visited = {}
        self._visited[(x,y)] = (1, 1, 1, 1)
        while len(stack) > 0:
            time.sleep(Config.WILSON_MYSTEERI)
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

                    if (x, y) in self._visited:
                        e, f, g, h = self._visited[(x, y)]
                    else:
                        e, f, g, h = 1, 1, 1, 1
                    self._visited[(x, y)] = (e, 0, g, h)
                    solution[(x, y)] = self._visited[(x, y)]#?
                    stack[(x, y)] = self._visited[(x, y)]#?
                    x += w
                    if (x, y) in self._visited:
                        e, f, g, h = self._visited[(x, y)]
                    else:
                        e, f, g, h = 1, 1, 1, 1
                    self._visited[(x, y)] = (0, f, g, h)
                    solution[(x, y)] = self._visited[(x, y)]#?
                    stack[(x, y)] = self._visited[(x, y)]#?
                    #solution[(x + w, y)] = x, y
                    #x = x + w
                    #self._visited.append((x, y))
                    #stack.append((x, y))

                elif cell_chosen == "left":
                    self._maze.push_left(x, y)

                    if (x, y) in self._visited:
                        e, f, g, h = self._visited[(x, y)]
                    else:
                        e, f, g, h = 1, 1, 1, 1
                    self._visited[(x, y)] = (0, f, g, h)
                    solution[(x, y)] = self._visited[(x, y)]#?
                    stack[(x, y)] = self._visited[(x, y)]#?
                    x -= w
                    if (x, y) in self._visited:
                        e, f, g, h = self._visited[(x, y)]
                    else:
                        e, f, g, h = 1, 1, 1, 1
                    self._visited[(x, y)] = (e, 0, g, h)
                    solution[(x, y)] = self._visited[(x, y)]#?
                    stack[(x, y)] = self._visited[(x, y)]#?

                    #solution[(x - w, y)] = x, y
                    #x = x - w
                    #self._visited.append((x, y))
                    #stack.append((x, y))

                elif cell_chosen == "down":
                    self._maze.push_down(x, y)

                    if (x, y) in self._visited:
                        e, f, g, h = self._visited[(x, y)]
                    else:
                        e, f, g, h = 1, 1, 1, 1
                    self._visited[(x, y)] = (e, f, g, 0)
                    solution[(x, y)] = self._visited[(x, y)]#?
                    stack[(x, y)] = self._visited[(x, y)]#?
                    y += w
                    if (x, y) in self._visited:
                        e, f, g, h = self._visited[(x, y)]
                    else:
                        e, f, g, h = 1, 1, 1, 1
                    self._visited[(x, y)] = (e, f, 0, h)
                    solution[(x, y)] = self._visited[(x, y)]#?
                    stack[(x, y)] = self._visited[(x, y)]#?

                    #solution[(x , y + w)] = x, y
                    #y = y + w
                    #self._visited.append((x, y))
                    #stack.append((x, y))

                elif cell_chosen == "up":
                    self._maze.push_up(x, y)

                    if (x, y) in self._visited:
                        e, f, g, h = self._visited[(x, y)]
                    else:
                        e, f, g, h = 1, 1, 1, 1
                    self._visited[(x, y)] = (e, f, 0, h)
                    solution[(x, y)] = self._visited[(x, y)]#?
                    stack[(x, y)] = self._visited[(x, y)]#?
                    y -= w
                    if (x, y) in self._visited:
                        e, f, g, h = self._visited[(x, y)]
                    else:
                        e, f, g, h = 1, 1, 1, 1
                    self._visited[(x, y)] = (e, f, g, 0)
                    solution[(x, y)] = self._visited[(x, y)]#?
                    stack[(x, y)] = self._visited[(x, y)]#?

                    #solution[(x , y - w)] = x, y
                    #y = y - w
                    #self._visited.append((x, y))
                    #stack.append((x, y))

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
    