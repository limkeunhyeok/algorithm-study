import unittest
import boggle, tsp, prob1, prob2, prob3

class Chap6ProbTest(unittest.TestCase):
    # boggle tests
    def test_boggle_case_1(self):
        result = boggle.solution(1, 1, 'pretty')
        self.assertEqual(result, True)
    def test_boggle_case_2(self):
        result = boggle.solution(2, 0, 'girl')
        self.assertEqual(result, True)
    def test_boggle_case_3(self):
        result = boggle.solution(1, 2, 'repeat')
        self.assertEqual(result, True)
    def test_boggle_case_4(self):
        result = boggle.solution(0, 0, 'keunhak')
        self.assertEqual(result, False)
    def test_boggle_case_5(self):
        result = boggle.solution(0, 0, 'hongik')
        self.assertEqual(result, False)
    def test_boggle_case_6(self):
        result = boggle.solution(0, 0, 'upr')
        self.assertEqual(result, True)

    # TSP tests
    def test_tsp_case_1(self):
        result = tsp.solution(3, [
            [0, 1, 4], 
            [1, 0, 3], 
            [4, 3, 0]
            ])
        self.assertEqual(result, 8)
    def test_tsp_case_2(self):
        result = tsp.solution(2, [
            [0, 1], 
            [1, 0] 
            ])
        self.assertEqual(result, 2)

    # Prob1 tests
    def test_prob1_case_1(self):
        result = prob1.solution(2, 1, [(0, 1)])
        self.assertEqual(result, 1)
    def test_prob1_case_2(self):
        result = prob1.solution(4, 6, [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2), (1, 3)])
        self.assertEqual(result, 3)
    def test_prob1_case_3(self):
        result = prob1.solution(6, 10, [(0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5)])
        self.assertEqual(result, 4)
    def test_prob1_case_4(self):
        result = prob1.solution(4, 1, [(0, 1)])
        self.assertEqual(result, 0)

    # Prob2 tests
    def test_prob2_case_1(self):
        result = prob2.solution(3, 7, [
            ['#', '.', '.', '.', '.', '.', '#'],
            ['#', '.', '.', '.', '.', '.', '#'],
            ['#', '#', '.', '.', '.', '#', '#']
            ])
        self.assertEqual(result, 0)
    def test_prob2_case_2(self):
        result = prob2.solution(3, 7, [
            ['#', '.', '.', '.', '.', '.', '#'],
            ['#', '.', '.', '.', '.', '.', '#'],
            ['#', '#', '.', '.', '#', '#', '#']
            ])
        self.assertEqual(result, 2)
    def test_prob2_case_3(self):
        result = prob2.solution(2, 3, [
            ['#', '.', '#'],
            ['#', '.', '.']
            ])
        self.assertEqual(result, 1)
    '''
    def test_prob2_case_4(self):
        result = prob2.solution(8, 10, [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
            ])
        self.assertEqual(result, 1514)
    '''

    # Prob3 tests
    def test_prob3_case_1(self):
        result = prob3.solution([12, 6, 6, 6, 6, 6, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12])
        self.assertEqual(result, 2)
    def test_prob3_case_2(self):
        result = prob3.solution([12, 9, 3, 12, 6, 6, 9, 3, 12, 9, 12, 9, 12, 12, 6, 6])
        self.assertEqual(result, 9)

if __name__ == '__main__':
    unittest.main()
