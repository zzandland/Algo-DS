from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        row, col = len(grid), len(grid[0])
        checked = [[False for _ in range(col)] for _ in range(row)]
        directions, count = [(0, 1), (0, -1), (1, 0), (-1, 0)], 0
        
        def dfs(y, x):
            if grid[y][x] == '0' or checked[y][x]: return
            checked[y][x] = True
            for r, c in directions:
                ny, nx = y+r, x+c
                if 0 <= ny < row and 0 <= nx < col:
                    dfs(y+r, x+c)
            
        for y, r in enumerate(grid):
            for x, c in enumerate(r):
                if c == '1' and not checked[y][x]:
                    count += 1
                    dfs(y, x)
        return count                        