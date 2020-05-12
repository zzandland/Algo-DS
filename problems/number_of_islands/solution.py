from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        R, C, res = len(grid), len(grid[0]), 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1':
                    grid[i][j], res, q = '0', res+1, deque([(i, j)])
                    while q:
                        y, x = q.popleft()
                        for r, c in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            ny, nx = y+r, x+c
                            if 0 <= ny < R and 0 <= nx < C and grid[ny][nx] == '1':
                                grid[ny][nx] = '0'
                                q.append((ny, nx))
        return res                        