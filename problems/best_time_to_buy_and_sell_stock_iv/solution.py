class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        
        N = len(prices)
        
        if N//2 < k: 
            res = 0
            for a, b in zip(prices, prices[1:]):
                res += max(0, b - a)
            return res
        
        dp = [[0]*N for _ in range(k+1)]
        
        # 6 1 6 4 3 0 2
        # 0 0 5 5 5 5 
        
        for i in range(1, k+1):
            dp[i][1] = max(0, prices[1] - prices[0])
            mx = -prices[0]
            for j in range(2, N):
                mx = max(mx, dp[i-1][j-2] - prices[j-1])
                dp[i][j] = max(dp[i][j-1], prices[j] + mx)
        return dp[-1][-1]