from heapq import heappush, heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dir_ = ((1, 0), (-1, 0), (0, 1), (0, -1))
        seen = [[False]*N for _ in range(N)]
        q = [(grid[0][0], 0, 0)]
        while q:
            t, y, x = heappop(q)
            if y == N-1 and x == N-1: return t
            if seen[y][x]: continue
            seen[y][x] = True
            for ny, nx in ((y+r, x+c) for r, c in dir_):
                if 0 <= ny < N and 0 <= nx < N:
                    heappush(q, (max(t, grid[ny][nx]), ny, nx))