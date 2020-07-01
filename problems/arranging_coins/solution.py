class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n < 2: return n
        l, r = 0, n
        while l < r:
            m = l + (r-l)//2
            if (m*(m+1))//2 > n: r = m
            else: l = m+1
        return l - 1