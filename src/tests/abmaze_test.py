import unittest
from unittest.mock import Mock, ANY
from maze import Maze
from abmaze import Abmaze

class TestAbmaze(unittest.TestCase):
    def setUp(self):
        maze_mock = Mock()#wraps=Maze())
        w = 20
        self.algoritmi = Abmaze(maze_mock, w)
        self.algoritmi._grid = []
        x, y = 0, 0
        for i in range(1, w + 1):
            x = w
            y = y + w
            for j in range(1, w + 1):
                self.algoritmi._grid.append((x,y))
                x = x + w

    def test_algoritmi_kay_kaikissa_ruuduissa(self):
        self.algoritmi.carve_AB_maze(0)
        self.algoritmi._maze.assert_any_call