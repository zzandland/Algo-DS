class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        N = len(prices)
        dp, mns = [0]*3, [prices[0]]*3
        for i in range(1, N):
            for k in range(1, 3):
                mns[k] = min(mns[k], prices[i] - dp[k-1])
                dp[k] = max(dp[k], prices[i] - mns[k])
        return dp[-1]