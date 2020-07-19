class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        N, K = len(prices), 2
        # dp array of n cols and k rows
        dp = [[0]*(N+1) for _ in range(K+1)]
        for k in range(1, K+1):
            mx = -prices[0]
            for i in range(2, N+1):
                mx = max(mx, dp[k-1][i-2] - prices[i-2])
                dp[k][i] = max(dp[k-1][i], dp[k][i-1], prices[i-1] + mx)
        return dp[-1][-1]