import unittest
import prob1, prob1_2, prob2

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

    def test_prob1_2_case_1(self):
        result = prob1_2.solution('w')
        self.assertEqual(result, 'w')
    def test_prob1_2_case_2(self):
        result = prob1_2.solution('xbwwb')
        self.assertEqual(result, 'xwbbw')
    def test_prob1_2_case_3(self):
        result = prob1_2.solution('xbwxwbbwb')
        self.assertEqual(result, 'xxbwwbbbw')
    def test_prob1_2_case_4(self):
        result = prob1_2.solution('xxwwwbxwxwbbbwwxxxwwbbbwwwwbb')
        self.assertEqual(result, 'xxwbxwwxbbwwbwbxwbwwxwwwxbbwb')

    def test_prob2_case_1(self):
        result = prob2.solution([7, 1, 5, 9, 6, 7, 3])
        self.assertEqual(result, 20)
    def test_prob2_case_2(self):
        result = prob2.solution([1, 4, 4, 4, 4, 1, 1])
        self.assertEqual(result, 16)
    def test_prob2_case_3(self):
        result = prob2.solution([1, 8, 1, 1])
        self.assertEqual(result, 8)
    def test_prob2_case_4(self):
        result = prob2.solution([10000, 10000, 10000 ])
        self.assertEqual(result, 30000)
    def test_prob2_case_5(self):
        result = prob2.solution([10000 for T in range(20000)])
        self.assertEqual(result, 200000000)

if __name__ == '__main__':
    unittest.main()
