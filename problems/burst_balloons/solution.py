class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        p = 1
        mat = []
        for n in nums:
            mat.append((p, n))
            p = n
        mat.append((p, 1))
        N = len(mat)
        dp = [[0]*N for _ in range(N)]
        for i in range(1, N):
            for j in range(N-i):
                l, r = j, j+i
                res = 0
                for k in range(l, r):
                    res = max(res, dp[l][k] + dp[k+1][r] + mat[l][0] * mat[k][1] * mat[r][1])
                dp[l][r] = res

        return dp[0][-1]