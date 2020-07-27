class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        M, N = len(grid), len(grid[0])
        dp = [[float('inf')]*(N+1) for _ in range(M+1)]
        dp[0][1] = dp[1][0] = 0
        for y in range(1, M+1):
            for x in range(1, N+1):
                dp[y][x] = min(dp[y-1][x], dp[y][x-1]) + grid[y-1][x-1]
        return dp[-1][-1]