# test_game_logic.py

import unittest
from random_games.random_games.game_logic import JeuDeTacquin

class TestJeuDeTacquin(unittest.TestCase):

    def test_find_path(self):
        tableau = [
            [1, 2, 3],
            [2, 5, 6],
            [3, 6, 7]
        ]
        jeu = JeuDeTacquin()
        path = jeu.find_path(tableau)
        expected_path = [(0, 0), (1, 0), (2, 1), (2, 2)]
        self.assertEqual(path, expected_path)

    def test_empty_tableau(self):
        tableau = []
        jeu = JeuDeTacquin()
        path = jeu.find_path(tableau)
        self.assertEqual(path, [])

if __name__ == "__main__":
    unittest.main()
