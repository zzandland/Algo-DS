class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ""
        S, mx = len(s), s[0]
        dp = [0]*(S-1) + [1]
        for r in range(S-1, -1, -1):
            for c in range(S-1, r, -1):
                if s[r] == s[c] and dp[c-1] == c-r-1:
                    dp[c] = 2 + dp[c-1]
                    mx = max(mx, s[c-dp[c]+1:c+1], key=lambda x: len(x))    
            dp[r] = 1       
        return mx        