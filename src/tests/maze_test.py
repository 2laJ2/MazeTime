import unittest
from optparse import make_option
from maze import Maze


class TestMain(unittest.TestCase):
    def setUp(self):
        self.maze = Maze(1)

    def test_ohjelma_luo_labyrintin_joka_antaa_tervehdyksen(self):
        self.assertEqual(self.maze.viesti(), "Hello, I'm a maze.")

    def test_labyrintti_palauttaa_oikean_nimen(self):
        self.assertEqual(self.maze.get_nimi(), 1)
        