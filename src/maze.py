import time
import random
from random import seed
from random import randint
import pygame
from wilson import Wilson
from abmaze import Abmaze
from mysteerimaze import Mysteerimaze
from config import Config


"""
Pygamen avulla labyrintin visualisoinnin rakentava luokka
"""
class Maze():
    def __init__(self):
        self._grid = Config.grid
        self._solution = Config.solution
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        pygame.display.set_caption("Python Labyrintti")
        self.clock = pygame.time.Clock()
        self._x, self._y, self._w = Config.x, Config.y, Config.w
        self.main_menu()
        ###### pygame loop #######
        RUNNING = True
        while RUNNING:
            # keep running at the at the right speed
            self.clock.tick(Config.FPS)
            # process input (events)
            for event in pygame.event.get():
                # check for closing the window
                if event.type == pygame.QUIT:
                    RUNNING = False

    # reset the grid
    def reset_grid(self):
        pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        pygame.display.set_caption("Python Labyrintti")

    # build the grid
    def build_grid(self, w):
        x, y = 0, 0
        for i in range(1, w + 1):
            x = w           # set x coordinate to start position
            y = y + w       # start a new row
            for j in range(1, w + 1):
                pygame.draw.line(self.screen, Config.WHITE, [x, y], [x + w, y])           # top of cell
                pygame.draw.line(self.screen, Config.WHITE, [x + w, y], [x + w, y + w])   # right of cell
                pygame.draw.line(self.screen, Config.WHITE, [x + w, y + w], [x, y + w])   # bottom of cell
                pygame.draw.line(self.screen, Config.WHITE, [x, y + w], [x, y])           # left of cell
                self._grid.append((x,y))                                      # add cell to grid list
                x = x + w                                                     # move cell to new position

    def push_up(self, x, y):
        w = self._w
        pygame.draw.rect(self.screen, Config.PURPLE, (x + 1, y - w + 1, w - 1, (2*w) - 1), 0)
        pygame.display.update()

    def push_down(self, x, y):
        w = self._w
        pygame.draw.rect(self.screen, Config.PURPLE, (x + 1, y + 1, w - 1, (2*w) - 1), 0)
        pygame.display.update()

    def push_left(self, x, y):
        w = self._w
        pygame.draw.rect(self.screen, Config.PURPLE, (x - w + 1, y + 1, (2*w) - 1, w - 1), 0)
        pygame.display.update()

    def push_right(self, x, y):
        w = self._w
        pygame.draw.rect(self.screen, Config.PURPLE, (x + 1, y + 1, (2*w) - 1, w - 1), 0)
        pygame.display.update()

    def single_cell(self, x, y): # draw a single width cell
        w = self._w
        pygame.draw.rect(self.screen, Config.BLUE, (x + 1, y + 1, w - 2, w - 2), 0)
        pygame.display.update()

    def single_purple_cell(self, x, y):
        w = self._w
        pygame.draw.rect(self.screen, Config.PURPLE, (x + 1, y + 1, w - 2, w - 2), 0)
        pygame.display.update()

    def single_yellow_cell(self, x, y):
        w = self._w
        pygame.draw.rect(self.screen, Config.YELLOW, (x + 1, y + 1, w - 2, w - 2), 0)
        pygame.display.update()

    def backtracking_cell(self, x, y):
        w = self._w
        pygame.draw.rect(self.screen, Config.PURPLE, (x + 1, y + 1, w - 2, w - 2), 0)
        pygame.display.update() # has visited cell

    def backtracking_blue_cell(self, x, y):
        w = self._w
        pygame.draw.rect(self.screen, Config.BLUE, (x + 1, y + 1, w - 2, w - 2), 0)
        pygame.display.update()

    def solution_cell(self, x,y): # used to show the solution
        w = self._w
        pygame.draw.rect(self.screen, Config.YELLOW, (x + 8, y + 8, 5, 5), 0)
        pygame.display.update() # has visited cell

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
            self.build_grid(self._w)
            mysteerimaze = Mysteerimaze(self, self._w, self._solution)
            mysteerimaze.carve_mysteerimaze(0, self._x, self._y, resp)
        elif resp == '2':
            self.reset_grid()
            self.build_grid(self._w)
            abmaze = Abmaze(self, self._w)
            abmaze.carve_AB_maze(0)
        elif resp == '3':
            self.reset_grid()
            self.build_grid(self._w)
            wilson = Wilson(self, self._w)
            wilson.carve_Wilson_maze(0)
        self.main_menu()

if __name__ == "__main__":
    Maze()