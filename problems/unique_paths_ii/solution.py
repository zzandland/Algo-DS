class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid: return 0
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*(N+1) for _ in range(M+1)]
        dp[1][0] = 1
        for y in range(1, M+1):
            for x in range(1, N+1):
                if obstacleGrid[y-1][x-1] == 0:
                    dp[y][x] = dp[y-1][x] + dp[y][x-1]
        return dp[-1][-1]