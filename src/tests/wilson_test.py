import unittest
from unittest.mock import Mock, ANY
from maze import Maze
from wilson import Wilson

class TestAbmaze(unittest.TestCase):
    def setUp(self):
        maze_mock = Mock()
        w = 20
        self.algoritmi = Wilson(maze_mock, w)

    def test_metodi_reverse_stack_builder_toimii_oikein(self):
        self.assertEqual(self.algoritmi.reverse_stack_builder(2,2), [(20, 20), (20, 40), (40, 20), (40, 40)])

    def test_metodi_wilson_path_palauttaa_tyhjan_polun(self):
        self.assertEqual(self.algoritmi.wilson_path([],3,3), [])
