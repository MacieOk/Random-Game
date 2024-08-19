# test_scaling_limit_analyzer.py
import unittest
from random_games.random_games.scaling_limit_analyzer import ScalingLimitAnalyzer

class TestScalingLimitAnalyzer(unittest.TestCase):

    def test_analyze_scaling_limit(self):
        analyzer = ScalingLimitAnalyzer()
        limit = analyzer.analyze_scaling_limit([1, 10, 100, 1000])
        self.assertEqual(limit, 10)

    def test_empty_input(self):
        analyzer = ScalingLimitAnalyzer()
        limit = analyzer.analyze_scaling_limit([])
        self.assertEqual(limit, 0)

if __name__ == "__main__":
    unittest.main()
