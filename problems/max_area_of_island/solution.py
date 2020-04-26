class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        R, C = len(grid), len(grid[0])
        def dfs(y: int, x: int) -> int:
            grid[y][x], output = 0, 1
            for r, c in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ny, nx = y+r, x+c
                if 0 <= ny < R and 0 <= nx < C and grid[ny][nx] == 1:
                    output += dfs(ny, nx)
            return output        
        return max([0 if grid[y][x] == 0 else dfs(y, x) for y in range(R) for x in range(C)])