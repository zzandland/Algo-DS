class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp, out = [[False for _ in range(len(s))] for _ in range(len(s))], ''
        for i in range(len(s)):
            dp[i][i] = True
            out = s[i]
        for c in range(1, len(s)):
            for r in range(c-1, -1, -1):
                if s[r] == s[c] and (dp[r+1][c-1] or c-r == 1):
                    dp[r][c] = True
                    if c-r+1 > len(out): out = s[r:c+1]
        return out        