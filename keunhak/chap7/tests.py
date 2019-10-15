import unittest
import prob1

class Chap7ProbTests(unittest.TestCase):
    def test_prob1_case_1(self):
        result = prob1.solution('w')
        self.assertEqual(result, 'w')
    def test_prob1_case_2(self):
        result = prob1.solution('xbwwb')
        self.assertEqual(result, 'xwbbw')
    def test_prob1_case_3(self):
        result = prob1.solution('xbwxwbbwb')
        self.assertEqual(result, 'xxbwwbbbw')
    def test_prob1_case_4(self):
        result = prob1.solution('xxwwwbxwxwbbbwwxxxwwbbbwwwwbb')
        self.assertEqual(result, 'xxwbxwwxbbwwbwbxwbwwxwwwxbbwb')

if __name__ == '__main__':
    unittest.main()
