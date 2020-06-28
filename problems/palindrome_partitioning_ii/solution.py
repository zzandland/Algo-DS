class Solution:
    def minCut(self, s: str) -> int:
        N = len(s)
        dp1, dp2 = [[None]*N for _ in range(N)], [-1]+[float('inf')]*N
        for y in range(N-1, -1, -1):
            dp1[y][y] = True
            for x in range(y+1, N):
                dp1[y][x] = s[y] == s[x] and (dp1[y+1][x-1] or x-y == 1)
        for i in range(1, N+1):
            for j in range(0, i):
                if dp1[j][i-1]: dp2[i] = min(dp2[i], 1 + dp2[j])
        return dp2[-1]