#!/usr/bin/env python

import solve, unittest, time

class Test(unittest.TestCase):
    
    def test_seq_1(self):
        mat=[[3, 1, 2, 2, 1], [1, 3, 4, 2, 0], [4, 1, 1, 4, 2], [4, 4, 1, 0, 3], [3, 1, 0, 0, 1], [2, 1, 1, 2, 3]]
        ret = solve.eliminate_simu(mat, [1, 0])
        self.assertEqual(ret, [(0,0), (1,1), (2,0)])
    
    def test_seq_2(self):
        mat=[[3, 1, 2, 2, 1], [1, 3, 4, 2, 0], [4, 1, 1, 4, 2], [4, 4, 1, 0, 3], [3, 1, 0, 0, 1], [2, 1, 1, 2, 3]]
        ret = solve.eliminate_simu(mat, [0, 4])
        self.assertEqual(ret, [(0,3), (2,4)])

    def test_seq_3(self):
        mat=[[3, 1, 2, 2, 1], [1, 3, 4, 2, 0], [4, 1, 1, 4, 2], [4, 4, 1, 0, 3], [3, 1, 0, 0, 1], [2, 1, 1, 2, 3]]
        ret = solve.eliminate_simu(mat, [0, 1])
        self.assertEqual(ret, [(0,0), (1,1), (0, 2)])

    def test_3(self):
        mat = [[0,1,0,0,1], [0,0,0,0,0],[0,2,0,0,1],[0,2,0,0,1],[0,0,0,0,0],[0,1,0,0,1]]
        solve.eliminate_simu(mat, [2, 4])
        self.assertEqual(mat, [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
        
    def test_4(self):
        mat = [[1,2,1,1,2],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        solve.eliminate_simu(mat, [0,3])
        self.assertEqual(mat, [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

    def test_5(self):
        mat = [[0,0,0,0,0],[0,1,0,1,0],[1,1,0,1,1],[0,2,0,2,0],[0,1,0,1,0],[0,0,0,0,0]]
        solve.eliminate_simu(mat, [2,1])
        self.assertEqual(mat, [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

    def test_6(self):
        mat = [[1,2,2,2,1],[2,4,3,4,2],[2,2,2,2,2],[2,2,2,2,2],[1,2,2,1,1],[1,2,1,2,1]]
        solve.eliminate_simu(mat, [4,3])
        self.assertEqual(mat, [[0,0,0,1,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

    def test_7(self):
        mat = [[1,2,2,2,1],[2,4,3,4,2],[1,2,2,2,2],[0,1,2,2,2],[0,1,2,2,1],[0,1,1,2,1]]
        solve.eliminate_simu(mat, [3,1])
        self.assertEqual(mat, [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

    def test_8(self):
        mat = [[1, 0, 1, 0, 1], [2,0,1,0,2],[2,0,1,0,2],[2,0,1,0,2],[2,0,1,0,2],[2,3,1,3,2]]
        solve.eliminate_simu(mat, [3,2])
        self.assertEqual(mat, [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,2,0,2,1]])

    def test_9(self):
        mat = [[4,2,2,3,1],[0,2,0,1,2],[4,1,3,4,4],[4,1,1,4,1],[1,2,3,1,1],[1,0,3,3,0]]
        solve.eliminate_simu(mat, [3,2])
        self.assertEqual(mat, [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

if __name__ == "__main__":
    unittest.main()
    a = 0

