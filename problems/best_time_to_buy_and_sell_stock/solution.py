class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        mx, res, P = prices[-1], 0, len(prices)
        for i in range(P-1, -1, -1):
            res = max(res, mx - prices[i])
            mx = max(mx, prices[i])
        return res    