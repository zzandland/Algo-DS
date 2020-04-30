class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        ds, dp = set(days), [0 for _ in range(days[-1]+1)]
        for i in range(1, days[-1]+1):
            a, b, c = i-1 if i-1 >= 0 else 0, i-7 if i-7 >= 0 else 0, i-30 if i-30 >= 0 else 0
            if i in ds: dp[i] = min(costs[0]+dp[a], costs[1]+dp[b], costs[2]+dp[c])
            else: dp[i] = dp[i-1]
        return dp[-1]        