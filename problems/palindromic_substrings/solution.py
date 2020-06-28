class Solution:
    def countSubstrings(self, s: str) -> int:
        res, N = 0, len(s)
        dp = [[False]*N for _ in range(N)]
        for y in range(N-1, -1, -1):
            dp[y][y] = True
            res += 1
            for x in range(y+1, N):
                dp[y][x] = s[y] == s[x] and (dp[y+1][x-1] or x-y == 1)
                if dp[y][x]: res += 1
        return res