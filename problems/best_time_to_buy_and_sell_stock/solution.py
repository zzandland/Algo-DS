class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, mx, P = 0, float('-inf'), len(prices)
        for i in range(P-1, -1, -1):
            res = max(res, mx-prices[i])
            mx = max(mx, prices[i])
        return res    