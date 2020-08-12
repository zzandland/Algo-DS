from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        res = 0
        dir_ = (-1, 0, 1, 0, -1)
        for y in range(m):
            for x in range(n):
                if grid[y][x] == '1':
                    res += 1
                    grid[y][x] = '0'
                    q = deque([(y, x)])
                    while q:
                        r, c = q.popleft()
                        for nr, nc in ((r+rr, c+cc) for rr, cc in zip(dir_, dir_[1:])):
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                                grid[nr][nc] = '0'
                                q.append((nr, nc))
        return res