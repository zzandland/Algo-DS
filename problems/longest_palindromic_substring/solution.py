class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False for _, _ in enumerate(s)] for _, _ in enumerate(s)]
        for i, _ in enumerate(s):
            dp[i][i] = True
        max_len, max_coord = 0, (0, 0)
        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    new_len = j - i + 1
                    if new_len == 2 or dp[i + 1][j - 1]:
                        if new_len > max_len:
                            max_len = new_len
                            max_coord = (i, j)
                        dp[i][j] = True
        return s[max_coord[0]: max_coord[1] + 1]            