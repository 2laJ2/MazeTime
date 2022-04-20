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
        self.algoritmi._visited = []
        x, y = 0, 0
        for i in range(1, maze_mock._y_max + 1):
            x = self.algoritmi._w
            y = y + self.algoritmi._w
            for j in range(1, maze_mock._x_max + 1):
                self.algoritmi._grid.append((x,y))
                x = x + self.algoritmi._w
        self.maxDiff = None
    
    def test_metodi_reverse_stack_builder_toimii_oikein(self):
        self.assertEqual(self.algoritmi.reverse_stack_builder(2,2), [(20, 20), (20, 40), (40, 20), (40, 40)])

    def test_metodi_wilson_path_palauttaa_tyhjan_polun(self):
        self.assertEqual(self.algoritmi.wilson_path([],3,3), [])

    def test_algoritmi_kutsuu_maze_oliota(self):
        self.algoritmi.carve_Wilson_maze(0)
        self.algoritmi._maze.assert_any_call

    def test_algoritmi_kay_kaikissa_ruuduissa(self):
        self.algoritmi._not_visited = [(10,10),(10,20),(20,10),(20,20)]
        self.algoritmi.carve_Wilson_maze(0)
        self.assertEqual(len(self.algoritmi._not_visited), 0)

    def test_algoritmi_toimii_oikein(self):
        self.algoritmi.carve_Wilson_maze(0)
        labyrinth = [(120, 120), (140, 120), (140, 140), (140, 160), (120, 160), (120, 180), (100, 180),
        (100, 200), (80, 200), (60, 200), (40, 200), (40, 180), (60, 180), (80, 180), (80, 160), (80, 140),
        (80, 120), (80, 100), (100, 100), (100, 120), (100, 140), (120, 140), (60, 160), (60, 180), (20, 180)
        , (40, 180), (60, 100), (40, 100), (20, 100), (20, 120), (20, 140), (40, 140), (60, 140), (60, 160),
        (40, 80), (40, 60), (60, 60), (60, 80), (60, 100), (120, 100), (120, 120), (160, 200), (160, 180),
        (160, 160), (160, 140), (140, 140), (180, 120), (200, 120), (200, 100), (200, 80), (180, 80),
        (180, 100), (160, 100), (140, 100), (120, 100), (20, 60), (20, 40), (20, 20), (40, 20), (60, 20),
        (80, 20), (100, 20), (120, 20), (140, 20), (160, 20), (160, 40), (160, 60), (160, 80), (140, 80),
        (140, 60), (120, 60), (100, 60), (100, 40), (80, 40), (80, 60), (80, 80), (60, 80), (200, 40),
        (200, 20), (180, 20), (160, 20), (140, 180), (160, 180), (180, 160), (180, 180), (200, 180),
        (200, 200), (180, 200), (160, 200), (40, 120), (20, 120), (180, 40), (160, 40), (160, 120),
        (160, 100), (20, 160), (40, 160), (60, 160), (140, 200), (160, 200), (60, 120), (80, 120), (20, 200),
        (40, 200), (200, 160), (200, 140), (180, 140), (180, 160), (100, 80), (100, 100), (100, 160),
        (120, 160), (20, 80), (40, 80), (180, 60), (200, 60), (200, 40), (120, 200), (120, 180), (120, 80),
        (140, 80), (60, 40), (80, 40), (120, 40), (140, 40), (160, 40), (40, 40), (40, 60)]
        self.assertEqual(self.algoritmi.get_visited(), labyrinth)
        