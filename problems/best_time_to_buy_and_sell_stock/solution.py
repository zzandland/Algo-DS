class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = float('inf')
        res = 0
        for p in prices:
            mn = min(mn, p)
            res = max(res, p - mn)
        return res