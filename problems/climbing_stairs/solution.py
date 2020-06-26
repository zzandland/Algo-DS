class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1] + [None]*(n-1)
        def fn(i: int) -> int:
            if dp[i] == None:
                dp[i] = fn(i-1) + fn(i-2)
            return dp[i]
        return fn(n)