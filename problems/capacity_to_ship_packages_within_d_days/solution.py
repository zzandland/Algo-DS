class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            m = l + (r-l)//2
            days, cur = 1, 0
            for w in weights:
                if cur + w > m:
                    days += 1
                    cur = w
                else: cur += w
            if days > D: l = m+1
            else: r = m
        return l