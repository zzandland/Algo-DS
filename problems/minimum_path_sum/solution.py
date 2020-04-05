class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        directions, dp = [(-1, 0), (0, -1)], [[0 for _ in range(len(row))] for row in grid]
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if y > 0 and x > 0: dp[y][x] = min(dp[y-1][x], dp[y][x-1])
                elif y > 0: dp[y][x] = dp[y-1][x]
                elif x > 0: dp[y][x] = dp[y][x-1]
                dp[y][x] += cell
        return dp[len(grid)-1][len(grid[0])-1]