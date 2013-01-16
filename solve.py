#!/usr/bin/env python

import os, sys, copy, Queue

ans = [-99] * 100

def iszero(mat):
    for i in mat:
        for j in i:
            if j > 0:
                return False
    return True

directions = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]

def eliminate(mat, ops):
    #print '\n', ops
    #for i in mat:
    #    print i
    #raw_input("\ncontinue ...\n")
    rows = len(mat)
    cols = len(mat[0])
    new_ops = [[[] for j in range(cols)] for i in range(rows)]

    flag = 0

    def add(i, j, b, d):
        if i < rows and i >= 0 and j < cols and j >= 0:
            new_ops[i][j].append((b, d))
            return 1
        return 0

    def cmp(a, b):
        return a[1] > b[1] and 1 or (a[1] < b[1] and -1 or 0)

    for i in range(rows):
        for j in range(cols):
            if ops[i][j]:
                if mat[i][j]:
                    if mat[i][j] > len(ops[i][j]):
                        mat[i][j] -= len(ops[i][j])
                    else:
                        flag += add(i+1, j, 3, 1)
                        flag += add(i-1, j, 4, 1)
                        flag += add(i, j+1, 1, 1)
                        flag += add(i, j-1, 2, 1)
                        if mat[i][j] == len(ops[i][j]):
                            mat[i][j] = 0
                            continue
                        ops[i][j].sort(cmp = cmp)
                        k = mat[i][j]
                        mat[i][j] = 0
                        mind = ops[i][j][k-1][1]
                        while k < len(ops[i][j]):
                            if ops[i][j][k][1] == mind:
                                k += 1
                                continue
                            flag += add(i + directions[ops[i][j][k][0]][0], j + directions[ops[i][j][k][0]][1], ops[i][j][k][0], ops[i][j][k][1]+1)
                            k += 1
                else:
                    for b, d in ops[i][j]:
                        flag += add(i + directions[b][0], j + directions[b][1], b, d+1)
    if flag:
        eliminate(mat, new_ops)

def solve(mat, remain):
    if remain == 0:
        return iszero(mat)
    has = False
    rows = len(mat)
    cols = len(mat[0])
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                continue
            has = True
            ans[remain] = (i,j)
            nm = copy.deepcopy(mat)
            op = [[0 for _j in range(cols)] for _i in range(rows)]
            op[i][j] = [1]
            eliminate(nm, op)
            rs = solve(nm, remain-1)
            if rs:
                return True
    return not has

def main(filepath, cnt):
    f = open(filepath)
    mat = []
    for line in f:
        mat.append(map(lambda s: int(s), line.strip().split(' ')))
    if solve(mat, cnt):
        for i in range(cnt, 0, -1):
            print ans[i]
    else:
        print 'cannot find solution'

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'usage: %s <input> <count>' % sys.argv[0]
        sys.exit(10)
    sys.exit(main(sys.argv[1], int(sys.argv[2])))

