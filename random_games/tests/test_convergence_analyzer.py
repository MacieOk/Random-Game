# test_convergence_analyzer.py
import unittest
from random_games.random_games.convergence_analyzer import ConvergenceAnalyzer

class TestConvergenceAnalyzer(unittest.TestCase):

    def test_analyze_convergence(self):
        analyzer = ConvergenceAnalyzer()
        result = analyzer.analyze_convergence([1, 0.5, 0.25, 0.125])
        self.assertTrue(result)

    def test_non_convergent_sequence(self):
        analyzer = ConvergenceAnalyzer()
        result = analyzer.analyze_convergence([1, 2, 3, 4, 5])
        self.assertFalse(result)

    def test_empty_input(self):
        analyzer = ConvergenceAnalyzer()
        result = analyzer.analyze_convergence([])
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
