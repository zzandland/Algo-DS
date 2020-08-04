class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries: return 0
        res = duration
        for a, b in zip(timeSeries, timeSeries[1:]):
            res += min(b-a, duration)
        return res