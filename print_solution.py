#!/usr/bin/env python
# encoding=utf8

import os, sys, solve, copy

def print_sol(mat, sol):
    mat = copy.deepcopy(mat)
    rows = len(mat)
    cols = len(mat[0])
    for r in mat:
        print r
    print ''
    for i,j in sol:
        op = [[0 for _j in range(cols)] for _i in range(rows)]
        op[i][j] = [(1,0)]
        print i,j
        print ''
        solve.eliminate(mat, op)
        for r in mat:
            print r
        print ''

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'usage: %s <puzzle board> <solution file>'
        sys.exit(10)
    f = open(sys.argv[1], 'r')
    mat = []
    for line in f:
        line = line.strip()
        if line.startswith('#'):
            continue
        mat.append(map(lambda s: int(s), line.split(' ')))
    f.close()
    f = open(sys.argv[2], 'r')
    sol = []
    for line in f:
        sol.append(map(lambda s: int(s), line.strip()[1:-1].split(',')))
    print_sol(mat, sol)
