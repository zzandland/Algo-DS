class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n > m: m, n = n, m
        dp = [1] + [0]*(m-1)
        for _ in range(n):
            for j in range(1, m):
                dp[j] += dp[j-1]
        return dp[-1]        