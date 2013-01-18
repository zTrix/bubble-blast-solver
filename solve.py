#!/usr/bin/env python

import os, sys, copy, time

ans = [-99] * 100

def iszero(mat):
    for i in mat:
        for j in i:
            if j > 0:
                return False
    return True

directions = [(0, 0), (-1, 0), (0, -1), (1, 0), (0, 1)]

# example: eliminate_simu(mat, [2, 3])
def eliminate_simu(mat, point):
    minis = [[point[0], point[1], 1]]

    rows = len(mat)
    cols = len(mat[0])

    def add(i, j, s):
        if i < rows and i >= 0 and j < cols and j >= 0:
            minis.append([i, j, s])

    while len(minis):
        total = len(minis)
        for i in range(total):
            if mat[minis[i][0]][minis[i][1]]:
                mat[minis[i][0]][minis[i][1]] -= 1
                minis[i][2] = 0
                if mat[minis[i][0]][minis[i][1]] == 0:
                    add(minis[i][0]-1, minis[i][1], 1)
                    add(minis[i][0], minis[i][1]-1, 2)
                    add(minis[i][0]+1, minis[i][1], 3)
                    add(minis[i][0], minis[i][1]+1, 4)
            else:
                add(minis[i][0] + directions[minis[i][2]][0], minis[i][1] + directions[minis[i][2]][1], minis[i][2])
                minis[i][2] = 0
        total = len(minis) - 1
        for i in range(total, -1, -1):
            if minis[i][2] == 0:
                minis[i] = minis[len(minis)-1]
                minis.pop()

## example here:
# op = [[0 for _j in range(cols)] for _i in range(rows)]
# op[i][j] = [(1,0)]
# eliminate(mat, op)

def eliminate(mat, ops):
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
                        flag += add(i-1, j, 1, 1)
                        flag += add(i, j+1, 4, 1)
                        flag += add(i, j-1, 2, 1)
                        mat[i][j] = 0
                else:
                    for b, d in ops[i][j]:
                        flag += add(i + directions[b][0], j + directions[b][1], b, d+1)
    if flag:
        eliminate(mat, new_ops)

def solve(mat, remain):
    if remain == 0:
        return iszero(mat)
    nonzero = False
    rows = len(mat)
    cols = len(mat[0])
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                continue
            nonzero = True
            ans[remain] = (i,j)
            nm = copy.deepcopy(mat)
            op = [[0 for _j in range(cols)] for _i in range(rows)]
            op[i][j] = [(1,0)]
            eliminate(nm, op)
            rs = solve(nm, remain-1)
            if rs:
                return True
    return not nonzero

def quick_solve(mat, remain):
    if remain == 0:
        return iszero(mat)
    rows = len(mat)
    cols = len(mat[0])
    non_red = False
    nonzero = False
    if remain > 1:
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] < 2:
                    continue
                nonzero = True
                ans[remain] = (i,j)
                non_red = True
                nm = copy.deepcopy(mat)
                nm[i][j] -= 1
                if quick_solve(nm, remain-1): return True
    for i in range(rows):
        for j in range(cols):
            if mat[i][j]:
                nonzero = True
            if mat[i][j] != 1:
                continue
            nonzero = True
            ans[remain] = (i,j)
            nm = copy.deepcopy(mat)
            eliminate_simu(nm, [i, j])
            if solve(nm, remain-1): return True
    return not nonzero

def main(filepath, cnt):
    f = open(filepath)
    mat = []
    for line in f:
        line = line.strip()
        if line.startswith('#'):
            continue
        mat.append(map(lambda s: int(s), line.split(' ')))
    print >> sys.stderr, 'trying quick solution...'
    start_time = time.time()
    if quick_solve(mat, cnt):
        print >> sys.stderr, 'found solution in %.2fs using quick solution' % (time.time() - start_time)
        for i in range(cnt, 0, -1):
            print ans[i]
        return 0
    print >> sys.stderr, 'no solution using quick logic(%.2fs), trying brute force' % (time.time() - start_time)
    start_time = time.time()
    if solve(mat, cnt):
        print >> sys.stderr, 'found solution in %.2fs using brute force' % (time.time() - start_time)
        for i in range(cnt, 0, -1):
            print ans[i]
        return 0
    print >> sys.stderr, 'no solution under normal logic(%.2fs), trying brute force with buggy elimination...' % (time.time() - start_time)
    return 11

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print >> sys.stderr, 'usage: %s <input> <count>' % sys.argv[0]
        sys.exit(10)
    sys.exit(main(sys.argv[1], int(sys.argv[2])))

