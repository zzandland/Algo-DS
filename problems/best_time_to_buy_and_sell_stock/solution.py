class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        res = 0
        for p in prices[::-1]:
            mx = max(mx, p)
            res = max(res, mx-p)
        return res