from heapq import heappush, heappop

class Solution:
    def shortestPath(self, grid: List[List[int]], K: int) -> int:
        if not grid: return -1
        N, M = len(grid), len(grid[0])
        dir_ = (-1, 0, 1, 0, -1)
        
        q = [(0, N+M-2, -K, 0, 0)]
        seen = {(0, 0): -K}
        
        while q:
            s, d, k, y, x = heappop(q)
            if y == N-1 and x == M-1: return s
            for ny, nx in ((y+r, x+c) for r, c in zip(dir_, dir_[1:])):
                if 0 <= ny < N and 0 <= nx < M:
                    nd = N + M - ny - nx - 2
                    if (ny, nx) not in seen or seen[ny, nx] > k:
                        seen[ny, nx] = k
                        if grid[ny][nx] == 1:
                            if k < 0: heappush(q, (s+1, nd, k+1, ny, nx))
                        else: heappush(q, (s+1, nd, k, ny, nx))
        return -1