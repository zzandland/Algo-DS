from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        R, C = len(grid), len(grid[0])
        dir_, res = ((1, 0), (0, 1), (-1, 0), (0, -1)), 0
        for y, x in [[y, x] for y in range(R) for x in range(C)]:
            if grid[y][x] == '1':
                res += 1
                grid[y][x] = '0'
                q = deque([[y, x]])
                while q:
                    r, c = q.popleft()
                    for ny, nx in [[r+r2, c+c2] for r2, c2 in dir_]:
                        if 0 <= ny < R and 0 <= nx < C and grid[ny][nx] == '1':
                            grid[ny][nx] = '0'
                            q.append([ny, nx])
        return res