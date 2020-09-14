class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        dp = [1, 1]
        while dp[-1] < k:
            dp.append(dp[-1] + dp[-2])
        res = 0
        while k > 0:
            res += 1
            idx = bisect.bisect_left(dp, k+1) - 1
            k -= dp[idx]
        return res
