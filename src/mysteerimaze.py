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

    def gt_always_last(self, stack, x, y):

        """ Apumetodi, kun option = 1: valitsee viimeisimmän lisätyn ruudun ja poistaa sen pinosta,
            jolloin algoritmi muuttuu recursive backtracking -algoritmiksi.

        Args:
            stack: sanakirja, johon on tallennettu kuljetun polun ruudut muodossa (x, y) = (a, b, c, d).
            x: nykyisen ruudun x-koordinaatti
            y: nykyisen ruudun y-koordinaatti
        Returns:
            stack: sanakirjamuodossa oleva polku, josta on poistettu viimeinen ruutu.
            x: edellisen ruudun x-koordinaatti
            y: edellisen ruudun y-koordinaatti
        """

        stack_keys = stack.items()
        keys_iterator = iter(stack_keys)
        n = len(stack)
        for i in range(0, n):
            wanted_key = next(keys_iterator)
        key, value = wanted_key
        x, y = key
        del stack[(key)]
        self._maze.single_yellow_cell(x, y)
        time.sleep(Config.WILSON_MYSTEERI)
        self._maze.backtracking_cell(x, y)
        return stack, x, y

    def gt_always_random(self, stack, x, y):

        """ Apumetodi, kun option = 2: poistaa ruudun polusta ja valitsee polusta satunnaisen ruudun.

        Args:
            stack: sanakirja, johon on tallennettu kuljetun polun ruudut muodossa (x, y) = (a, b, c, d).
            x: nykyisen ruudun x-koordinaatti
            y: nykyisen ruudun y-koordinaatti
        Returns:
            stack: sanakirjamuodossa oleva polku, josta on poistettu viimeinen ruutu.
            x: satunnaisen, polussa olevan ruudun x-koordinaatti
            y: satunnaisen, polussa olevan ruudun y-koordinaatti
        """

        if (x, y) in stack:
            wanted_key = (x, y), stack[(x, y)]
            del stack[(x, y)]
        if len(stack) > 0:
            n = randint(0, len(stack))
            stack_keys = stack.items()
            keys_iterator = iter(stack_keys)
            for i in range(0, n):
                wanted_key = next(keys_iterator)
                key, value = wanted_key
                x, y = key
            self._maze.single_cell(x, y)
            time.sleep(Config.WILSON_MYSTEERI)
            self._maze.backtracking_cell(x, y)
        return stack, x, y

    def gt_always_first(self, stack, x, y):

        """ Apumetodi, kun option = 3: poistaa ruudun polusta ja valitsee polun ensimmäisen ruudun.

        Args:
            stack: sanakirja, johon on tallennettu kuljetun polun ruudut muodossa (x, y) = (a, b, c, d).
            x: nykyisen ruudun x-koordinaatti
            y: nykyisen ruudun y-koordinaatti
        Returns:
            stack: sanakirjamuodossa oleva polku, josta on poistettu viimeinen ruutu.
            x: polun ensimmäisen ruudun x-koordinaatti
            y: polun ensimmäisen ruudun y-koordinaatti
        """

        if (x, y) in stack:
            wanted_key = (x, y), stack[(x, y)]
            del stack[(x, y)]
            if len(stack) > 0:
                stack_keys = stack.items()
                keys_iterator = iter(stack_keys)
                wanted_key = next(keys_iterator)
                key, value = wanted_key
                x, y = key
            self._maze.single_cell(x, y)
            time.sleep(Config.WILSON_MYSTEERI)
            self._maze.backtracking_cell(x, y)
        return stack, x, y

    def gt_usually_last_occasionally_random(self, stack, x, y):

        """ Apumetodi, kun option = 4: poistaa ruudun polusta ja valitsee yleensä viimeisimmän,
            välillä satunnaisen ruudun polusta.

        Args:
            stack: sanakirja, johon on tallennettu kuljetun polun ruudut muodossa (x, y) = (a, b, c, d).
            x: nykyisen ruudun x-koordinaatti
            y: nykyisen ruudun y-koordinaatti
        Returns:
            stack: sanakirjamuodossa oleva polku, josta on poistettu viimeinen ruutu.
            x ja y: yleensä polun viimeisimmän, välillä satunnaisen ruudun x- ja y-koordinaatit
        """

        if (x, y) in stack:
            wanted_key = (x, y), stack[(x, y)]
            del stack[(x, y)]
        if len(stack) > 0:
            choice = (randint(1, 5))
            if choice == 1:
                n = randint(0, len(stack))
                stack_keys = stack.items()
                keys_iterator = iter(stack_keys)
                for i in range(0, n):
                    wanted_key = next(keys_iterator)
                    key, value = wanted_key
                    x, y = key
            else:
                stack_keys = stack.items()
                keys_iterator = iter(stack_keys)
                n = len(stack)
                for i in range(0, n):
                    wanted_key = next(keys_iterator)
                key, value = wanted_key
                x, y = key
                del stack[(key)]
                self._maze.single_cell(x, y)
                time.sleep(Config.WILSON_MYSTEERI)
                self._maze.backtracking_cell(x, y)
        return stack, x, y

    def gt_random_among_last_ones(self, stack, x, y):

        """ Apumetodi, kun option = 5: poistaa ruudun polusta ja valitsee satunnaisen ruudun polun
            viimeisistä ruuduista.

        Args:
            stack: sanakirja, johon on tallennettu kuljetun polun ruudut muodossa (x, y) = (a, b, c, d).
            x: nykyisen ruudun x-koordinaatti
            y: nykyisen ruudun y-koordinaatti
        Returns:
            stack: sanakirjamuodossa oleva polku, josta on poistettu viimeinen ruutu.
            x: satunnaisen ruudun polun viimeisistä ruuduista x-koordinaatti
            y: satunnaisen ruudun polun viimeisistä ruuduista y-koordinaatti
        """

        if (x, y) in stack:
            wanted_key = (x, y), stack[(x, y)]
        if len(stack) > 0:
            del stack[(x, y)]
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
            if len(mysteeri_list) > 0:
                n = randint(0, len(mysteeri_list))
                mysteeri_keys = mysteeri_list.items()
                keys_iterator = iter(mysteeri_keys)
                for i in range(0, n):
                    wanted_key = next(keys_iterator)
                key, value = wanted_key
                x, y = key
            self._maze.single_cell(x, y)
            time.sleep(Config.WILSON_MYSTEERI)
            self._maze.backtracking_cell(x, y)
        return stack, x, y

    def carve_mysteerimaze(self, seedling, option):

        """ Metodi, joka luo ja piirtää labyrintin Pygame-ikkunan ruudukkoon Growing Tree -algoritmilla.
            Labyrintti tallennetaan muodossa (x, y) = (a, b, c, d), missä (x, y) on ruudun koordinaatti
            tuplé-muodossa ja arvot a, b, c ja d vastaavat kyseisen ruudun seiniä järjestyksessä vasen,
            oikea, ylös ja alas. Seinää vastaa arvo 1, avointa kulkua arvo 0.

        Args:
            seedling:   Seed-arvo, joka on määritelty config.py-tiedostossa. Käyttäjä voi halutessaan vaihtaa
                        algoritmin käyttämää seed-arvoa konfiguraatiotiedostossa.
        """

        seed(seedling)
        w = self._w
        x, y = w, w
        self._maze.single_cell(x, y)
        grid = self._grid
        solution = self._solution
        stack = {}
        stack[(x, y)] = (1, 1, 1, 1)
        self._visited = {}
        self._visited[(x, y)] = (1, 1, 1, 1)
        while len(stack) > 0:
            time.sleep(Config.WILSON_MYSTEERI)
            cell_list = []
            if (x + w, y) not in self._visited and (x + w, y) in grid:
                cell_list.append("right")

            if (x - w, y) not in self._visited and (x - w, y) in grid:
                cell_list.append("left")

            if (x, y + w) not in self._visited and (x, y + w) in grid:
                cell_list.append("down")

            if (x, y - w) not in self._visited and (x, y - w) in grid:
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
                    solution[(x, y)] = self._visited[(x, y)]
                    stack[(x, y)] = self._visited[(x, y)]
                    x += w
                    if (x, y) in self._visited:
                        e, f, g, h = self._visited[(x, y)]
                    else:
                        e, f, g, h = 1, 1, 1, 1
                    self._visited[(x, y)] = (0, f, g, h)
                    solution[(x, y)] = self._visited[(x, y)]
                    stack[(x, y)] = self._visited[(x, y)]

                elif cell_chosen == "left":
                    self._maze.push_left(x, y)

                    if (x, y) in self._visited:
                        e, f, g, h = self._visited[(x, y)]
                    else:
                        e, f, g, h = 1, 1, 1, 1
                    self._visited[(x, y)] = (0, f, g, h)
                    solution[(x, y)] = self._visited[(x, y)]
                    stack[(x, y)] = self._visited[(x, y)]
                    x -= w
                    if (x, y) in self._visited:
                        e, f, g, h = self._visited[(x, y)]
                    else:
                        e, f, g, h = 1, 1, 1, 1
                    self._visited[(x, y)] = (e, 0, g, h)
                    solution[(x, y)] = self._visited[(x, y)]
                    stack[(x, y)] = self._visited[(x, y)]

                elif cell_chosen == "down":
                    self._maze.push_down(x, y)

                    if (x, y) in self._visited:
                        e, f, g, h = self._visited[(x, y)]
                    else:
                        e, f, g, h = 1, 1, 1, 1
                    self._visited[(x, y)] = (e, f, g, 0)
                    solution[(x, y)] = self._visited[(x, y)]
                    stack[(x, y)] = self._visited[(x, y)]
                    y += w
                    if (x, y) in self._visited:
                        e, f, g, h = self._visited[(x, y)]
                    else:
                        e, f, g, h = 1, 1, 1, 1
                    self._visited[(x, y)] = (e, f, 0, h)
                    solution[(x, y)] = self._visited[(x, y)]
                    stack[(x, y)] = self._visited[(x, y)]

                elif cell_chosen == "up":
                    self._maze.push_up(x, y)

                    if (x, y) in self._visited:
                        e, f, g, h = self._visited[(x, y)]
                    else:
                        e, f, g, h = 1, 1, 1, 1
                    self._visited[(x, y)] = (e, f, 0, h)
                    solution[(x, y)] = self._visited[(x, y)]
                    stack[(x, y)] = self._visited[(x, y)]
                    y -= w
                    if (x, y) in self._visited:
                        e, f, g, h = self._visited[(x, y)]
                    else:
                        e, f, g, h = 1, 1, 1, 1
                    self._visited[(x, y)] = (e, f, g, 0)
                    solution[(x, y)] = self._visited[(x, y)]
                    stack[(x, y)] = self._visited[(x, y)]

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

    def get_visited(self):

        """ Testauksessa käytetty metodi, joka palauttaa labyrintin.

        Returns:
            algoritmin luoman ja tallentaman valmiin labyrintin sanakirjamuodossa.
        """

        return self._visited
