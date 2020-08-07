class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        N = len(A)
        index = {n: i for i, n in enumerate(A)}
        dp = [[2]*N for _ in range(N)]
        
        res = 0
        for k, z in enumerate(A):
            for j in range(k):
                i = index.get(z - A[j], -1)
                if i != -1 and i < j:
                    dp[j][k] = dp[i][j] + 1
                    res = max(res, dp[j][k])
        return res if res >= 3 else 0