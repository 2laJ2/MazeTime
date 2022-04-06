import time
import random
from random import seed
from random import randint
import pygame


# set up pygame window
WIDTH = 500
HEIGHT = 600
FPS = 30

# define colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTBLUE = (0, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255 ,255 ,0)
ORANGE = (255, 175, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

# setup maze variables
x = 0                    # x axis
y = 0                    # y axis
w = 20                   # width of cell
grid = []
visited = []
stack = []
solution = {}
stack_current = []

# initalise Pygame
class Maze():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Python Labyrintti")
        self.clock = pygame.time.Clock()
        self.x, self.y = 20, 20
        self.main_menu()
        ###### pygame loop #######
        RUNNING = True
        while RUNNING:
            # keep running at the at the right speed
            self.clock.tick(FPS)
            # process input (events)
            for event in pygame.event.get():
                # check for closing the window
                if event.type == pygame.QUIT:
                    RUNNING = False

# reset the grid
    def reset_grid(self):
        pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Python Labyrintti")

# build the grid
    def build_grid(self, x, y, w):              # 1st argument=x value, 2nd argument=y value, 3rd argument=width of cell
        for i in range(1, w + 1):
            x = w                                                             # set x coordinate to start position
            y = y + w                                                         # start a new row
            for j in range(1, w + 1):
                pygame.draw.line(self.screen, WHITE, [x, y], [x + w, y])           # top of cell
                pygame.draw.line(self.screen, WHITE, [x + w, y], [x + w, y + w])   # right of cell
                pygame.draw.line(self.screen, WHITE, [x + w, y + w], [x, y + w])   # bottom of cell
                pygame.draw.line(self.screen, WHITE, [x, y + w], [x, y])           # left of cell
                grid.append((x,y))                                            # add cell to grid list
                x = x + w                                                     # move cell to new position

    def push_up(self, x, y):
        pygame.draw.rect(self.screen, PURPLE, (x + 1, y - w + 1, w - 1, (2*w) - 1), 0)
        pygame.display.update()

    def push_down(self, x, y):
        pygame.draw.rect(self.screen, PURPLE, (x + 1, y + 1, w - 1, (2*w) - 1), 0)
        pygame.display.update()

    def push_left(self, x, y):
        pygame.draw.rect(self.screen, PURPLE, (x - w + 1, y + 1, (2*w) - 1, w - 1), 0)
        pygame.display.update()

    def push_right(self, x, y):
        pygame.draw.rect(self.screen, PURPLE, (x + 1, y + 1, (2*w) - 1, w - 1), 0)
        pygame.display.update()

    def single_cell(self, x, y):
        pygame.draw.rect(self.screen, BLUE, (x + 1, y + 1, w - 2, w - 2), 0)           # draw a single width cell
        pygame.display.update()

    def single_purple_cell(self, x, y):
        pygame.draw.rect(self.screen, PURPLE, (x + 1, y + 1, w - 2, w - 2), 0)         # draw a single width cell
        pygame.display.update()

    def single_yellow_cell(self, x, y):
        pygame.draw.rect(self.screen, YELLOW, (x + 1, y + 1, w - 2, w - 2), 0)         # draw a single width cell
        pygame.display.update()

    def backtracking_cell(self, x, y):
        pygame.draw.rect(self.screen, PURPLE, (x + 1, y + 1, w - 2, w - 2), 0)
        pygame.display.update()                                                        # has visited cell

    def backtracking_blue_cell(self, x, y):
        pygame.draw.rect(self.screen, BLUE, (x + 1, y + 1, w - 2, w - 2), 0)
        pygame.display.update()

    def solution_cell(self, x,y):
        pygame.draw.rect(self.screen, YELLOW, (x + 8, y + 8, 5, 5), 0)      # used to show the solution
        pygame.display.update()                                        # has visited cell

    def main_menu(self):
        print(f"{' VALITSE ALGORITMI ':_^30}")
        print("1. Mysteerialgoritmi")
        print("2. Aldous-Broder")
        print("3. Wilson")
        print('q. Lopeta ohjelma')
        print()
        resp=None
        while resp not in ['1', '2', '3', 'Q']:
            resp = str(input("Anna numero\n")).upper().strip()

        if resp == "Q":
            print("Nähdään taas!")
            self.event == pygame.QUIT
        elif resp == '1':
            print("Valitse luku yhdestä viiteen")
            resp=None
            while resp not in ['1', '2', '3', '4', '5']:
                resp = str(input("Anna numero\n")).upper().strip()
            self.reset_grid()
            self.build_grid(40, 0, w)
            x, y = 20, 20
            mysteerimaze = Mysteerimaze(self)
            mysteerimaze.carve_mysteerimaze(x, y, resp)
        elif resp == '2':
            self.reset_grid()
            self.build_grid(40, 0, w)
            ab_maze = AB_maze(self)
            ab_maze.carve_AB_maze(0)
        elif resp == '3':
            self.reset_grid()
            self.build_grid(40, 0, w)
            wilson = Wilson(self)
            wilson.carve_Wilson_maze(0)
        self.main_menu()

if __name__ == "__main__":
    main()


class Mysteerimaze():

    def __init__(self, maze):
        self._maze = maze

    def gt_always_last(self, stack, x, y):# valitsee viimeisimmän lisätyn ruudun ja poistaa sen pinosta
        x, y = stack.pop()# algoritmi muuttuu recursive backtracking -algoritmiksi
        self._maze.single_yellow_cell(x, y)
        time.sleep(.05)
        self._maze.backtracking_cell(x, y)
        return stack, x, y

    def gt_always_random(self, stack, x, y):# poistaa ruudun pinosta ja valitsee pinosta satunnaisen ruudun
        if len(stack) > 0:
            stack.remove((x, y))
            if len(stack)>0:
                x, y = (random.choice(stack))
                self._maze.single_cell(x, y)
                time.sleep(.05)
                self._maze.backtracking_cell(x, y) 
        return stack, x, y          

    def gt_always_first(self, stack, x, y):# poistaa ruudun pinosta ja valitsee pinon ensimmäisen ruudun
        if len(stack) > 0:
            stack.remove((x, y))
            if len(stack) > 0:
                x, y = stack[0]
                self._maze.single_cell(x, y)
                time.sleep(.05)
                self._maze.backtracking_cell(x, y)
        return stack, x, y

    def gt_usually_last_occasionally_random(self, stack, x, y):
        if len(stack) > 0:# poistaa ruudun pinosta ja valitsee yleensä viimeisimmän, välillä satunnaisen ruudun pinosta
            choice = (randint(1, 5))
            if choice == 1:
                x, y = (random.choice(stack))    
            else:
                x, y = stack.pop()
                self._maze.single_cell(x, y)
                time.sleep(.05)
                self._maze.backtracking_cell(x, y)
        return stack, x, y

    def gt_random_among_last_ones(self, stack, x, y):# poistaa ruudun pinosta ja valitsee satunnaisen ruudun viimeisten ruutujen joukosta
        if len(stack) > 0:
            stack.remove((x, y))
            length = len(stack)
            latest = len(stack)//10
            list = []
            for i in range(latest, length):
                list.append((stack[i]))
                if len(list) > 0:
                    x, y = (random.choice(list))
            self._maze.single_cell(x, y)
            time.sleep(.05)
            self._maze.backtracking_cell(x, y)
        return stack, x, y

    # Growing Tree algorithm
    def carve_mysteerimaze(self, x, y, option):
        self._maze.single_cell(x, y)
        stack = []
        stack.append((x,y))
        visited = []
        visited.append((x,y))
        while len(stack) > 0:
            time.sleep(.07)
            cell_list = []
            if (x + w, y) not in visited and (x + w, y) in grid:
                cell_list.append("right")

            if (x - w, y) not in visited and (x - w, y) in grid:
                cell_list.append("left")

            if (x , y + w) not in visited and (x , y + w) in grid:
                cell_list.append("down")

            if (x, y - w) not in visited and (x , y - w) in grid:
                cell_list.append("up")

            if len(cell_list) > 0:
                cell_chosen = (random.choice(cell_list))

                if cell_chosen == "right":
                    self._maze.push_right(x, y)
                    solution[(x + w, y)] = x, y
                    x = x + w
                    visited.append((x, y))
                    stack.append((x, y))

                elif cell_chosen == "left":
                    self._maze.push_left(x, y)
                    solution[(x - w, y)] = x, y
                    x = x - w
                    visited.append((x, y))
                    stack.append((x, y))

                elif cell_chosen == "down":
                    self._maze.push_down(x, y)
                    solution[(x , y + w)] = x, y
                    y = y + w
                    visited.append((x, y))
                    stack.append((x, y))

                elif cell_chosen == "up":
                    self._maze.push_up(x, y)
                    solution[(x , y - w)] = x, y
                    y = y - w
                    visited.append((x, y))
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
          
class AB_maze():

    def __init__(self, maze):
        self._maze = maze

    # Aldous-Broder algorithm
    def carve_AB_maze(self, seedling): # luo seed-arvolla 0 labyrintin
        seed(seedling)
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

class Wilson():
    def __init__(self, maze):
        self._maze = maze

    def reverse_stack_builder(self, x_max, y_max):
        stack = []
        for i in range(1, x_max+1):
            x = i*w
            for j in range(1, y_max+1):
                y = j*w
                stack.append((x, y))
        return stack

    def wilson_path(self, solution, a, b):
        self._maze.single_purple_cell(a, b)
        for cell in solution:# käydään uudelleen reitti läpi ja liitetään se valmiiseen labyrinttiin
            if  cell == "right":
                self._maze.push_right(a, b)
                a += w
            if cell == "left":
                self._maze.push_left(a, b)
                a -=w
            if cell == "down":
                self._maze.push_down(a, b)
                b += w
            if cell == "up":
                self._maze.push_up(a, b)
                b -= w
        return []

    # Wilson algorithm
    def carve_Wilson_maze(self, seedling):
        seed(seedling)
        x = (randint(0, w-1))*20
        y = (randint(0, w-1))*20
        a = x
        b = y
        solution = []
        stack = []
        counter = 0
        not_visited = self.reverse_stack_builder(20, 20)# labyrintin koko x, y
        while len(not_visited) > 0:# labyrintin ruutujen lukumäärä alussa 400
                            # jos haluat tarkastella labyrinttia, pysäytä viimeiseen ruutuun laittamalla 0:n tilalle 1
            if (x, y) in not_visited:# jos ruutu on vapaa 
                not_visited.remove((x, y))# poista vapaiden ruutujen luettelosta
                stack.append((x, y))# lisää nykyiseen polkuun
        
            self._maze.single_yellow_cell(x, y)
            time.sleep(0.01)
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
