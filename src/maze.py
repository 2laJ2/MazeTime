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
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        pygame.display.set_caption("Python Labyrintti")
        self._x_max, self._y_max, self._w = Config.x_max, Config.y_max, Config.w
        self.main_menu()
        ###### pygame loop #######
        RUNNING = True
        while RUNNING:
            self.clock.tick(Config.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUNNING = False

    def reset_grid(self):

        """ Alustaa uudelleen Pygame-ikkunan, johon labyrintti piirretään. """

        pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        pygame.display.set_caption("Python Labyrintti")

    def build_grid(self):

        """ Piirtää valkoisen ruudukon, johon labyrintti piirretään. """

        w = self._w
        x, y = 0, 0
        for i in range(1, self._y_max + 1):
            x = w          # x koordinaatin asetus aloituskohtaan
            y = y + w      # uuden rivin aloitus
            for j in range(1, self._x_max + 1):
                pygame.draw.line(self.screen, Config.WHITE, [x, y], [x + w, y])
                pygame.draw.line(self.screen, Config.WHITE, [x + w, y], [x + w, y + w])
                pygame.draw.line(self.screen, Config.WHITE, [x + w, y + w], [x, y + w])
                pygame.draw.line(self.screen, Config.WHITE, [x, y + w], [x, y])
                self._grid.append((x,y))
                x = x + w

    """ Seuraavilla metodeilla poistetaan ruutujen välinen seinä kuljettaessa seuraavaan ruutuun. """

    def push_up(self, x, y):
        w = self._w
        pygame.draw.rect(self.screen, Config.LABYRINTH_COLOUR, (x + 1, y - w + 1, w - 1, (2*w) - 1), 0)
        pygame.display.update()

    def push_down(self, x, y):
        w = self._w
        pygame.draw.rect(self.screen, Config.LABYRINTH_COLOUR, (x + 1, y + 1, w - 1, (2*w) - 1), 0)
        pygame.display.update()

    def push_left(self, x, y):
        w = self._w
        pygame.draw.rect(self.screen, Config.LABYRINTH_COLOUR, (x - w + 1, y + 1, (2*w) - 1, w - 1), 0)
        pygame.display.update()

    def push_right(self, x, y):
        w = self._w
        pygame.draw.rect(self.screen, Config.LABYRINTH_COLOUR, (x + 1, y + 1, (2*w) - 1, w - 1), 0)
        pygame.display.update()

    """ Seuraavilla metodeilla piirretään yksi värillinen ruutu. """

    def single_cell(self, x, y):
        w = self._w
        pygame.draw.rect(self.screen, Config.BLUE, (x + 1 + w//6, y + 1 + w//6, w - 2 - w//3, w - 2 - w//3), 0)
        pygame.display.update()

    def single_purple_cell(self, x, y):
        w = self._w
        pygame.draw.rect(self.screen, Config.LABYRINTH_COLOUR, (x + 1, y + 1, w - 2, w - 2), 0)
        pygame.display.update()

    def single_yellow_cell(self, x, y):
        w = self._w
        pygame.draw.rect(self.screen, Config.YELLOW, (x + 1, y + 1, w - 2, w - 2), 0)
        pygame.display.update()

    def backtracking_cell(self, x, y):
        w = self._w
        pygame.draw.rect(self.screen, Config.LABYRINTH_COLOUR, (x + 1, y + 1, w - 2, w - 2), 0)
        pygame.display.update()

    def backtracking_blue_cell(self, x, y):
        w = self._w
        pygame.draw.rect(self.screen, Config.BLUE, (x + 1, y + 1, w - 2, w - 2), 0)
        pygame.display.update()

    def solution_cell(self, x,y):
        w = self._w
        pygame.draw.rect(self.screen, Config.YELLOW, (x + 8, y + 8, 5, 5), 0)
        pygame.display.update()

    def main_menu(self):

        """ Käyttäjälle komentoruudulla näkyvän valikon luominen ja ohjelman käynnistys. """

        print(f"{' VALITSE ALGORITMI ':_^30}")
        print("1. Mysteerialgoritmi")
        print("2. Aldous-Broder")
        print("3. Wilson")
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
            mysteerimaze.carve_mysteerimaze(Config.SEED, resp)
            #print(mysteerimaze.get_visited())# tulostaa labyrintin komentorivillä
            pituus = len(mysteerimaze.get_visited())
            print("ruutuja labyrintissa:", pituus)
            comparison = Comparison(mysteerimaze)
            comparison.test_lukumaarat(mysteerimaze.get_visited(), "k")
            print("labyrintissa olevien käytävien pituudet:")
            comparison.test_kaytavien_pituudet(mysteerimaze.get_visited(), ".")
            comparison.piirra_reitti(mysteerimaze.get_visited())
            print("labyrintin läpi kulkevan reitin käytävien pituudet:")
            comparison.test_kaytavien_pituudet(mysteerimaze.get_visited(), "k")
        elif resp == '2':
            self.reset_grid()
            self.build_grid()
            abmaze = Abmaze(self, self._x_max, self._y_max, self._w)
            abmaze.carve_AB_maze(Config.SEED)
            #print(abmaze.get_visited())
            pituus = len(abmaze.get_visited())
            print("ruutuja labyrintissa:", pituus)
            comparison = Comparison(abmaze)
            comparison.test_lukumaarat(abmaze.get_visited(), "k")
            print("labyrintissa olevien käytävien pituudet:")
            comparison.test_kaytavien_pituudet(abmaze.get_visited(), ".")
            comparison.piirra_reitti(abmaze.get_visited())
            print("labyrintin läpi kulkevan reitin käytävien pituudet:")
            comparison.test_kaytavien_pituudet(abmaze.get_visited(), "k")
        elif resp == '3':
            self.reset_grid()
            self.build_grid()
            wilson = Wilson(self, self._x_max, self._y_max, self._w)
            wilson.carve_Wilson_maze(Config.SEED)
            #print(wilson.get_visited())
            pituus = len(wilson.get_visited())
            print("ruutuja labyrintissa:", pituus)
            comparison = Comparison(wilson)
            comparison.test_lukumaarat(wilson.get_visited(), "k")
            print("labyrintissa olevien käytävien pituudet:")
            comparison.test_kaytavien_pituudet(wilson.get_visited(), ".")
            comparison.piirra_reitti(wilson.get_visited())
            print("labyrintin läpi kulkevan reitin käytävien pituudet:")
            comparison.test_kaytavien_pituudet(wilson.get_visited(), "k")
        self.main_menu()

if __name__ == "__main__":
    Maze()
