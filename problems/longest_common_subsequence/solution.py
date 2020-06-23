class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [[0] * (N+1) for _ in range(M+1)]
        for y in range(1, M+1):
            for x in range(1, N+1):
                if text1[y-1] == text2[x-1]:
                    dp[y][x] = dp[y-1][x-1] + 1
                else:
                    dp[y][x] = max(dp[y-1][x], dp[y][x-1])
        return dp[M][N]