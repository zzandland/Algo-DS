class Solution:
    def numSquares(self, n: int) -> int:
        sqs, idx = [], 1
        while idx*idx <= n:
            sqs.append(idx*idx)
            idx += 1
        dp = [0] + [float('inf')]*(n)
        for sq in sqs:
            for i in range(sq, n+1):
                dp[i] = min(dp[i], 1 + dp[i-sq])
        return dp[n]