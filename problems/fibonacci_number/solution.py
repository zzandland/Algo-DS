class Solution:
    def fib(self, N: int) -> int:
        dp = [0, 1] + [None]*(N-1)
        def fn(n: int) -> int:
            if dp[n] == None:
                dp[n] = fn(n-1) + fn(n-2)
            return dp[n]
        return fn(N)