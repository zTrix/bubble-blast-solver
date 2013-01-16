
import solve, unittest

mat = [[1,2,2,2,1],[2,4,3,4,2],[2,2,2,2,2],[2,2,2,2,2],[1,2,2,1,1],[1,2,1,2,1]]
ops = [[0, 0, 0, 0, 0] for i in range(6)]
ops[4][3] = [1]
#solve.eliminate(mat, ops)

class Test(unittest.TestCase):
    def test_3(self):
        mat = [[0,1,0,0,1], [0,0,0,0,0],[0,2,0,0,1],[0,2,0,0,1],[0,0,0,0,0],[0,1,0,0,1]]
        ops = [[0, 0, 0, 0, 0] for i in range(6)]
        ops[2][4] = [1]
        solve.eliminate(mat, ops)
        self.assertEqual(mat, [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
        
    def test_4(self):
        mat = [[1,2,1,1,2],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        ops = [[0, 0, 0, 0, 0] for i in range(6)]
        ops[0][3] = [1]
        solve.eliminate(mat, ops)
        self.assertEqual(mat, [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

    def test_5(self):
        mat = [[0,0,0,0,0],[0,1,0,1,0],[1,1,0,1,1],[0,2,0,2,0],[0,1,0,1,0],[0,0,0,0,0]]
        ops = [[0, 0, 0, 0, 0] for i in range(6)]
        ops[2][1] = [1]
        solve.eliminate(mat, ops)
        self.assertEqual(mat, [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

    def test_6(self):
        mat = [[1,2,2,2,1],[2,4,3,4,2],[2,2,2,2,2],[2,2,2,2,2],[1,2,2,1,1],[1,2,1,2,1]]
        ops = [[0, 0, 0, 0, 0] for i in range(6)]
        ops[4][3] = [1]
        solve.eliminate(mat, ops)
        self.assertEqual(mat, [[0,0,0,1,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])

if __name__ == "__main__":
    unittest.main()
    a = 0
