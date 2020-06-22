class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for a in range(1, n+1):
            dp[0][a] = dp[0][a-1] + 1
        for b in range(1, m+1):
            dp[b][0] = dp[b-1][0] + 1
        for y in range(1, m+1):
            for x in range(1, n+1):
                if word1[y-1] == word2[x-1]:
                    dp[y][x] = dp[y-1][x-1]
                else:
                    dp[y][x] = 1 + min(dp[y-1][x], dp[y][x-1])
        return dp[m][n]