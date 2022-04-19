import unittest
from unittest.mock import Mock, ANY
from maze import Maze
from mysteerimaze import Mysteerimaze

class TestAbmaze(unittest.TestCase):
    def setUp(self):
        maze_mock = Mock()
        maze_mock._x_max = 20
        maze_mock._y_max = 20
        w = 20
        self.algoritmi = Mysteerimaze(maze_mock, maze_mock._x_max, maze_mock._y_max, w, {})

    def test_metodi_gt_always_last_toimii_oikein(self):
        stack, x, y = self.algoritmi.gt_always_last([(4,2),(4,4)],4,4) 
        self.assertEqual(stack, [(4,2)])
        self.assertEqual(x+y, 8)

    def test_metodi_gt_always_random_toimii_oikein(self):
        stack, x, y = self.algoritmi.gt_always_random([(1,1),(1,2),(3,1),(3,2)],3,2)
        self.assertEqual(stack, [(1,1),(1,2),(3,1)])
        self.assertNotEqual(x+y, 5)

    def test_gt_always_first_toimii_oikein(self):
        stack, x, y = self.algoritmi.gt_always_first([(1,1),(1,2),(3,1),(3,2)],3,2)
        self.assertEqual(stack, [(1,1),(1,2),(3,1)])
        self.assertEqual(x+y, 2)
        
    def test_gt_usually_last_occasionally_random_poistaa_ruudun_pinosta(self):
        stack, x, y = self.algoritmi.gt_usually_last_occasionally_random([(1,1),(1,2),(3,1),(3,2)],3,2)
        self.assertEqual(stack, [(1,1),(1,2),(3,1)])
        
    def test_gt_random_among_last_ones_toimii_oikein(self):
        pino = [(1,1),(1,2),(1,3),(1,4),(5,1),(5,2),(5,3),(5,4)]
        a, b = 5, 4
        stack, x, y = self.algoritmi.gt_random_among_last_ones(pino, a, b)
        self.assertEqual(stack, [(1,1),(1,2),(1,3),(1,4),(5,1),(5,2),(5,3)])
        self.assertNotEqual(x+y, 2)
        self.assertNotEqual(x+y, 3)
        self.assertNotEqual(x+y, 9)