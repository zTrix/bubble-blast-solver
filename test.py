
import solve, unittest

class Test(unittest.TestCase):
    def test_1(self):
        mat = [[1,2,0,3,4], [1,2,1,0,1], [0,1,3,1,4], [0,0,1,0,0], [0,0,0,1,2], [1,0,0,0,0]]
        ops = [[0, 0, 0, 0, 0] for i in range(6)]
        ops[1][2] = [1]
        solve.eliminate(mat, ops)
        self.assertEqual(mat, [[0,0,0,1,3],[0,0,0,0,0],[0,0,1,1,3],[0,0,1,0,0],[0,0,0,1,2],[0,0,0,0,0]])

    def test_2(self):
        mat = [[1,3,2,0,2], [1,3,1,1,3], [2,1,1,3,0], [3,1,1,3,2], [1,2,0,0,4], [0,2,3,4,2]]
        ops = [[0, 0, 0, 0, 0] for i in range(6)]
        ops[2][2] = [1]
        solve.eliminate(mat, ops)
        self.assertEqual(mat, [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

    def test_3(self):
        mat = [[0,1,0,0,1], [0,0,0,0,0],[0,2,0,0,1],[0,2,0,0,1],[0,0,0,0,0],[0,1,0,0,1]]
        ops = [[0, 0, 0, 0, 0] for i in range(6)]
        ops[2][4] = [1]
        solve.eliminate(mat, ops)
        self.assertEqual(mat, [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
        

if __name__ == "__main__":
    unittest.main()
