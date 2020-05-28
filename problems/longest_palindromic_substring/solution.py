class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        S, mx = len(s), s[0]
        dp = [0]*S
        for i in range(S-1, -1, -1):
            for j in range(S-1, i, -1):
                if s[i] == s[j] and dp[j-1] == j-i-1:
                    dp[j] = dp[j-1] + 2
                    mx = max(mx, s[i:j+1], key=lambda x: len(x))
                else: dp[j] = 0
            dp[i] = 1
        return mx    