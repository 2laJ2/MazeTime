import unittest
from unittest.mock import Mock, ANY
from maze import Maze
from mysteerimaze import Mysteerimaze

class TestMysteerimaze(unittest.TestCase):
    def setUp(self):
        maze_mock = Mock()
        maze_mock._x_max = 10
        maze_mock._y_max = 10
        maze_mock._w = 20
        maze_mock._solution = {}
        self.algoritmi = Mysteerimaze(maze_mock, maze_mock._x_max, maze_mock._y_max, maze_mock._w)
        self.algoritmi._maze = maze_mock
        self.algoritmi._x_max = maze_mock._x_max
        self.algoritmi._y_max = maze_mock._y_max
        self.algoritmi._w = maze_mock._w
        self.algoritmi._solution = maze_mock._solution
        self.algoritmi._grid = []
        x, y = 0, 0
        for i in range(1, maze_mock._y_max + 1):
            x = self.algoritmi._w
            y = y + self.algoritmi._w
            for j in range(1, maze_mock._x_max + 1):
                self.algoritmi._grid.append((x,y))
                x = x + self.algoritmi._w
        self.maxDiff = None

    def test_metodi_gt_always_last_toimii_oikein(self):
        stack, x, y = self.algoritmi.gt_always_last({(4,2):(1, 0, 1, 1),(4,4): (0, 1, 1, 1)},4,4) 
        self.assertEqual(stack, {(4,2): (1, 0, 1, 1)})
        self.assertEqual(x+y, 8)

    def test_metodi_gt_always_random_toimii_oikein(self):
        stack, x, y = self.algoritmi.gt_always_random({(1,1):(1, 0, 1, 1),(1,2):(0, 1, 1, 1),(3,1):
        (1, 0, 1, 1),(3,2):(0, 1, 1, 1)},3,2)
        self.assertEqual(stack, {(1,1):(1, 0, 1, 1),(1,2):(0, 1, 1, 1),(3,1):(1, 0, 1, 1)})
        self.assertNotEqual(x+y, 5)

    def test_gt_always_first_toimii_oikein(self):
        stack, x, y = self.algoritmi.gt_always_first({(1,1):(1, 0, 1, 1),(1,2):(0, 1, 1, 1),(3,1):
        (1, 0, 1, 1),(3,2):(0, 1, 1, 1)},3,2)
        self.assertEqual(stack, {(1,1):(1, 0, 1, 1),(1,2):(0, 1, 1, 1),(3,1):(1, 0, 1, 1)})
        self.assertEqual(x+y, 2)
        
    def test_gt_usually_last_occasionally_random_poistaa_ruudun_pinosta(self):
        stack, x, y = self.algoritmi.gt_usually_last_occasionally_random({(1,1):(1, 0, 1, 1),(1,2):(0, 1, 1, 1),(3,1):
        (1, 0, 1, 1),(3,2):(0, 1, 1, 1)},3,2)
        self.assertEqual(stack, {(1,1):(1, 0, 1, 1),(1,2):(0, 1, 1, 1),(3,1):(1, 0, 1, 1)})
        
    def test_gt_random_among_last_ones_toimii_oikein(self):
        pino = {(1,1):(1, 0, 1, 1),(1,2):(0, 0, 1, 1),(1,3):(0, 0, 1, 1),(1,4):(0, 1, 1, 1),
        (5,1):(1, 0, 1, 1),(5,2):(0, 0, 1, 1),(5,3):(0, 0, 1, 1),(5,4):(0, 1, 1, 1)}
        a, b = 5, 4
        stack, x, y = self.algoritmi.gt_random_among_last_ones(pino, a, b)
        self.assertEqual(stack, {(1,1):(1, 0, 1, 1),(1,2):(0, 0, 1, 1),(1,3):(0, 0, 1, 1),(1,4):(0, 1, 1, 1),
        (5,1):(1, 0, 1, 1),(5,2):(0, 0, 1, 1),(5,3):(0, 0, 1, 1)})
        self.assertNotEqual(x+y, 2)
        self.assertNotEqual(x+y, 3)
        self.assertNotEqual(x+y, 9)

    def test_algoritmi_kutsuu_maze_oliota_kun_option_1(self):
        self.algoritmi.carve_mysteerimaze(0, '1')
        self.algoritmi._maze.assert_any_call

    def test_algoritmi_toimii_oikein_kun_option_1(self):
        self.algoritmi.carve_mysteerimaze(0, '1')
        labyrinth = {(20, 20): (1, 1, 1, 0), (20, 40): (1, 1, 0, 0), (20, 60): (1, 0, 0, 1), (40, 60):
         (0, 1, 1, 0), (40, 80): (1, 1, 0, 0), (40, 100): (0, 1, 0, 1), (20, 100): (1, 0, 0, 0), (20, 80):
         (1, 1, 1, 0), (20, 120): (1, 1, 0, 0), (20, 140): (1, 1, 0, 0), (20, 160): (1, 0, 0, 1), (40, 160):
         (0, 1, 0, 1), (40, 140): (1, 0, 1, 0), (60, 140): (0, 1, 1, 0), (60, 160): (1, 0, 0, 1), (80, 160):
         (0, 0, 1, 1), (100, 160): (0, 1, 0, 1), (100, 140): (0, 1, 1, 0), (80, 140): (1, 0, 0, 1), (80, 120)
         : (0, 1, 1, 0), (60, 120): (0, 0, 0, 1), (40, 120): (1, 0, 1, 1), (60, 100): (1, 1, 0, 0), (60, 80):
         (1, 1, 0, 0), (60, 60): (1, 0, 1, 0), (80, 60): (0, 1, 1, 0), (80, 80): (1, 1, 0, 0), (80, 100):
         (1, 0, 0, 1), (100, 100): (0, 1, 0, 1), (100, 80): (1, 0, 1, 0), (120, 80): (0, 1, 0, 1), (120, 60):
         (0, 1, 1, 0), (100, 60): (1, 0, 0, 1), (100, 40): (1, 1, 0, 0), (100, 20): (0, 0, 1, 0), (80, 20):
         (0, 0, 1, 1), (60, 20): (0, 0, 1, 1), (40, 20): (1, 0, 1, 0), (40, 40): (1, 0, 0, 1), (60, 40):
         (0, 0, 1, 1), (80, 40): (0, 1, 1, 1), (120, 20): (0, 1, 1, 0), (120, 40): (1, 0, 0, 1), (140, 40):
         (0, 1, 0, 1), (140, 20): (1, 0, 1, 0), (160, 20): (0, 0, 1, 1), (180, 20): (0, 0, 1, 1), (200, 20):
         (0, 1, 1, 0), (200, 40): (0, 1, 0, 1), (180, 40): (0, 0, 1, 1), (160, 40): (1, 0, 1, 0), (160, 60):
         (1, 0, 0, 1), (180, 60): (0, 0, 1, 1), (200, 60): (0, 1, 1, 0), (200, 80): (1, 1, 0, 0), (200, 100):
         (0, 1, 0, 1), (180, 100): (1, 0, 1, 0), (180, 120): (1, 1, 0, 0), (180, 140): (0, 1, 0, 1),
         (160, 140): (1, 0, 0, 1), (160, 120): (0, 1, 1, 0), (140, 120): (1, 0, 0, 1), (140, 100):
         (0, 1, 0, 0), (120, 100): (1, 0, 1, 0), (120, 120): (0, 1, 0, 0), (120, 140): (1, 1, 0, 0),
         (120, 160): (1, 0, 0, 1), (140, 160): (0, 1, 0, 0), (140, 140): (1, 1, 1, 0), (140, 180):
         (0, 1, 0, 1), (120, 180): (0, 0, 1, 1), (100, 180): (1, 0, 1, 0), (100, 200): (0, 0, 0, 1),
         (120, 200): (0, 0, 1, 1), (140, 200): (0, 0, 1, 1), (160, 200): (0, 0, 1, 1), (180, 200):
         (0, 1, 0, 1), (180, 180): (0, 1, 1, 0), (160, 180): (1, 0, 0, 1), (160, 160): (1, 0, 1, 0),
         (180, 160): (0, 0, 1, 1), (200, 160): (0, 1, 0, 0), (200, 180): (1, 1, 0, 0), (200, 200):
         (1, 1, 0, 1), (200, 140): (1, 1, 0, 0), (200, 120): (1, 1, 1, 0), (80, 200): (0, 0, 1, 1), (60, 200)
         : (0, 0, 1, 1), (40, 200): (1, 0, 0, 1), (40, 180): (0, 0, 1, 0), (20, 180): (1, 0, 1, 0), (20, 200)
         : (1, 1, 0, 1), (60, 180): (0, 0, 1, 1), (80, 180): (0, 1, 1, 1), (100, 120): (1, 0, 1, 1),
         (140, 80): (1, 0, 0, 0), (160, 80): (0, 0, 1, 0), (160, 100): (1, 1, 0, 1), (180, 80): (0, 1, 1, 1),
         (140, 60): (1, 1, 1, 0)}
        self.assertEqual(self.algoritmi.get_visited(), labyrinth)
                
    def test_algoritmi_toimii_oikein_kun_option_2(self):
        self.algoritmi.carve_mysteerimaze(0, '2')
        labyrinth = {(20, 20): (1, 1, 1, 0), (20, 40): (1, 1, 0, 0), (20, 60): (1, 0, 0, 1), (40, 60):
         (0, 0, 0, 0), (40, 80): (1, 1, 0, 0), (40, 100): (0, 1, 0, 1), (20, 100): (1, 0, 0, 1), (20, 80):
         (1, 1, 1, 0), (40, 40): (1, 1, 0, 0), (40, 20): (1, 0, 1, 0), (60, 20): (0, 0, 1, 0), (80, 20):
         (0, 1, 1, 0), (80, 40): (1, 0, 0, 1), (100, 40): (0, 0, 1, 1), (120, 40): (0, 0, 0, 1), (120, 20):
         (0, 1, 1, 0), (100, 20): (1, 0, 1, 1), (60, 60): (0, 0, 1, 1), (80, 60): (0, 0, 1, 1), (100, 60):
         (0, 1, 1, 0), (100, 80): (0, 1, 0, 1), (80, 80): (0, 0, 1, 0), (60, 80): (1, 0, 1, 0), (60, 100):
         (1, 1, 0, 0), (60, 120): (0, 1, 0, 1), (40, 120): (0, 0, 1, 1), (20, 120): (1, 0, 1, 0), (20, 140):
         (1, 1, 0, 0), (20, 160): (1, 1, 0, 0), (20, 180): (1, 0, 0, 1), (40, 180): (0, 1, 0, 1), (40, 160):
         (1, 0, 1, 0), (60, 160): (0, 0, 1, 0), (80, 160): (0, 1, 0, 1), (80, 140): (0, 1, 0, 0), (60, 140):
         (0, 0, 1, 1), (40, 140): (1, 0, 1, 1), (60, 180): (1, 0, 0, 0), (80, 180): (0, 1, 1, 0), (80, 200):
         (1, 0, 0, 1), (100, 200): (0, 0, 0, 1), (120, 200): (0, 0, 1, 1), (140, 200): (0, 0, 1, 1),
         (160, 200): (0, 0, 1, 1), (180, 200): (0, 1, 0, 1), (180, 180): (1, 0, 1, 0), (200, 180):
         (0, 1, 1, 0), (200, 200): (1, 1, 0, 1), (80, 100): (1, 0, 0, 1), (100, 100): (0, 1, 1, 0),
         (100, 120): (1, 1, 0, 0), (100, 140): (1, 1, 0, 0), (100, 160): (1, 0, 0, 1), (120, 160):
         (0, 1, 0, 1), (120, 140): (1, 1, 0, 0), (120, 120): (1, 0, 1, 0), (140, 120): (0, 1, 0, 1),
         (140, 100): (1, 1, 0, 0), (140, 80): (1, 1, 0, 0), (140, 60): (0, 1, 1, 0), (120, 60): (1, 0, 1, 0),
         (120, 80): (1, 1, 0, 0), (120, 100): (1, 1, 0, 1), (100, 180): (1, 0, 1, 0), (120, 180):
         (0, 0, 1, 1), (140, 180): (0, 1, 0, 1), (140, 160): (1, 0, 1, 0), (160, 160): (0, 0, 1, 0),
         (180, 160): (0, 0, 1, 1), (200, 160): (0, 1, 0, 1), (200, 140): (1, 1, 0, 0), (200, 120):
         (1, 1, 0, 0), (200, 100): (0, 1, 0, 0), (180, 100): (0, 0, 1, 1), (160, 100): (1, 0, 1, 0),
         (160, 120): (1, 0, 0, 1), (180, 120): (0, 1, 1, 0), (180, 140): (0, 1, 0, 1), (160, 140):
         (0, 0, 1, 1), (140, 140): (1, 0, 1, 1), (60, 200): (0, 1, 0, 1), (40, 200): (0, 0, 1, 1), (20, 200):
         (1, 0, 1, 1), (60, 40): (1, 1, 0, 1), (140, 40): (0, 1, 0, 1), (140, 20): (1, 0, 1, 0), (160, 20):
         (0, 0, 1, 1), (180, 20): (0, 0, 1, 1), (200, 20): (0, 1, 1, 0), (200, 40): (0, 1, 0, 1), (180, 40):
         (0, 0, 1, 1), (160, 40): (1, 0, 1, 0), (160, 60): (1, 0, 0, 1), (180, 60): (0, 1, 1, 0), (180, 80):
         (0, 1, 0, 1), (160, 80): (1, 0, 1, 1), (160, 180): (1, 1, 0, 1), (200, 80): (1, 1, 0, 0), (200, 60):
         (1, 1, 1, 0), (80, 120): (1, 1, 1, 0)}
        self.assertEqual(self.algoritmi.get_visited(), labyrinth)

    def test_algoritmi_toimii_oikein_kun_option_3(self):
        self.algoritmi.carve_mysteerimaze(0, '3')
        labyrinth = {(20, 20): (1, 0, 1, 0), (20, 40): (1, 1, 0, 0), (20, 60): (1, 0, 0, 1), (40, 60):
         (0, 0, 1, 0), (40, 80): (1, 1, 0, 0), (40, 100): (0, 0, 0, 1), (20, 100): (1, 0, 0, 1), (20, 80):
         (1, 1, 1, 0), (40, 20): (0, 1, 1, 0), (40, 40): (1, 0, 0, 1), (60, 40): (0, 0, 0, 1), (60, 20):
         (1, 0, 1, 0), (80, 20): (0, 0, 1, 1), (100, 20): (0, 1, 1, 0), (100, 40): (1, 0, 0, 1), (120, 40):
         (0, 0, 1, 0), (140, 40): (0, 1, 0, 1), (140, 20): (0, 1, 1, 0), (120, 20): (1, 0, 1, 1), (60, 60):
         (0, 1, 1, 0), (60, 80): (1, 0, 0, 1), (80, 80): (0, 1, 0, 1), (80, 60): (1, 0, 1, 0), (100, 60):
         (0, 1, 1, 0), (100, 80): (1, 1, 0, 0), (100, 100): (1, 1, 0, 0), (100, 120): (1, 0, 0, 1),
         (120, 120): (0, 0, 1, 0), (120, 140): (0, 0, 0, 1), (100, 140): (1, 0, 1, 0), (100, 160):
         (1, 1, 0, 0), (100, 180): (1, 1, 0, 0), (100, 200): (1, 0, 0, 1), (120, 200): (0, 0, 0, 1),
         (120, 180): (1, 0, 0, 0), (120, 160): (1, 0, 1, 0), (140, 160): (0, 0, 1, 1), (160, 160):
         (0, 1, 0, 1), (160, 140): (1, 0, 1, 0), (180, 140): (0, 0, 1, 1), (200, 140): (0, 1, 0, 1),
         (200, 120): (0, 1, 0, 0), (180, 120): (1, 0, 0, 1), (180, 100): (0, 1, 0, 0), (160, 100):
         (0, 0, 1, 1), (140, 100): (1, 0, 0, 1), (140, 80): (0, 1, 1, 0), (120, 80): (1, 0, 1, 0), (120, 100)
         : (1, 1, 0, 1), (60, 100): (0, 0, 1, 1), (80, 100): (0, 1, 1, 0), (80, 120): (0, 1, 0, 1), (60, 120)
         : (1, 0, 1, 0), (60, 140): (1, 0, 0, 1), (80, 140): (0, 1, 1, 0), (80, 160): (1, 1, 0, 0), (80, 180)
         : (1, 1, 0, 0), (80, 200): (0, 1, 0, 1), (60, 200): (1, 0, 0, 1), (60, 180): (1, 1, 0, 0), (60, 160)
         : (0, 1, 1, 0), (40, 160): (1, 0, 0, 1), (40, 140): (1, 1, 0, 0), (40, 120): (0, 1, 1, 0), (20, 120)
         : (1, 0, 1, 0), (20, 140): (1, 1, 0, 0), (20, 160): (1, 1, 0, 0), (20, 180): (1, 1, 0, 0), (20, 200)
         : (1, 0, 0, 1), (40, 200): (0, 1, 0, 1), (40, 180): (1, 1, 1, 0), (80, 40): (0, 1, 1, 1), (120, 60):
         (1, 0, 0, 1), (140, 60): (0, 0, 1, 1), (160, 60): (0, 0, 1, 1), (180, 60): (0, 1, 0, 1), (180, 40):
         (1, 1, 0, 0), (180, 20): (0, 1, 1, 0), (160, 20): (1, 0, 1, 0), (160, 40): (1, 1, 0, 1), (140, 120):
         (0, 0, 1, 1), (160, 120): (0, 1, 1, 1), (140, 140): (0, 1, 1, 1), (140, 200): (0, 0, 1, 1),
         (160, 200): (0, 0, 1, 1), (180, 200): (0, 1, 0, 1), (180, 180): (1, 1, 0, 0), (180, 160):
         (1, 0, 1, 0), (200, 160): (0, 1, 1, 0), (200, 180): (1, 1, 0, 0), (200, 200): (1, 1, 0, 1),
         (140, 180): (0, 0, 1, 1), (160, 180): (0, 1, 1, 1), (200, 100): (1, 1, 0, 0), (200, 80):
         (1, 1, 0, 0), (200, 60): (1, 1, 0, 0), (200, 40): (1, 1, 0, 0), (200, 20): (1, 1, 1, 0), (180, 80):
         (0, 1, 1, 0), (160, 80): (1, 0, 1, 1)}
        self.assertEqual(self.algoritmi.get_visited(), labyrinth)

    def test_algoritmi_toimii_oikein_kun_option_4(self):
        self.algoritmi.carve_mysteerimaze(0, '4')
        labyrinth = {(20, 20): (1, 1, 1, 0), (20, 40): (1, 1, 0, 0), (20, 60): (1, 0, 0, 1), (40, 60):
         (0, 1, 1, 0), (40, 80): (1, 1, 0, 0), (40, 100): (0, 1, 0, 1), (20, 100): (1, 0, 0, 0), (20, 80):
         (1, 1, 1, 0), (20, 120): (1, 1, 0, 0), (20, 140): (1, 0, 0, 1), (40, 140): (0, 1, 0, 1), (40, 120):
         (1, 0, 1, 0), (60, 120): (0, 1, 1, 0), (60, 140): (1, 0, 0, 1), (80, 140): (0, 0, 1, 1), (100, 140):
         (0, 1, 0, 1), (100, 120): (0, 1, 1, 0), (80, 120): (1, 0, 0, 1), (80, 100): (0, 1, 1, 0), (60, 100):
         (1, 0, 0, 1), (60, 80): (1, 0, 1, 0), (80, 80): (0, 1, 0, 1), (80, 60): (0, 1, 1, 0), (60, 60):
         (1, 0, 0, 1), (60, 40): (0, 1, 1, 0), (40, 40): (1, 0, 0, 1), (40, 20): (1, 0, 1, 0), (60, 20):
         (0, 0, 1, 1), (80, 20): (0, 1, 1, 0), (80, 40): (1, 0, 0, 1), (100, 40): (0, 1, 0, 1), (100, 20):
         (1, 0, 1, 0), (120, 20): (0, 0, 1, 1), (140, 20): (0, 0, 1, 1), (160, 20): (0, 0, 1, 1), (180, 20):
         (0, 1, 1, 0), (180, 40): (1, 1, 0, 0), (180, 60): (1, 1, 0, 0), (180, 80): (1, 1, 0, 0), (180, 100):
         (0, 0, 0, 1), (200, 100): (0, 1, 0, 0), (200, 80): (1, 1, 0, 0), (200, 60): (1, 1, 0, 0), (200, 40):
         (1, 1, 0, 0), (200, 20): (1, 1, 1, 0), (200, 120): (0, 1, 0, 1), (180, 120): (0, 0, 1, 1),
         (160, 120): (1, 0, 1, 0), (160, 140): (1, 1, 0, 0), (160, 160): (0, 1, 0, 1), (140, 160):
         (0, 0, 1, 1), (120, 160): (1, 0, 1, 0), (120, 180): (1, 0, 0, 0), (120, 200): (0, 1, 0, 1),
         (100, 200): (0, 0, 1, 1), (80, 200): (0, 0, 0, 1), (80, 180): (1, 1, 0, 0), (80, 160): (1, 0, 1, 0),
         (100, 160): (0, 1, 1, 0), (100, 180): (1, 1, 0, 1), (160, 100): (1, 0, 0, 1), (160, 80):
         (0, 1, 1, 0), (140, 80): (1, 0, 1, 0), (140, 100): (0, 1, 0, 1), (120, 100): (0, 0, 1, 0),
         (100, 100): (1, 0, 0, 1), (100, 80): (1, 0, 1, 0), (120, 80): (0, 1, 0, 1), (120, 60): (0, 0, 1, 0),
         (100, 60): (1, 0, 1, 1), (140, 60): (0, 0, 1, 1), (160, 60): (0, 1, 0, 1), (160, 40): (0, 1, 1, 0),
         (140, 40): (0, 0, 1, 1), (120, 40): (1, 0, 1, 1), (120, 120): (1, 0, 0, 1), (140, 120): (0, 1, 1, 0)
         , (140, 140): (0, 1, 0, 1), (120, 140): (1, 0, 1, 1), (140, 180): (0, 0, 1, 1), (160, 180):
         (0, 0, 1, 1), (180, 180): (0, 1, 1, 0), (180, 200): (0, 0, 0, 1), (200, 200): (0, 1, 0, 1),
         (200, 180): (1, 1, 0, 0), (200, 160): (0, 1, 1, 0), (180, 160): (1, 0, 0, 1), (180, 140):
         (1, 0, 1, 0), (200, 140): (0, 1, 1, 1), (160, 200): (0, 0, 1, 1), (140, 200): (1, 0, 1, 1),
         (60, 200): (1, 0, 0, 1), (60, 180): (0, 1, 1, 0), (40, 180): (1, 0, 1, 0), (40, 200): (0, 1, 0, 1),
         (20, 200): (1, 0, 0, 1), (20, 180): (1, 1, 0, 0), (20, 160): (1, 0, 1, 0), (40, 160): (0, 0, 1, 1),
         (60, 160): (0, 1, 1, 1)}
        self.assertEqual(self.algoritmi.get_visited(), labyrinth)

    def test_algoritmi_toimii_oikein_kun_option_5(self):
        self.algoritmi.carve_mysteerimaze(0, '5')
        labyrinth = {(20, 20): (1, 1, 1, 0), (20, 40): (1, 1, 0, 0), (20, 60): (1, 0, 0, 1), (40, 60):
         (0, 1, 1, 0), (40, 80): (1, 1, 0, 0), (40, 100): (0, 1, 0, 0), (20, 100): (1, 0, 0, 1), (20, 80):
         (1, 1, 1, 0), (40, 120): (0, 1, 0, 1), (20, 120): (1, 0, 1, 0), (20, 140): (1, 0, 0, 1), (40, 140):
         (0, 1, 1, 0), (40, 160): (1, 0, 0, 1), (60, 160): (0, 0, 1, 1), (80, 160): (0, 1, 0, 1), (80, 140):
         (0, 1, 1, 0), (60, 140): (1, 0, 0, 1), (60, 120): (1, 1, 0, 0), (60, 100): (1, 0, 1, 0), (80, 100):
         (0, 1, 0, 1), (80, 80): (1, 0, 1, 0), (100, 80): (0, 1, 0, 1), (100, 60): (0, 1, 1, 0), (80, 60):
         (0, 0, 0, 1), (80, 40): (0, 1, 0, 0), (80, 20): (1, 0, 1, 0), (100, 20): (0, 1, 1, 0), (100, 40):
         (1, 0, 0, 1), (120, 40): (0, 1, 1, 0), (120, 60): (1, 0, 0, 0), (140, 60): (0, 1, 0, 1), (140, 40):
         (1, 1, 0, 0), (140, 20): (0, 1, 1, 0), (120, 20): (1, 0, 1, 1), (60, 40): (1, 0, 0, 1), (60, 20):
         (0, 1, 1, 0), (40, 20): (1, 0, 1, 0), (40, 40): (1, 1, 0, 1), (60, 60): (1, 0, 1, 0), (60, 80):
         (1, 1, 0, 1), (120, 80): (1, 0, 0, 1), (140, 80): (0, 1, 1, 0), (140, 100): (1, 0, 0, 1), (160, 100)
         : (0, 0, 1, 1), (180, 100): (0, 1, 1, 0), (180, 120): (0, 1, 0, 0), (180, 140): (0, 0, 0, 1),
         (160, 140): (0, 0, 1, 1), (140, 140): (1, 0, 1, 0), (140, 160): (1, 1, 0, 0), (140, 180):
         (0, 1, 0, 1), (120, 180): (1, 0, 0, 1), (120, 160): (0, 1, 1, 0), (100, 160): (1, 0, 0, 0),
         (100, 140): (1, 0, 1, 0), (120, 140): (0, 1, 0, 1), (120, 120): (0, 1, 1, 0), (100, 120):
         (0, 0, 0, 1), (80, 120): (1, 0, 1, 1), (160, 120): (0, 0, 1, 1), (140, 120): (1, 0, 1, 1),
         (200, 140): (0, 1, 0, 0), (200, 160): (0, 1, 0, 1), (180, 160): (0, 0, 1, 1), (160, 160):
         (1, 0, 1, 0), (160, 180): (1, 1, 0, 0), (160, 200): (1, 0, 0, 1), (180, 200): (0, 0, 1, 1),
         (200, 200): (0, 1, 0, 1), (200, 180): (0, 1, 1, 0), (180, 180): (1, 0, 1, 1), (100, 180):
         (0, 1, 0, 0), (100, 200): (0, 0, 0, 1), (80, 200): (0, 0, 1, 1), (60, 200): (0, 0, 1, 1), (40, 200):
         (0, 0, 0, 1), (40, 180): (0, 1, 1, 0), (20, 180): (1, 0, 0, 1), (20, 160): (1, 1, 1, 0), (100, 100):
         (1, 0, 1, 0), (120, 100): (0, 1, 1, 1), (200, 120): (1, 1, 0, 0), (200, 100): (1, 1, 0, 0),
         (200, 80): (0, 1, 1, 0), (180, 80): (0, 0, 1, 1), (160, 80): (1, 0, 0, 1), (160, 60): (1, 0, 1, 0),
         (180, 60): (0, 0, 1, 1), (200, 60): (0, 1, 0, 1), (200, 40): (0, 1, 0, 0), (180, 40): (1, 0, 0, 1),
         (180, 20): (0, 1, 1, 0), (160, 20): (1, 0, 1, 0), (160, 40): (1, 1, 0, 1), (80, 180): (0, 0, 1, 1),
         (60, 180): (1, 0, 1, 1), (120, 200): (0, 0, 1, 1), (140, 200): (0, 1, 1, 1), (20, 200): (1, 0, 1, 1)
         , (200, 20): (1, 1, 1, 0)}
        self.assertEqual(self.algoritmi.get_visited(), labyrinth)
