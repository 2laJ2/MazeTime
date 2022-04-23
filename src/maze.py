import pygame
from wilson import Wilson
from abmaze import Abmaze
from mysteerimaze import Mysteerimaze
from comparison import Comparison
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
        self._x_max, self._y_max, self._w = Config.x_max, Config.y_max, Config.w
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
    def build_grid(self):
        w = self._w
        x, y = 0, 0
        for i in range(1, self._y_max + 1):
            x = w          # set x coordinate to start position
            y = y + w       # start a new row
            for j in range(1, self._x_max + 1):
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
        print("4. Suorituskykytestaus")
        print('q. Lopeta ohjelma')
        print()
        resp=None
        while resp not in ['1', '2', '3', '4', 'Q']:
            resp = str(input("Anna numero\n")).upper().strip()

        if resp == "Q":
            print("Nähdään taas!")
            self.event == pygame.QUIT
        elif resp == '1':
            print("Valitse luku yhdestä viiteen")
            resp=None
            while resp not in ['1', '2', '3', '4', '5']:
                resp = str(input("Anna luku\n")).upper().strip()
            self.reset_grid()
            self.build_grid()
            mysteerimaze = Mysteerimaze(self, self._x_max, self._y_max, self._w)
            mysteerimaze.carve_mysteerimaze(0, resp)
            # print(mysteerimaze.get_visited()) # tällä komennolla sovellus palauttaa labyrintin
                                                # tuple-listana komentorivillä
        elif resp == '2':
            self.reset_grid()
            self.build_grid()
            abmaze = Abmaze(self, self._x_max, self._y_max, self._w)
            abmaze.carve_AB_maze(0)
            # print(abmaze.get_visited()) # tällä komennolla sovellus palauttaa labyrintin
        elif resp == '3':
            self.reset_grid()
            self.build_grid()
            wilson = Wilson(self, self._x_max, self._y_max, self._w)
            wilson.carve_Wilson_maze(0)
            # print(wilson.get_visited()) # tällä komennolla sovellus palauttaa labyrintin
        elif resp == '4':
            print(f"{' VALITSE ALGORITMI ':_^30}")
            print("1. Mysteerialgoritmi")
            print("2. Aldous-Broder")
            print("3. Wilson")
            resp=None
            while resp not in ['1', '2', '3']:
                resp = str(input("Anna luku\n")).upper().strip()
            self.reset_grid()
            self.build_grid()
            # tähän toteutetaan myöhemmin myös muut algoritmit
            abmaze = Abmaze(self, self._x_max, self._y_max, self._w)
            comparison = Comparison(abmaze)
            print("Aldous-Broderin algoritmia käyttävän metodin suoritusaika sekunneissa on keskimäärin")
            print(comparison.test_time_complexity())
        self.main_menu()

if __name__ == "__main__":
    Maze()
