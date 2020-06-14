class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [0] + [1 if i <= f else 0 for i in range(1, target+1)]
        for _ in range(d-1):
            for i in range(target, 0, -1):
                dp[i] = sum([dp[j] for j in range(max(0, i-f), i)])
        return dp[target] % (10**9+7)