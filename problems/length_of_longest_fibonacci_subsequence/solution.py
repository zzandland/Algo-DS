from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        N = len(A)
        idx = {n: i for i, n in enumerate(A)}
        dp = defaultdict(lambda: 2)
        res = 0
        for i in range(N):
            for j in range(i):
                if A[i] - A[j] < A[j] and A[i] - A[j] in idx:
                    dp[A[j], A[i]] = dp[A[i]-A[j], A[j]] + 1
                    res = max(res, dp[A[j], A[i]])
        return res if res > 2 else 0