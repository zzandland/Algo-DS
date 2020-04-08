#  Given a matrix with r rows and c columns, find the maximum score of a path starting at [0, 0] and ending at [r-1, c-1]. The score of a path is the minimum value in that path. For example, the score of the path 8 => 4 => 5 => 9 is 4.

#  Don't include the first or final entry. You can only move either down or right at any point in time.

#  Example 1:

#  Input:
grid = [[5, 1], [4, 5]]

#  Output: 4
#  Explanation:
#  Possible paths:
#  5 => 1 => 5 => min value is 1
#  5 => 4 => 5 => min value is 4
#  Return the max value among minimum values => max(4, 1) = 4.
#  Example 2:

#  Input:
#  grid = [[1, 2, 3], [4, 5, 1]]

#  Output: 4
#  Explanation:
#  Possible paths:
#  1-> 2 -> 3 -> 1
#  1-> 2 -> 5 -> 1
#  1-> 4 -> 5 -> 1
#  So min of all the paths = [2, 2, 4]. Note that we don't include the first and final entry.
#  Return the max of that, so 4.

import heapq

def maxMinAlt(grid):
    R, C = len(grid), len(grid[0])
    seen, dir_ = [[False for _ in range(C)] for _ in range(R)], [(0, 1),(1, 0)]
    def diijkstra():
        hp, min_ = [(-grid[0][0], 0, 0)], float('inf')
        while hp:
            print(hp, min_)
            al, y, x = heapq.heappop(hp)
            if y != 0 or x != 0: min_ = min(min_, grid[y][x])
            seen[y][x] = True
            for r, c in dir_:
                ny, nx = y+r, x+c
                if ny < R and nx < C and not seen[ny][nx]:
                    if ny == R-1 and nx == C-1: return min_
                    heapq.heappush(hp, (-grid[ny][nx], ny, nx))
        return min_
    def unionFind():
        uf = [i for i in range(R*C)]
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        def union(a, b):
            ua, ub = find(a), find(b)
            if ua != ub:
                uf[ua] = ub
        union(0, 1)
        union(0, C)
        for y, x in sorted([(r, c) for r in range(R) for c in range(C)], key=lambda x: grid[x[0]][x[1]], reverse=True):
            seen[y][x] = True
            print(grid[y][x], seen, uf)
            for ver, hor in dir_:
                ny, nx = y+ver, x+hor
                if ny < R and nx < C and seen[y][x]: union(ny*C+nx, y*C+x)
                if find(0) == find(R*C-1): return grid[y][x]
    return unionFind()

print(maxMinAlt(grid))
