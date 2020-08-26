from bisect import bisect as bs

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dst = set(days)
        dp = [0]*(days[-1]+1)
        for d in range(1, days[-1]+1):
            if d not in dst: dp[d] = dp[d-1]
            else:
                dp[d] = min(costs[0] + dp[d-1], costs[1] + dp[max(0, d-7)], costs[2] + dp[max(0, d-30)])
        return dp[-1]