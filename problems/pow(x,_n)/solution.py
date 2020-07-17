class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        dp = {}
        def dq(i: int) -> float:
            if i == 1:
                return x
            if i == -1:
                return 1/x
            if i not in dp:
                if i % 2 == 1:
                    dp[i] = dq(i//2) * dq(i//2+1)
                else:
                    dp[i] = dq(i//2) * dq(i//2)
            return dp[i]
        return dq(n)