class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for a in range(1, n+1):
            dp[0][a] = dp[0][a-1] + ord(s2[a-1])
        for b in range(1, m+1):
            dp[b][0] = dp[b-1][0] + ord(s1[b-1])
        for y in range(1, m+1):
            for x in range(1, n+1):
                if s1[y-1] == s2[x-1]:
                    dp[y][x] = dp[y-1][x-1]
                else:
                    dp[y][x] = min(ord(s1[y-1]) + dp[y-1][x],
                                   ord(s2[x-1]) + dp[y][x-1])
        return dp[m][n]