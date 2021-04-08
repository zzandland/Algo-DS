class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = [1] + [0] * N
        for i in range(N):
            if i > 0 and s[i-1] != '0' and int(s[i-1:i+1]) < 27:
                dp[i+1] += dp[i-1]
            if s[i] != '0':
                dp[i+1] += dp[i]
        return dp[N]