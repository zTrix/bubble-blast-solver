#!/usr/bin/env python

import os, sys, copy, Queue

ans = [-99] * 100

def iszero(mat):
    for i in mat:
        for j in i:
            if j > 0:
                return False
    return True

def action(mat, ops):
    q = []
    for i,j in ops:
        for k in range(i+1, len(mat)):
            if mat[k][j]:
                mat[k][j] -= 1
                if mat[k][j] == 0: q.append((k,j))
                break
        for k in range(i-1, -1, -1):
            if mat[k][j]:
                mat[k][j] -= 1
                if mat[k][j] == 0: q.append((k,j))
                break
        for k in range(j+1, len(mat[0])):
            if mat[i][k]:
                mat[i][k] -= 1
                if mat[i][k] == 0:
                    q.append((i, k))
                break
        for k in range(j-1, -1, -1):
            if mat[i][k]:
                mat[i][k] -= 1
                if mat[i][k] == 0:
                    q.append((i, k))
                break
    if len(q):
        action(mat, q)

def solve(mat, remain):
    if remain == 0:
        return iszero(mat)
    has = False
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                continue
            has = True
            ans[remain] = (i,j)
            nm = copy.deepcopy(mat)
            nm[i][j] -= 1
            if nm[i][j] == 0:
                action(nm, [(i, j)])
            rs = solve(nm, remain-1)
            if rs:
                return True
    return not has

def main(filepath, cnt):
    f = open(filepath)
    mat = []
    for line in f:
        mat.append(map(lambda s: int(s), line.strip().split(' ')))
    rows = len(mat)
    cols = len(mat[0])
    if solve(mat, cnt):
        for i in range(cnt, 0, -1):
            print ans[i]
    else:
        print 'cannot find solution'

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'usage: %s <input> <count>' % sys.argv[0]
    sys.exit(main(sys.argv[1], int(sys.argv[2])))