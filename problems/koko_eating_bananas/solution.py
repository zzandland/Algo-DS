class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l, r = 1, sum(piles)
        while l < r:
            m = l + (r-l)//2
            hr = 0
            for n in piles:
                hr += ceil(n / m) 
            if hr > H: l = m+1
            else: r = m
        return l