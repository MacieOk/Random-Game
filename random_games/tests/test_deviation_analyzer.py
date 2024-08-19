# test_deviation_analyzer.py
import unittest
from random_games.random_games.deviation_analyzer import DeviationAnalyzer

class TestDeviationAnalyzer(unittest.TestCase):

    def test_calculate_standard_deviation(self):
        analyzer = DeviationAnalyzer()
        deviation = analyzer.calculate_standard_deviation([1, 2, 3, 4, 5])
        self.assertAlmostEqual(deviation, 1.58, places=2)

    def test_empty_input(self):
        analyzer = DeviationAnalyzer()
        deviation = analyzer.calculate_standard_deviation([])
        self.assertEqual(deviation, 0)

if __name__ == "__main__":
    unittest.main()
