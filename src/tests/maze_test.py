import unittest
from optparse import make_option
from maze import Maze

class TestMain(unittest.TestCase):
    def setUp(self):
        self.maze = Maze()

    def test_ohjelma_luo_labyrintin_joka_antaa_tervehdyksen(self):
        self.assertEqual(self.maze.viesti(), "Hello, I'm a maze.")
