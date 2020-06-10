class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        dp = [0]*N
        for i in range(N):
            for j in range(max(0, i-K+1), i+1):
                dp[i] = max(dp[i], max(A[j:i+1])*(i-j+1)+dp[j-1])
        return dp[-1]