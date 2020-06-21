class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        dp = [0]*(N+1)
        for i in range(N):
            for j in range(max(-1, i-K), i):
                dp[i+1] = max(dp[i+1], dp[j+1] + max(A[j+1:i+1])*(i-j))
        return dp[-1]