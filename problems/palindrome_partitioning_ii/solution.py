class Solution:
    def minCut(self, s: str) -> int:
        S = len(s)
        dp = [[False]*S for _ in range(S)]
        for i in range(S-1, -1, -1):
            dp[i][i] = True
            for j in range(i+1, S):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] or j - i == 1
        
        dp2 = [-1] + [float('inf')]*S
        for i in range(S):
            for j in range(i+1):
                if dp[j][i]: dp2[i+1] = min(dp2[i+1], 1 + dp2[j])
        return dp2[-1]