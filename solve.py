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

# preprocess mat, handle those bubbles that must give touches, return touches total at least
def preprocess(mat, remain, ans):
    if remain < 2:
        return 0
    rows = len(mat)
    cols = len(mat[0])
    rowcnt = [0] * rows
    colcnt = [0] * cols
    for i in range(rows):
        for j in range(cols):
            if mat[i][j]:
                rowcnt[i] += 1
                colcnt[j] += 1
    ret = 0
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0: continue
            attack = rowcnt[i] + colcnt[j] - 2
            if mat[i][j] > attack:
                delta = mat[i][j] - attack
                for k in range(delta):
                    if k < remain:
                        ans[remain-k] = (i, j)
                ret += delta
                mat[i][j] = attack
                if ret > remain:
                    return ret
    return ret

def solve(mat, remain, ans, eliminator):
    atleast = preprocess(mat, remain, ans)

    if remain < atleast:
        return False
    elif remain == 0:
        return iszero(mat)
    else:
        remain -= atleast

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
    atleast = preprocess(mat, remain, ans)

    if remain < atleast:
        return False
    elif remain == 0:
        return iszero(mat)
    else:
        remain -= atleast

    rows = len(mat)
    cols = len(mat[0])
    nonzero = False
    if remain > 1:
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] < 2:
                    continue
                nonzero = True
                ans[remain] = (i,j)
                nm = copy.deepcopy(mat)
                nm[i][j] -= 1
                if quick_solve(nm, remain-1, ans, eliminator): return True
    for i in range(rows):
        for j in range(cols):
            if mat[i][j]:
                nonzero = True
            if mat[i][j] != 1:
                continue
            ans[remain] = (i,j)
            nm = copy.deepcopy(mat)
            eliminator(nm, [i, j])
            if quick_solve(nm, remain-1, ans, eliminator): return True
    return not nonzero

def main(mat, cnt, options):
    global preprocess

    solver = options['bruteforce'] and solve or quick_solve
    eliminator = options['android'] and eliminate_simu or eliminate
    if options['nopreprocess']:
        preprocess = lambda mat, remain, ans: 0

    start_time = time.time()
    ans = [-99] * 10
    if solver(mat, cnt, ans, eliminator):
        for i in range(cnt, 0, -1):
            print ans[i]
        print >> sys.stderr, 'found solution in %.2fs' % (time.time() - start_time)
    else:
        print 'no solution found in %.2fs' % (time.time() - start_time)

def usage():
    print >> sys.stderr, 'usage: %s <input> <count> [--np] [-a] [-b]' % sys.argv[0]
    print >> sys.stderr, 'options:'
    print >> sys.stderr, '     -a: switch on special elimination logic for android'
    print >> sys.stderr, '     -b: switch on brute force search'
    print >> sys.stderr, '   --np: switch off preprocess strategy'
    return 10

if __name__ == '__main__':
    touch_max = 0
    if len(sys.argv) < 2:
        sys.exit(usage())
    if len(sys.argv) < 3:
        touch_max = int(open(sys.argv[1], 'r').readline().split('#')[1].strip())
    else:
        touch_max = int(sys.argv[2])
    if touch_max <= 0:
        sys.exit(usage())
    else:
        print 'touch max = %d' % touch_max
    options = {
        'android': False,
        'bruteforce': False,
        'nopreprocess': False
    }
    for p in sys.argv[3:]:
        if p == '-a':
            options['android'] = True
        elif p == '-b':
            options['bruteforce'] = True
        elif p == '--np':
            options['nopreprocess'] = True
    f = open(sys.argv[1], 'r')
    mat = []
    for line in f:
        line = line.strip()
        if line.startswith('#'):
            continue
        mat.append(map(lambda s: int(s), line.split(' ')))
    main(mat, touch_max, options)

