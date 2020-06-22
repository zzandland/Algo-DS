class Solution:
    def numTrees(self, n: int) -> int:
        if n < 2:
            return 1
        dp = [1, 1] + [0]*(n-1)
        for i in range(2, n+1):
            dp[i] = sum([dp[j] * dp[i-j-1] for j in range(i)])
        return dp[-1]