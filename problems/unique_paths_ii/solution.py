class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(row))] for row in obstacleGrid]
        for y, row in enumerate(obstacleGrid):
            for x, col in enumerate(row):
                if col != 1:
                    if y == 0 and x == 0: 
                        dp[y][x] = 1
                    else:
                        top = 0 if y <= 0 else dp[y-1][x]
                        left = 0 if x <= 0 else dp[y][x-1]
                        dp[y][x] = top + left
        return dp[len(dp)-1][len(dp[0])-1]