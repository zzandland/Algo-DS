class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        N = len(prices)
        if k >= N//2:
            res = 0
            for prev, nxt in zip(prices, prices[1:]):
                if nxt > prev: res += nxt - prev
            return res
        dp = [[0]*(N+1) for _ in range(k+1)]
        for r in range(1, k+1):
            mx = -prices[0]
            for i in range(2, N+1):
                mx = max(mx, dp[r-1][i-2] - prices[i-2])
                dp[r][i] = max(dp[r][i-1], mx + prices[i-1])
        return dp[-1][-1]