# test_random_list_generator.py
import unittest
from random_games.random_games.random_list_generator import generate_random_list

class TestRandomListGenerator(unittest.TestCase):

    def test_generate_random_list(self):
        result = generate_random_list(5, 1, 10)
        self.assertEqual(len(result), 5)
        for num in result:
            self.assertGreaterEqual(num, 1)
            self.assertLessEqual(num, 10)

    def test_generate_random_list_empty(self):
        result = generate_random_list(0, 1, 10)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
