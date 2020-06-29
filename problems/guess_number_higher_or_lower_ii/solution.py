class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0]*n for _ in range(n)]
        for l in range(n, 0, -1):
            for r in range(l+1, n+1):
                if r-l == 1:
                    dp[l-1][r-1] = l
                else:
                    dp[l-1][r-1] = min([m + max(dp[l-1][m-2], dp[m][r-1]) for m in range(l+1, r)])
        return dp[0][-1]