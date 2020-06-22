class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        dp = [[0]*(M+1) for _ in range(N+1)]
        for i in range(1, M+1):
            dp[0][i] = dp[0][i-1] + 1
        for j in range(1, N+1):    
            dp[j][0] = dp[j-1][0] + 1
        for r in range(1, N+1):
            for c in range(1, M+1):
                if word2[r-1] == word1[c-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
        return dp[N][M]