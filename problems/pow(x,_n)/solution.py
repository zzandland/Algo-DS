class Solution:
    def __init__(self):
        self.dp = {}
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n == 1: return x
        if n == -1: return 1/x
        if (x, n) not in self.dp:
            if n & 1 == 1:
                self.dp[x, n] = self.myPow(x, n//2) * self.myPow(x, n//2+1)
            else:
                self.dp[x, n] = self.myPow(x, n//2) * self.myPow(x, n//2)
        return self.dp[x, n]