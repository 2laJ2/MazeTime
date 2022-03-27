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
pygame.display.set_caption("Python Maze Generator")
clock = pygame.time.Clock()

# setup maze variables
x = 0                    # x axis
y = 0                    # y axis
w = 20                   # width of cell
grid = []
visited = []
stack = []
solution = {}

# build the grid
def build_grid(x, y, w):
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

def backtracking_cell(x, y):
    pygame.draw.rect(screen, PURPLE, (x + 1, y + 1, w - 2, w - 2), 0)
    pygame.display.update()                                                   # has visited cell


def solution_cell(x,y):
    pygame.draw.rect(screen, YELLOW, (x + 8, y + 8, 5, 5), 0)      # used to show the solution
    pygame.display.update()                                        # has visited cell

# depth-first search backtracking; iterative implementation
def carve_out_maze(x,y):
    single_cell(x, y)                                              # starting positing of maze
    stack.append((x,y))                                            # place starting cell into stack
    visited.append((x,y))                                          # add starting cell to visited list
    while len(stack) > 0:                                          # loop until stack is empty
        time.sleep(.01)                                            # slow program now a bit
        cell = []
        if (x + w, y) not in visited and (x + w, y) in grid:       # right cell available?
            cell.append("right")                                   # if yes add to cell list

        if (x - w, y) not in visited and (x - w, y) in grid:       # left cell available?
            cell.append("left")

        if (x , y + w) not in visited and (x , y + w) in grid:     # down cell available?
            cell.append("down")

        if (x, y - w) not in visited and (x , y - w) in grid:      # up cell available?
            cell.append("up")

        if len(cell) > 0:                                          # check to see if cell list is empty
            cell_chosen = (random.choice(cell))                    # select one of the cell randomly

            if cell_chosen == "right":           # if this cell has been chosen
                push_right(x, y)                 # call push_right function
                solution[(x + w, y)] = x, y      # solution = dictionary key = new cell, other = current cell
                x = x + w                        # make this cell the current cell
                visited.append((x, y))           # add to visited list
                stack.append((x, y))             # place current cell on to stack

            elif cell_chosen == "left":
                push_left(x, y)
                solution[(x - w, y)] = x, y
                x = x - w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "down":
                push_down(x, y)
                solution[(x , y + w)] = x, y
                y = y + w
                visited.append((x, y))
                stack.append((x, y))

            elif cell_chosen == "up":
                push_up(x, y)
                solution[(x , y - w)] = x, y
                y = y - w
                visited.append((x, y))
                stack.append((x, y))
        else:
            x, y = stack.pop()
            single_cell(x, y)
            time.sleep(.05)
            backtracking_cell(x, y)

# Aldous-Broder algorithm
def carve_AB_maze(seedling):
    seed(seedling)
    x = (randint(0, w-1))*20
    y = (randint(0, w-1))*20
    visits = 0
    while visits < 400:# labyrintin ruutujen lukumäärä
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

def plot_route_back(x,y):
    solution_cell(x, y)         # solution list contains all the coordinates to route back to start
    while (x, y) != (20,20):    # loop until cell position == start position
        x, y = solution[x, y]   # "key value" now becomes the new key
        solution_cell(x, y)     # animate route back
        time.sleep(.01)


x, y = 20, 20              # starting position of grid
build_grid(40, 0, w)       # 1st argument=x value, 2nd argument=y value, 3rd argument=width of cell
#carve_out_maze(x,y)       # call build the maze  function
#plot_route_back(400, 400) # call the plot solution function
carve_AB_maze(0)           # luo Aldous-Broderin algoritmilla seed-arvolla 0 labyrintin, jota ei
                           # voi ratkaista valmiin metodin avulla, koska lähtöpiste vaihtelee

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
