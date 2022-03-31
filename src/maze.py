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

# initalise Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Labyrintti")
clock = pygame.time.Clock()

# setup maze variables
x = 0                    # x axis
y = 0                    # y axis
w = 20                   # width of cell
grid = []
visited = []
stack = []
solution = {}
stack_current = []

# reset the grid
def reset_grid():
    pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Python Labyrintti")


# build the grid
def build_grid(x, y, w):              # 1st argument=x value, 2nd argument=y value, 3rd argument=width of cell
    for i in range(1, w + 1):
        x = w                                                             # set x coordinate to start position
        y = y + w                                                         # start a new row
        for j in range(1, w + 1):
            pygame.draw.line(screen, WHITE, [x, y], [x + w, y])           # top of cell
            pygame.draw.line(screen, WHITE, [x + w, y], [x + w, y + w])   # right of cell
            pygame.draw.line(screen, WHITE, [x + w, y + w], [x, y + w])   # bottom of cell
            pygame.draw.line(screen, WHITE, [x, y + w], [x, y])           # left of cell
            grid.append((x,y))                                            # add cell to grid list
            x = x + w                                                     # move cell to new position


def push_up(x, y):
    pygame.draw.rect(screen, PURPLE, (x + 1, y - w + 1, w - 1, (2*w) - 1), 0)
    pygame.display.update()


def push_down(x, y):
    pygame.draw.rect(screen, PURPLE, (x + 1, y + 1, w - 1, (2*w) - 1), 0)
    pygame.display.update()


def push_left(x, y):
    pygame.draw.rect(screen, PURPLE, (x - w + 1, y + 1, (2*w) - 1, w - 1), 0)
    pygame.display.update()


def push_right(x, y):
    pygame.draw.rect(screen, PURPLE, (x + 1, y + 1, (2*w) - 1, w - 1), 0)
    pygame.display.update()


def single_cell( x, y):
    pygame.draw.rect(screen, BLUE, (x + 1, y + 1, w - 2, w - 2), 0)           # draw a single width cell
    pygame.display.update()

def single_purple_cell( x, y):
    pygame.draw.rect(screen, PURPLE, (x + 1, y + 1, w - 2, w - 2), 0)         # draw a single width cell
    pygame.display.update()

def single_yellow_cell( x, y):
    pygame.draw.rect(screen, YELLOW, (x + 1, y + 1, w - 2, w - 2), 0)         # draw a single width cell
    pygame.display.update()

def backtracking_cell(x, y):
    pygame.draw.rect(screen, PURPLE, (x + 1, y + 1, w - 2, w - 2), 0)
    pygame.display.update()                                                   # has visited cell


def solution_cell(x,y):
    pygame.draw.rect(screen, YELLOW, (x + 8, y + 8, 5, 5), 0)      # used to show the solution
    pygame.display.update()                                        # has visited cell

# depth-first search backtracking; iterative implementation
def carve_out_maze(x,y):
    pass

# Aldous-Broder algorithm
def carve_AB_maze(seedling): # luo seed-arvolla 0 labyrintin
    seed(seedling)
    x = (randint(0, w-1))*20
    y = (randint(0, w-1))*20
    visits = 0
    while len(visited) < 400: # labyrintin ruutujen lukumäärä
        if (x, y) not in visited: visited.append((x,y))
        single_purple_cell(x, y)
        time.sleep(.0001)
        cell = []
        if (x + w, y) in grid:
            cell.append("right")

        if (x - w, y) in grid:
            cell.append("left")

        if (x , y + w) in grid:
            cell.append("down")

        if (x , y - w) in grid:
            cell.append("up")

        cell_chosen = (random.choice(cell))

        if  cell_chosen == "right":
            if (x + w, y) not in visited:
                push_right(x, y)
                visited.append((x + w, y))
                visits += 1
            x = x + w

        elif cell_chosen == "left":
            if (x - w, y) not in visited:
                push_left(x, y)
                visited.append((x - w, y))
                visits += 1
            x = x - w

        elif cell_chosen == "down":
            if (x, y + w) not in visited:
                push_down(x, y)
                visited.append((x, y + w))
                visits += 1
            y = y + w

        elif cell_chosen == "up":
            if (x, y - w) not in visited:
                push_up(x, y)
                visited.append((x, y - w))
                visits += 1
            y = y - w

def reverse_stack_builder(x_max, y_max):
    stack = []
    for i in range(1, x_max+1):
        x = i*w
        for j in range(1, y_max+1):
            y = j*w
            stack.append((x, y))
    return stack

def wilson_path(solution, a, b):
    single_purple_cell(a, b)
    for cell in solution:# käydään uudelleen reitti läpi ja liitetään se valmiiseen labyrinttiin
        if  cell == "right":
            push_right(a, b)
            a += w
        if cell == "left":
            push_left(a, b)
            a -=w
        if cell == "down":
            push_down(a, b)
            b += w
        if cell == "up":
            push_up(a, b)
            b -= w
    return []

# Wilson algorithm
def carve_Wilson_maze(seedling):
    seed(seedling)
    x = (randint(0, w-1))*20
    y = (randint(0, w-1))*20
    a = x
    b = y
    solution = []
    stack = []
    counter = 0
    not_visited = reverse_stack_builder(20, 20)# labyrintin koko x, y
    while len(not_visited) > 0:# labyrintin ruutujen lukumäärä alussa 400
                           # jos haluat tarkastella labyrinttia, pysäytä viimeiseen ruutuun laittamalla 0:n tilalle 1
        if (x, y) in not_visited:# jos ruutu on vapaa 
            not_visited.remove((x, y))# poista vapaiden ruutujen luettelosta
            stack.append((x, y))# lisää nykyiseen polkuun
       
        single_yellow_cell(x, y)
        time.sleep(0.01)
        cell = []
            
        if (x + w, y) not in stack and (x + w, y) in grid:# ei nykyisessä polussa eli ei mennä taaksepäin
            cell.append("right")

        if (x - w, y) not in stack and (x - w, y) in grid:
            cell.append("left")

        if (x , y + w) not in stack and (x , y + w) in grid:
            cell.append("down")

        if (x , y - w) not in stack and (x , y - w) in grid:
            cell.append("up")

        if len(cell)>0:
            cell_chosen = (random.choice(cell))
            
            if  cell_chosen == "right":
                if (x + w, y) not in not_visited:# on käyty aiemmin
                    solution.append(cell_chosen)#
                    a, b = (stack[0])
                    solution = wilson_path(solution, a, b)# liittää polun labyrinttiin, tyhjentää polun
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
                    solution = wilson_path(solution, a, b)
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
                    solution = wilson_path(solution, a, b)
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
                    solution = wilson_path(solution, a, b)
                    stack = []
                    if len(not_visited) != 0: x, y = (random.choice(not_visited))
                    a, b = x, y
                elif (x, y - w) in not_visited:
                    y -= w
                    not_visited.remove((x, y))
                    stack.append((x, y))
                    solution.append(cell_chosen)#
                    
        elif len(cell)==0:# jos tullaan nykyisen polun muodostamaan umpikujaan 
            
            if counter == 1:#ensimmäisen kerran jälkeen
                x, y = (random.choice(not_visited))# hyppy
                for cell in stack:# merkitään kuljetun polun ruudut takaisin ei käydyiksi
                    not_visited.append(cell)
                stack = []# tyhjennetään polku
                solution = []# tyhjennetään piirrettävä reitti
                solution.append((x, y))# lisätään piirrettävään polkuun nykyinen ruutu
            if counter == 0:# ensimmäinen kerta
                stack = []# tyhjennetään polku
                solution = wilson_path(solution, a, b)# # liittää polun labyrinttiin, tyhjentää polun
                x, y = (random.choice(not_visited))# hyppy
                solution.append((x,y))# lisätään piirrettävään polkuun nykyinen ruutu
                counter += 1            

def main_menu():
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
            event == pygame.QUIT
        elif resp == '1':
            main_menu()
            return
        elif resp == '2':
            reset_grid()
            build_grid(40, 0, w)
            carve_AB_maze(0)
        elif resp == '3':
            reset_grid()
            build_grid(40, 0, w)
            carve_Wilson_maze(0)
        main_menu()

x, y = 20, 20          # starting position of grid
main_menu()


###### pygame loop #######
RUNNING = True
while RUNNING:
    # keep running at the at the right speed
    clock.tick(FPS)
    # process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            RUNNING = False
