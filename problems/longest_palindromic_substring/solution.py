class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        N, res = len(s), s[0]
        dp = [[False]*N for _ in range(N)]
        for y in range(N-1, -1, -1):
            dp[y][y] = True
            for x in range(y+1, N):
                if s[y] == s[x]:
                    if dp[y+1][x-1] or x-y == 1:
                        dp[y][x] = True
                        if len(res) < x-y+1:
                            res = s[y:x+1]
        return res                