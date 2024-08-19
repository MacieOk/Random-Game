# test_tableau_manager.py

import unittest
import numpy as np
from random_games.random_games.tableau_manager import TableauManager

class TestTableauManager(unittest.TestCase):

    def test_insertion_tableau(self):
        random_numbers = np.array([3, 1, 4, 1, 5])
        manager = TableauManager(random_numbers)
        tableau = manager.insertion_tableau()
        expected_tableau = [[1, 4], [3, 5], [1]]
        self.assertEqual(tableau, expected_tableau)

    def test_recording_tableau(self):
        random_numbers = np.array([3, 1, 4, 1, 5])
        manager = TableauManager(random_numbers)
        tableau = manager.recording_tableau()
        expected_tableau = [[1, 3], [2, 5], [4]]
        self.assertEqual(tableau, expected_tableau)

    def test_empty_insertion_tableau(self):
        random_numbers = np.array([])
        manager = TableauManager(random_numbers)
        tableau = manager.insertion_tableau()
        self.assertEqual(tableau, [])

if __name__ == "__main__":
    unittest.main()
