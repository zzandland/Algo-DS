import functools

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(startTime)
        tmp = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [(0, 0)]
        
        for s, e, p in tmp:
            idx = bisect.bisect_left(dp, (s+1,))-1
            if dp[idx][1] + p > dp[-1][1]: dp.append((e, dp[idx][1] + p))
        return dp[-1][1]