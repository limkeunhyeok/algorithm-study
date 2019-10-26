import unittest
import prob1, prob2, prob3, prob4

class WeMakePriceProbTests(unittest.TestCase):
    def test_prob1_case_1(self):
        result = prob1.solution(1)
        self.assertEqual(result, 1)
    def test_prob1_case_2(self):
        result = prob1.solution(2)
        self.assertEqual(result, 2)
    def test_prob1_case_3(self):
        result = prob1.solution(3)
        self.assertEqual(result, 3)
    def test_prob1_case_4(self):
        result = prob1.solution(4)
        self.assertEqual(result, 5)
    def test_prob1_case_5(self):
        result = prob1.solution(5)
        self.assertEqual(result, 8)
    def test_prob1_case_6(self):
        result = prob1.solution(6)
        self.assertEqual(result, 13)
    def test_prob1_case_7(self):
        result = prob1.solution(7)
        self.assertEqual(result, 21)

    def test_prob2_case_1(self):
        result = prob2.solution(111)
        self.assertEqual(result, 2)
    def test_prob2_case_2(self):
        result = prob2.solution(9999)
        self.assertEqual(result, 7379)

    def test_prob3_case_1(self):
        result = prob3.solution(300, 12, [58, 70, 54, 85, 99, 125, 100, 75, 76, 80, 88, 75])
        self.assertEqual(result, 4)
    def test_prob3_case_2(self):
        result = prob3.solution(200, 12, [58, 70, 54, 85, 99, 125, 201, 75, 76, 80, 88, 75])
        self.assertEqual(result, -1)
    def test_prob4_case_1(self):
        result = prob4.solution(4, [2, 1, 2, 2], { '1': ['2', '3'], '2': ['4'] })
        self.assertEqual(result, '4 5')
    def test_prob4_case_2(self):
        result = prob4.solution(5, [1, 1, 2, 3, 4], { '1': ['2', '3', '4', '5'] })
        self.assertEqual(result, '5 5')
    def test_prob4_case_3(self):
        result = prob4.solution(6, [1, 1, 1, 1, 1, 1], { '1': ['2', '3', '4'], '3': ['5', '6'] })
        self.assertEqual(result, '6 3')

if __name__ == '__main__':
    unittest.main()
