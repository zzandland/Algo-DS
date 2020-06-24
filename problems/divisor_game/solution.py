class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [None]*1001
        for i in range(1, N+1):
            dp[i-1] = False
            for j in range(1, i):
                if i % j == 0 and not dp[i-j-1]:
                    dp[i-1] = True
                    break
        return dp[N-1]