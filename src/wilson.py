from pickle import FALSE
from pickle import TRUE
import time
import random
from random import seed
from random import randint
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

    # apumetodi, jolla luodaan lista ruuduista, joissa ei ole käyty
    def reverse_stack_builder(self, x_max, y_max):
        w = self._w
        stack = []
        for i in range(1, x_max+1):
            x = i*w
            for j in range(1, y_max+1):
                y = j*w
                stack.append((x, y))
        return stack

    # apumetodi, jolla liitetään viimeksi kuljettu polku labyrinttiin ja tyhjennetään polku
    def wilson_path(self, solution, a, b):
        w = self._w
        self._maze.single_purple_cell(a, b)
        for cell in solution:# käydään uudelleen reitti läpi ja liitetään se valmiiseen labyrinttiin
            if  cell == "right":
                self._maze.push_right(a, b)
                a += w
            if cell == "left":
                self._maze.push_left(a, b)
                a -= w
            if cell == "down":
                self._maze.push_down(a, b)
                b += w
            if cell == "up":
                self._maze.push_up(a, b)
                b -= w
        return []

    # metodi, joka luo parametrina annetulla seed-arvolla labyrintin
    def carve_Wilson_maze(self, seedling):
        seed(seedling)
        w = self._w
        grid = self._grid
        x = (randint(0, self._x_max-1))*w
        y = (randint(0, self._y_max-1))*w
        a = x
        b = y
        solution = []
        stack = []
        counter = 0
        not_visited = self.reverse_stack_builder(self._x_max, self._y_max)# labyrintin koko x, y
        while len(not_visited) > 0:# labyrintin ruutujen lukumäärä alussa 400
                            # jos haluat tarkastella labyrinttia, pysäytä viimeiseen ruutuun laittamalla 0:n tilalle 1
            if (x, y) in not_visited:# jos ruutu on vapaa 
                not_visited.remove((x, y))# poista vapaiden ruutujen luettelosta
                stack.append((x, y))# lisää nykyiseen polkuun
        
            
            self._maze.single_yellow_cell(x,y)
            time.sleep(0.001)
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
                    if (x + w, y) not in not_visited:# on käyty aiemmin
                        solution.append(cell_chosen)#
                        a, b = (stack[0])
                        solution = self.wilson_path(solution, a, b)# liittää polun labyrinttiin, tyhjentää polun
                        stack = []
                        if len(not_visited) != 0: x, y = (random.choice(not_visited))
                        a, b = x, y
                    elif (x + w, y) in not_visited:# ei ole käyty aiemmin
                        x += w
                        not_visited.remove((x, y))
                        stack.append((x, y))
                        solution.append(cell_chosen)# lisätään ruutu reittiin
                        
                elif cell_chosen == "left":
                    if (x - w, y) not in not_visited:
                        solution.append(cell_chosen)
                        a, b = (stack[0])
                        solution = self.wilson_path(solution, a, b)
                        stack = []
                        if len(not_visited) != 0: x, y = (random.choice(not_visited))
                        a, b = x, y
                    elif (x - w, y) in not_visited:
                        x -= w
                        not_visited.remove((x, y)) 
                        stack.append((x, y))
                        solution.append(cell_chosen)
                        
                elif cell_chosen == "down":
                    if (x, y + w) not in not_visited:
                        solution.append(cell_chosen)
                        a, b = (stack[0])
                        solution = self.wilson_path(solution, a, b)
                        stack = []
                        if len(not_visited) != 0: x, y = (random.choice(not_visited))
                        a, b = x, y
                    elif (x, y + w) in not_visited:
                        y += w
                        not_visited.remove((x, y))
                        stack.append((x, y))
                        solution.append(cell_chosen)#
                        
                elif cell_chosen == "up":
                    if (x, y - w) not in not_visited:
                        solution.append(cell_chosen)
                        a, b = (stack[0])
                        solution = self.wilson_path(solution, a, b)
                        stack = []
                        if len(not_visited) != 0: x, y = (random.choice(not_visited))
                        a, b = x, y
                    elif (x, y - w) in not_visited:
                        y -= w
                        not_visited.remove((x, y))
                        stack.append((x, y))
                        solution.append(cell_chosen)#
                        
            elif len(cell_list)==0:# jos tullaan nykyisen polun muodostamaan umpikujaan 
                
                if counter == 1:#ensimmäisen kerran jälkeen
                    x, y = (random.choice(not_visited))# hyppy
                    for cell_list in stack:# merkitään kuljetun polun ruudut takaisin ei käydyiksi
                        not_visited.append(cell_list)
                    stack = []# tyhjennetään polku
                    solution = []# tyhjennetään piirrettävä reitti
                    solution.append((x, y))# lisätään piirrettävään polkuun nykyinen ruutu
                if counter == 0:# ensimmäinen kerta
                    stack = []# tyhjennetään polku
                    solution = self.wilson_path(solution, a, b)# # liittää polun labyrinttiin, tyhjentää polun
                    x, y = (random.choice(not_visited))# hyppy
                    solution.append((x,y))# lisätään piirrettävään polkuun nykyinen ruutu
                    counter += 1            
