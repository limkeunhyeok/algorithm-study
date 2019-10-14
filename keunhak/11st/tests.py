import unittest
import prob1, prob2

class elevenstProbTest(unittest.TestCase):
    # boggle tests
    def test_prob1_case_1(self):
        result = prob1.solution(10)
        self.assertEqual(result, [6, 4])
    def test_prob1_case_2(self):
        result = prob1.solution(14)
        self.assertEqual(result, [5, 8])

    def test_prob2_case_1(self):
        result = prob2.solution([20,8,10,1,4,15])
        self.assertEqual(result, 62)

if __name__ == '__main__':
    unittest.main()
