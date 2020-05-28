class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1    
        pos, i, res = True, 0, 1
        if n < 0: pos, n = False, n*-1
        while n > 0:
            i, tmp = 1, x
            while i*2 <= n:
                tmp *= tmp
                i *= 2
            n, res = n-i, res*tmp
        return res if pos else 1/res