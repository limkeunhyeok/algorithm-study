import unittest
import prob1, prob2, prob3, prob4, prob5, prob6

class NHNProbTest(unittest.TestCase):
    # Prob1 tests
    def test_prob1_case_1(self):
        result = prob1.solution(4, 4, 3, [[2, 2, 3], [3, 1, 4], [4, 4, 4]])
        self.assertEqual(result, 9)
    def test_prob1_case_2(self):
        result = prob1.solution(4, 4, 0, [])
        self.assertEqual(result, 16)
    def test_prob1_case_3(self):
        result = prob1.solution(2, 2, 2, [[2, 1, 1], [1, 1, 2]])
        self.assertEqual(result, 1)
    def test_prob1_case_4(self):
        result = prob1.solution(1, 1, 1, [[1, 1, 1]])
        self.assertEqual(result, 0)
    def test_prob1_case_5(self):
        result = prob1.solution(5, 3, 1, [[5, 1, 3]])
        self.assertEqual(result, 12)
 
    # Prob2 tests
    def test_prob2_case_1(self):
        result = prob2.solution(4, ["abc", "abcba", "abcd", "cba"])
        self.assertEqual(result, [2, 0, 4, 2])
    def test_prob2_case_2(self):
        result = prob2.solution(1, ["axz"])
        self.assertEqual(result, [25])   
    def test_prob2_case_3(self):
        result = prob2.solution(3, ["axz", "zzza", "wne"])
        self.assertEqual(result, [25, 25, 18])   
    def test_prob2_case_4(self):
        result = prob2.solution(0, [])
        self.assertEqual(result, [])

    # Prob3 tests
    def test_prob3_case_1(self):
        result = prob3.solution(5, [1, 2, 3, 17, 10])
        self.assertEqual(result, 3)
    def test_prob3_case_2(self):
        result = prob3.solution(5, [1, 2, 3, 12, 10])
        self.assertEqual(result, 2)
    def test_prob3_case_3(self):
        result = prob3.solution(8, [1, 2, 3, 12, 100, 15, 40, 44])
        self.assertEqual(result, 4)
    def test_prob3_case_4(self):
        result = prob3.solution(5, [10, 20, 30, 40, 50])
        self.assertEqual(result, 5)
    def test_prob3_case_5(self):
        result = prob3.solution(100, [i + 1 for i in range(100)])
        self.assertEqual(result, 20)

    # Prob4 tests
    def test_prob4_case_1(self):
        result = prob4.solution(4, [1, 3, 7, 13])
        self.assertEqual(result, 3)
    def test_prob4_case_2(self):
        result = prob4.solution(4, [1, 3, 7, 10])
        self.assertEqual(result, 6)
    def test_prob4_case_3(self):
        result = prob4.solution(3, [1, 4, 19])
        self.assertEqual(result, 4)

    # Prob5 tests
    def test_prob5_case_1(self):
        result = prob5.solution(4, 5, [[1, 2, 3], [1, 3, 10], [1, 4, 1], [2, 3, 4], [3, 4, 2]])
        self.assertEqual(result, 6)
    def test_prob5_case_2(self):
        result = prob5.solution(7, 8, [[1, 4, 4], [1, 5, 1], [2, 3, 2], [2, 4, 8], [3, 4, 3], [4, 5, 10], [5, 6, 1], [6, 7, 9]])
        self.assertEqual(result, 20)
    def test_prob5_case_3(self):
        result = prob5.solution(3, 3, [[1, 2, 1], [1, 3, 2], [2, 3, 3]])
        self.assertEqual(result, 3)
    def test_prob5_case_4(self):
        result = prob5.solution(3, 1, [[1, 2, 1]])
        self.assertEqual(result, -1)

    # Prob6 tests
    def test_prob6_case_1(self):
        result = prob6.solution(4, [1, 6, 7, 10])
        self.assertEqual(result, 12)
    def test_prob6_case_2(self):
        result = prob6.solution(3, [1, 6, 8])
        self.assertEqual(result, 8)
    def test_prob6_case_3(self):
        result = prob6.solution(4, [1, 1, 1, 1])
        self.assertEqual(result, 4)
    def test_prob6_case_4(self):
        result = prob6.solution(11, [1, 1, 30, 1, 1, 1, 1, 1, 1, 99, 1])
        self.assertEqual(result, 100)



if __name__ == '__main__':
    unittest.main()
