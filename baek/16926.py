def solve(matrix: [[int]], r: int) -> [[int]]:
    M, N = len(matrix), len(matrix[0])

    dir_ = ((0, 1), (1, 0), (0, -1), (-1, 0))
    for i in range(min(M//2, N//2)):
        layer = []
        y = x = i
        yl, yr = i, M-i-1
        xl, xr = i, N-i-1
        d = 0
        while d < 4:
            ny, nx = y+dir_[d][0], x+dir_[d][1]
            if not (yl <= ny <= yr and xl <= nx <= xr): d += 1
            else:
                layer.append(matrix[y][x])
                y, x = ny, nx
        r %= len(layer)
        layer = layer[r:] + layer[:r]
        d = i = 0
        while d < 4:
            ny, nx = y+dir_[d][0], x+dir_[d][1]
            if not (yl <= ny <= yr and xl <= nx <= xr): d += 1
            else:
                matrix[y][x] = layer[i]
                y, x = ny, nx
                i += 1
    return matrix

import sys
readline = sys.stdin.readline

M, N, r = [int(n) for n in readline().split()]
matrix = []
for _ in range(M):
    matrix.append(readline().split())

res = solve(matrix, r)
for row in res:
    print(' '.join(row))
