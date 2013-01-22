#!/usr/bin/env python

import os, sys, copy, time, threading

def iszero(mat):
    for i in mat:
        for j in i:
            if j > 0:
                return False
    return True

directions = [(0, 0), (-1, 0), (0, -1), (1, 0), (0, 1)]

def eliminate(mat, point):
    rows = len(mat)
    cols = len(mat[0])
    minis = [[point[0], point[1], 1]]
    while len(minis):
        hit = [[0 for _j in range(cols)] for _i in range(rows)]
        total = len(minis)
        for i in range(total):
            if mat[minis[i][0]][minis[i][1]]:
                mat[minis[i][0]][minis[i][1]] -= 1
                minis[i][2] = 0
                if mat[minis[i][0]][minis[i][1]] == 0:
                    minis.append([minis[i][0]-1, minis[i][1], 1])
                    minis.append([minis[i][0], minis[i][1]-1, 2])
                    minis.append([minis[i][0]+1, minis[i][1], 3])
                    minis.append([minis[i][0], minis[i][1]+1, 4])
                    hit[minis[i][0]][minis[i][1]] = 1
            elif hit[minis[i][0]][minis[i][1]]:
                minis[i][2] = 0
            else:
                minis[i][0] += directions[minis[i][2]][0]
                minis[i][1] += directions[minis[i][2]][1]
        total = len(minis) - 1
        for i in range(total, -1, -1):
            if minis[i][2] == 0 or minis[i][0] < 0 or minis[i][0] >= rows or minis[i][1] < 0 or minis[i][1] >= cols:
                minis[i] = minis[len(minis)-1]
                minis.pop()

def eliminate_simu(mat, point):
    minis = []

    ret = []

    rows = len(mat)
    cols = len(mat[0])

    if mat[point[0]][point[1]]:
        mat[point[0]][point[1]] -= 1
        if mat[point[0]][point[1]] == 0:
            minis.append([point[0]-1, point[1], 1])
            minis.append([point[0], point[1]-1, 2])
            minis.append([point[0]+1, point[1], 3])
            minis.append([point[0], point[1]+1, 4])
    else:
        return ret

    while len(minis):
        total = len(minis) - 1
        for i in range(total, -1, -1):
            if minis[i][0] < -1:
                minis[i] = minis[len(minis)-1]
                minis.pop()

        total = len(minis) - 1
        for i in range(total, -1, -1):
            if minis[i][0] >= rows + 1:
                minis[i] = minis[len(minis)-1]
                minis.pop()

        total = len(minis) - 1
        for i in range(total, -1, -1):
            if minis[i][1] < 0 or minis[i][1] >= cols:
                minis[i] = minis[len(minis)-1]
                minis.pop()

        total = len(minis)
        for i in range(total):
            if minis[i][0] >= 0 and minis[i][0] < rows and minis[i][1] >= 0 and minis[i][1] < cols and mat[minis[i][0]][minis[i][1]]:
                ret.append((minis[i][0], minis[i][1]))
                mat[minis[i][0]][minis[i][1]] -= 1
                minis[i][2] = 0
                if mat[minis[i][0]][minis[i][1]] == 0:
                    minis.append([minis[i][0]-1, minis[i][1], 1])
                    minis.append([minis[i][0], minis[i][1]-1, 2])
                    minis.append([minis[i][0]+1, minis[i][1], 3])
                    minis.append([minis[i][0], minis[i][1]+1, 4])
            else:
                minis[i][0] += directions[minis[i][2]][0]
                minis[i][1] += directions[minis[i][2]][1]

        total = len(minis) - 1
        for i in range(total, -1, -1):
            if minis[i][2] == 0:
                minis[i] = minis[len(minis)-1]
                minis.pop()
    return ret

def preprocess(mat):
    rows = len(mat)
    cols = len(mat[0])
    rowcnt = [0] * rows
    colcnt = [0] * cols
    for i in range(rows):
        for j in range(cols):
            rowcnt[i] += mat[i][j] and 1 or 0
            colcnt[j] += mat[i][j] and 1 or 0
    ret = 0
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0: continue
            if mat[i][j] > rowcnt[i] + colcnt[j] - 2:
                delta = mat[i][j] + 2 - rowcnt[i] - colcnt[j]
                for k in range(delta):
                    print '(%d, %d)' % (i, j)
                ret += delta
                mat[i][j] = rowcnt[i] + colcnt[j] - 2
    return ret

def solve(mat, remain, ans, eliminator):
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
            eliminator(nm, [i, j])
            rs = solve(nm, remain-1, ans, eliminator)
            if rs:
                return True
    return not nonzero

def quick_solve(mat, remain, ans, eliminator):
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
                if quick_solve(nm, remain-1, ans, eliminator): return True
    for i in range(rows):
        for j in range(cols):
            if mat[i][j]:
                nonzero = True
            if mat[i][j] != 1:
                continue
            nonzero = True
            ans[remain] = (i,j)
            nm = copy.deepcopy(mat)
            eliminator(nm, [i, j])
            if quick_solve(nm, remain-1, ans, eliminator): return True
    return not nonzero

def main(mat, cnt, options):
    
    cnt -= preprocess(mat)

    solver = options['bruteforce'] and solve or quick_solve
    eliminator = options['android'] and eliminate_simu or eliminate

    start_time = time.time()
    ans = [-99] * 10
    if solver(mat, cnt, ans, eliminator):
        for i in range(cnt, 0, -1):
            print ans[i]
        print >> sys.stderr, 'found solution in %.2fs' % (time.time() - start_time)
    else:
        print 'no solution found in %.2fs' % (time.time() - start_time)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print >> sys.stderr, 'usage: %s <input> <count> [-a(for android)] [-b(brute force search)]' % sys.argv[0]
        sys.exit(10)
    options = {
        'android': False,
        'bruteforce': False
    }
    for p in sys.argv[3:]:
        if p == '-a':
            options['android'] = True
        elif p == '-b':
            options['bruteforce'] = True
    f = open(sys.argv[1], 'r')
    mat = []
    for line in f:
        line = line.strip()
        if line.startswith('#'):
            continue
        mat.append(map(lambda s: int(s), line.split(' ')))
    main(mat, int(sys.argv[2]), options)

