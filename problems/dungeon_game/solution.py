class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        R, C = len(dungeon), len(dungeon[0])
        dp = [[float('inf')]*(C+1) for _ in range(R+1)]
        dp[R][C-1] = dp[R-1][C] = 1
        for y in range(R-1, -1, -1):
            for x in range(C-1, -1, -1):
                dp[y][x] = max(1, min(dp[y+1][x], dp[y][x+1]) - dungeon[y][x])
        return dp[0][0]