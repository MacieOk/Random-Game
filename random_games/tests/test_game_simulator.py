# test_game_simulator.py
import unittest
from random_games.random_games.game_simulator import GameSimulator

class TestGameSimulator(unittest.TestCase):

    def test_simulate_game(self):
        simulator = GameSimulator()
        result = simulator.simulate_game(10)
        self.assertEqual(len(result), 10)
        self.assertIsInstance(result, list)

    def test_simulate_game_empty(self):
        simulator = GameSimulator()
        result = simulator.simulate_game(0)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
