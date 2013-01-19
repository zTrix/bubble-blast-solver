#!/usr/bin/env python

import os, sys, copy, time, threading

def iszero(mat):
    for i in mat:
        for j in i:
            if j > 0:
                return False
    return True

directions = [(0, 0), (-1, 0), (0, -1), (1, 0), (0, 1)]

# example: eliminate_simu(mat, [2, 3])
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

def solve(mat, remain, ans):
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
            rs = solve(nm, remain-1, ans)
            if rs:
                return True
    return not nonzero

def quick_solve(mat, remain, ans):
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
                if quick_solve(nm, remain-1, ans): return True
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
            if quick_solve(nm, remain-1, ans): return True
    return not nonzero

solved = False
lock = threading.Lock()

def run(func, mat, cnt, name):
    global solved
    print >> sys.stderr, 'trying %s ...' % name
    start_time = time.time()
    ans = [-99] * 10
    if func(mat, cnt, ans):
        lock.acquire()
        solved = True
        print >> sys.stderr, 'found solution in %.2fs using %s solution' % (time.time() - start_time, name)
        for i in range(cnt, 0, -1):
            print ans[i]
        lock.release()
        return 0
    print >> sys.stderr, 'no solution found using %s(%.2fs)' % (name, time.time() - start_time)

def main(mat, cnt):
    t = threading.Thread(target = run, args = (quick_solve, mat, cnt, 'quick solution'))
    t.setDaemon(True)
    t.start()

    t = threading.Thread(target = run, args = (solve, mat, cnt, 'brute-force solution'))
    t.setDaemon(True)
    t.start()

    while True:
        if threading.active_count() == 1:
            sys.exit(0)
        if not solved:
            time.sleep(5)
        else:
            time.sleep(3)
            sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print >> sys.stderr, 'usage: %s <input> <count>' % sys.argv[0]
        sys.exit(10)
    f = open(sys.argv[1], 'r')
    mat = []
    for line in f:
        line = line.strip()
        if line.startswith('#'):
            continue
        mat.append(map(lambda s: int(s), line.split(' ')))
    main(mat, int(sys.argv[2]))

