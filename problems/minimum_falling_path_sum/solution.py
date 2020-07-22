class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        N = len(A)
        dp = [0]*N
        for y in range(N):
            ndp = [0]*N
            for x in range(N):
                ndp[x] = min(dp[k] for k in range(max(0, x-1), min(N, x+2))) + A[y][x]
            dp = ndp
        return min(dp)