import unittest
from optparse import make_option
from maze import Maze

class TestMain(unittest.TestCase):
    def setUp(self):
        self.maze = Maze()

    def test_ohjelma_luo_labyrintin_joka_antaa_tervehdyksen(self):
        self.assertEqual(self.maze.viesti(), "Hello, I'm a maze.")

    def test_labyrintti_palauttaa_kaytetyn_algoritmimetodin(self):
        self.assertEqual(self.maze.algo1(), "That is a beginner algorithm.")

    def test_labyrintin_luomisessa_kaytetaan_haluttua_metodia(self):
        self.assertEqual(self.maze.algo2(), "That is a bit more complex stuff.")
