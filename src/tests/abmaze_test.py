import unittest
from unittest.mock import Mock, ANY
from maze import Maze
from abmaze import Abmaze

class TestAbmaze(unittest.TestCase):
    def setUp(self):
        maze_mock = Mock()
        maze_mock._x_max = 10
        maze_mock._y_max = 10
        maze_mock._w = 20
        self.algoritmi = Abmaze(maze_mock, maze_mock._x_max, maze_mock._y_max_, maze_mock._w)
        self.algoritmi._maze = maze_mock
        self.algoritmi._x_max = maze_mock._x_max
        self.algoritmi._y_max = maze_mock._y_max
        self.algoritmi._w = maze_mock._w
        self.algoritmi._grid = []
        x, y = 0, 0
        for i in range(1, maze_mock._y_max + 1):
            x = self.algoritmi._w
            y = y + self.algoritmi._w
            for j in range(1, maze_mock._x_max + 1):
                self.algoritmi._grid.append((x,y))
                x = x + self.algoritmi._w
        self.maxDiff = None

    def test_algoritmi_kutsuu_maze_oliota(self):
        self.algoritmi.carve_AB_maze(0)
        self.algoritmi._maze.assert_any_call

    def test_algoritmi_toimii_oikein(self):
        self.algoritmi.carve_AB_maze(0)
        labyrinth = [(120, 120), (140, 120), (140, 140), (140, 100), (100, 120), (100, 140), (80, 140),
        (100, 160), (80, 160), (80, 180), (100, 180), (120, 180), (120, 200), (100, 200), (80, 200),
        (60, 180), (60, 160), (60, 140), (120, 160), (120, 140), (140, 160), (140, 180), (140, 200),
        (160, 200), (180, 200), (180, 180), (200, 200), (200, 180), (200, 160), (200, 140), (180, 140),
        (160, 140), (160, 120), (160, 100), (180, 120), (200, 120), (180, 160), (160, 160), (160, 180),
        (40, 180), (40, 160), (40, 140), (40, 120), (60, 120), (60, 100), (60, 80), (80, 80), (60, 60),
        (80, 60), (60, 40), (80, 40), (100, 40), (100, 20), (80, 20), (60, 20), (40, 20), (120, 20),
        (120, 40), (140, 40), (160, 40), (140, 60), (140, 80), (120, 80), (180, 40), (180, 60), (200, 40),
        (200, 60), (180, 80), (200, 80), (180, 100), (200, 100), (160, 80), (160, 60), (140, 20), (120, 60),
        (120, 100), (100, 100), (180, 20), (160, 20), (60, 200), (40, 200), (80, 120), (80, 100), (40, 60),
        (40, 40), (20, 60), (20, 80), (20, 100), (20, 40), (200, 20), (100, 60), (20, 20), (100, 80),
        (20, 140), (20, 120), (40, 100), (20, 160), (20, 180), (20, 200), (40, 80)]
        self.assertEqual(self.algoritmi.get_visited(), labyrinth)
