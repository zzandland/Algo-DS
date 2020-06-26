class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        t = self.myPow(x, n//2 if n > 0 else ceil(n/2));
        if n % 2: return 1/x*t*t if n < 0 else x*t*t
        return t*t