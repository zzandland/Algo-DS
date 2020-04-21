class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                if y == 0 and x == 0: continue
                top = float('inf') if y == 0 else grid[y-1][x]
                left = float('inf') if x == 0 else row[x-1]
                grid[y][x] += min(top, left)
        return grid[-1][-1]        