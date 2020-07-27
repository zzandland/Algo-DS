class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        dp = [False]*N
        res = ''
        for y in range(N-1, -1, -1):
            ndp = [False]*N
            ndp[y] = True
            res = max(res, s[y], key=len)
            for x in range(y+1, N):
                if s[y] == s[x]:
                    if dp[x-1] or x-y == 1:
                        ndp[x] = True
                        res = max(res, s[y:x+1], key=len)
            dp = ndp
        return res