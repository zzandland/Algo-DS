class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for a in range(len(s)):
            dp[a][a] = True
        max_len, coord = 1, (0, 0)    
        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if j - i + 1 > max_len:
                            max_len = j - i + 1
                            coord = (i, j)
        return s[coord[0]:coord[1] + 1]                