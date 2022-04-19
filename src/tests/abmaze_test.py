import unittest
from unittest.mock import Mock, ANY
from maze import Maze
from abmaze import Abmaze

class TestAbmaze(unittest.TestCase):
    def setUp(self):
        maze_mock = Mock()
        maze_mock._x_max = 20
        maze_mock._y_max = 20
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

    def test_algoritmi_kutsuu_maze_oliota(self):
        self.algoritmi.carve_AB_maze(0)
        self.algoritmi._maze.assert_any_call

    def test_algoritmi_kay_kaikissa_ruuduissa(self):
        self.algoritmi.carve_AB_maze(0)
        self.assertEqual(len(self.algoritmi._visited), self.algoritmi._x_max*self.algoritmi._y_max)