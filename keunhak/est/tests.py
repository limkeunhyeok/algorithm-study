import unittest
import prob1, prob2

class ESTProbTest(unittest.TestCase):
    # Prob1 tests
    def test_prob1_case_1(self):
        result = prob1.solution('aaaa')
        self.assertEqual(result, 2)
    def test_prob1_case_2(self):
        result = prob1.solution('aabbaabb')
        self.assertEqual(result, 8)
    def test_prob1_case_3(self):
        result = prob1.solution('aaabbb')
        self.assertEqual(result, 4)
    def test_prob1_case_4(self):
        result = prob1.solution('baaabbabbb')
        self.assertEqual(result, 7)
    def test_prob1_case_5(self):
        result = prob1.solution('babba')
        self.assertEqual(result, 5)
    def test_prob1_case_6(self):
        result = prob1.solution('abaaaa')
        self.assertEqual(result, 4)

    def test_prob2_case_1(self):
        result = prob2.solution((1, (2, (3, (2, None, None), None), (6, None, None)), (3, (3, None, None), (1, (5, None, None), (6, None, None)))))
        self.assertEqual(result, 3)
    def test_prob2_case_2(self):
        result = prob2.solution((1, (2, (1, None, None), (2, None, None)), (2, (4, None, None), (1, None, None))))
        self.assertEqual(result, 3)
    def test_prob2_case_3(self):
        result = prob2.solution((1, (2, (1, None, None), (2, None, None)), (2, (4, None, None), (1, None, None))))
        self.assertEqual(result, 2)
if __name__ == '__main__':
    unittest.main()
