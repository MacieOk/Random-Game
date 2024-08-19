# test_asymptotic_analyzer.py
import unittest
from random_games.random_games.asymptotic_analyzer import AsymptoticAnalyzer

class TestAsymptoticAnalyzer(unittest.TestCase):

    def test_analyze_growth(self):
        analyzer = AsymptoticAnalyzer()
        growth_rate = analyzer.analyze_growth([1, 2, 4, 8, 16])
        self.assertEqual(growth_rate, 'exponential')

    def test_analyze_growth_linear(self):
        analyzer = AsymptoticAnalyzer()
        growth_rate = analyzer.analyze_growth([1, 2, 3, 4, 5])
        self.assertEqual(growth_rate, 'linear')

    def test_empty_input(self):
        analyzer = AsymptoticAnalyzer()
        growth_rate = analyzer.analyze_growth([])
        self.assertEqual(growth_rate, 'undefined')

if __name__ == "__main__":
    unittest.main()
