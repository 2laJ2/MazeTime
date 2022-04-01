import unittest
from maze import Maze

class TestMain(unittest.TestCase):
    def setUp(self):
        self.maze = Maze()# käynnistää ja ajaa koko ohjelman, tarkoituksena olisi testata yksittäisten metodien toimivuus
        # pass

    def test_metodi_wilson_path(self):
        self.assertEqual(self.maze.wilson_path([],3,3), [])

    def test_metodi_reverse_stack_builder(self):
        self.assertEqual(self.maze.reverse_stack_builder(2,2), [(20, 20), (20, 40), (40, 20), (40, 40)])

    def test_ohjelma_luo_labyrintin_Aldous_Broderin_algoritmilla(self):
        pass

    def test_ohjelma_luo_labyrintin_Wilsonin_algoritmilla(self):
        pass