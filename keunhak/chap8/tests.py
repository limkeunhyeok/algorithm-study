import unittest
import bino, jumpgame

class Chap8ProbTests(unittest.TestCase):
    def test_bino_case_1(self):
        result = bino.solution(2, 1)
        self.assertEqual(result, 2)
    def test_bino_case_2(self):
        result = bino.solution(4, 2)
        self.assertEqual(result, 6)

    def test_jump_case_1(self):
        result = jumpgame.solution(
            [[2, 5, 1, 6, 1, 4, 1],
            [6, 1, 1, 2, 2, 9, 3],
            [7, 2, 3, 2, 1, 3, 1],
            [1, 1, 3, 1, 7, 1, 2],
            [4, 1, 2, 3, 4, 1, 2],
            [3, 3, 1, 2, 3, 4, 1],
            [1, 5, 2, 9, 4, 7, 0]])
        self.assertEqual(result, True)
    def test_jump_case_2(self):
        result = jumpgame.solution(
            [[2, 5, 1, 6, 1, 4, 1],
            [6, 1, 1, 2, 2, 9, 3],
            [7, 2, 3, 2, 1, 3, 1],
            [1, 1, 3, 1, 7, 1, 2],
            [4, 1, 2, 3, 4, 1, 3],
            [3, 3, 1, 2, 3, 4, 1],
            [1, 5, 2, 9, 4, 7, 0]])
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
