class Solution:
    def numSquares(self, n: int) -> int:
        sqs = []
        i = 2
        while i*i <= n:
            sqs.append(i*i)
            i += 1
        dp = list(range(n+1))
        for sq in sqs:
            for i in range(sq, n+1):
                dp[i] = min(dp[i], dp[i - sq] + 1)
        return dp[-1]