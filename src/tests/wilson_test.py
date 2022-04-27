import unittest
from unittest.mock import Mock, ANY
from maze import Maze
from wilson import Wilson

class TestWilson(unittest.TestCase):
    def setUp(self):
        maze_mock = Mock()
        maze_mock._x_max = 10
        maze_mock._y_max = 10
        maze_mock._w = 20
        self.algoritmi = Wilson(maze_mock, maze_mock._x_max, maze_mock._y_max_, maze_mock._w)
        self.algoritmi._maze = maze_mock
        self.algoritmi._x_max = maze_mock._x_max
        self.algoritmi._y_max = maze_mock._y_max
        self.algoritmi._w = maze_mock._w
        self.algoritmi._grid = []
        self.algoritmi._visited = {}
        x, y = 0, 0
        for i in range(1, maze_mock._y_max + 1):
            x = self.algoritmi._w
            y = y + self.algoritmi._w
            for j in range(1, maze_mock._x_max + 1):
                self.algoritmi._grid.append((x,y))
                x = x + self.algoritmi._w
        self.maxDiff = None
    
    def test_metodi_reverse_stack_builder_toimii_oikein(self):
        self.assertEqual(self.algoritmi.reverse_stack_builder(2,2), {(20, 20):(1, 1, 1, 1), (20, 40):(1, 1, 1, 1), (40, 20):(1, 1, 1, 1), (40, 40):(1, 1, 1, 1)})

    def test_metodi_wilson_path_palauttaa_tyhjan_polun(self):
        self.assertEqual(self.algoritmi.wilson_path([],3,3), [])

    def test_algoritmi_kutsuu_maze_oliota(self):
        self.algoritmi.carve_Wilson_maze(0)
        self.algoritmi._maze.assert_any_call

    def test_algoritmi_kay_kaikissa_ruuduissa(self):
        self.algoritmi._not_visited = self.algoritmi.reverse_stack_builder(self.algoritmi._x_max, self.algoritmi._y_max)
        koko = len(self.algoritmi._not_visited)
        self.algoritmi.carve_Wilson_maze(0)
        self.assertEqual(len(self.algoritmi._not_visited), 0)
        self.assertEqual(len(self.algoritmi._visited), koko)

    def test_algoritmi_toimii_oikein(self):
        self.algoritmi.carve_Wilson_maze(0)
        labyrinth = {(120, 120): (1, 0, 0, 1), (140, 120): (0, 1, 1, 0), (140, 140): (1, 0, 0, 0), (140, 160)
        : (0, 1, 0, 1), (120, 160): (0, 0, 1, 0), (120, 180): (0, 1, 0, 0), (100, 180): (1, 0, 1, 0),
         (100, 200): (0, 1, 0, 1), (80, 200): (0, 0, 1, 1), (60, 200): (0, 0, 1, 1), (40, 200): (0, 0, 0, 1),
         (40, 180): (0, 0, 1, 0), (60, 180): (0, 0, 0, 1), (80, 180): (0, 1, 0, 1), (80, 160): (1, 1, 0, 0),
         (80, 140): (1, 1, 0, 0), (80, 120): (0, 1, 0, 0), (80, 100): (1, 0, 1, 0), (100, 100): (0, 1, 0, 0),
         (100, 120): (1, 1, 0, 0), (100, 140): (1, 0, 0, 1), (120, 140): (0, 1, 1, 1), (60, 160):
         (0, 1, 0, 0), (20, 180): (1, 0, 1, 1), (60, 100): (0, 1, 0, 1), (40, 100): (0, 0, 1, 1), (20, 100):
         (1, 0, 1, 0), (20, 120): (1, 0, 0, 0), (20, 140): (1, 0, 0, 1), (40, 140): (0, 0, 1, 1), (60, 140):
         (0, 1, 1, 0), (40, 80): (0, 1, 0, 1), (40, 60): (1, 0, 0, 0), (60, 60): (0, 1, 1, 0), (60, 80):
         (1, 0, 0, 0), (120, 100): (1, 0, 1, 0), (160, 200): (0, 0, 0, 1), (160, 180): (0, 1, 0, 0),
         (160, 160): (1, 1, 0, 0), (160, 140): (0, 1, 1, 0), (180, 120): (1, 0, 1, 1), (200, 120):
         (0, 1, 0, 1), (200, 100): (1, 1, 0, 0), (200, 80): (0, 1, 1, 0), (180, 80): (1, 0, 1, 0), (180, 100)
         : (0, 1, 0, 1), (160, 100): (0, 0, 1, 0), (140, 100): (0, 0, 1, 1), (20, 60): (1, 1, 0, 1), (20, 40)
         : (1, 1, 0, 0), (20, 20): (1, 0, 1, 0), (40, 20): (0, 0, 1, 1), (60, 20): (0, 0, 1, 1), (80, 20):
         (0, 0, 1, 1), (100, 20): (0, 0, 1, 1), (120, 20): (0, 0, 1, 1), (140, 20): (0, 0, 1, 1), (160, 20):
         (0, 0, 1, 0), (160, 40): (0, 0, 0, 0), (160, 60): (1, 1, 0, 0), (160, 80): (0, 1, 0, 1), (140, 80):
         (0, 0, 0, 1), (140, 60): (0, 1, 1, 0), (120, 60): (0, 0, 1, 1), (100, 60): (1, 0, 0, 1), (100, 40):
         (0, 1, 1, 0), (80, 40): (0, 0, 1, 0), (80, 60): (1, 1, 0, 0), (80, 80): (0, 1, 0, 1), (200, 40):
         (1, 1, 0, 0), (200, 20): (0, 1, 1, 0), (180, 20): (0, 0, 1, 1), (140, 180): (1, 0, 1, 1), (180, 160)
         : (1, 1, 0, 0), (180, 180): (1, 0, 0, 1), (200, 180): (0, 1, 1, 0), (200, 200): (0, 1, 0, 1),
         (180, 200): (0, 0, 1, 1), (40, 120): (0, 1, 1, 1), (180, 40): (0, 1, 1, 1), (160, 120): (1, 1, 0, 1)
         , (20, 160): (1, 0, 1, 1), (40, 160): (0, 0, 1, 1), (140, 200): (1, 0, 1, 1), (60, 120):
         (1, 0, 1, 1), (20, 200): (1, 0, 1, 1), (200, 160): (1, 1, 0, 1), (200, 140): (0, 1, 1, 0),
         (180, 140): (1, 0, 1, 0), (100, 80): (1, 1, 1, 0), (100, 160): (1, 0, 1, 1), (20, 80): (1, 0, 1, 1),
         (180, 60): (1, 0, 1, 1), (200, 60): (0, 1, 0, 1), (120, 200): (1, 1, 0, 1), (120, 80): (1, 0, 1, 1),
         (60, 40): (1, 0, 1, 1), (120, 40): (1, 0, 1, 1), (140, 40): (0, 0, 1, 1), (40, 40): (1, 1, 1, 0)}
        self.assertEqual(self.algoritmi.get_visited(), labyrinth)
        