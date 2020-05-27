class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        pos = True
        if dividend == (-1<<31) and divisor == -1: return (1<<31) - 1
        if dividend < 0 or divisor < 0: pos = False
        if dividend < 0 and divisor < 0: pos = True
        a, b, i = abs(dividend), abs(divisor), 0
        while a >= b:
            t, n = b, 1
            while t<<1 <= a:
                t <<= 1
                n <<= 1
            a -= t
            i += n
        return i * (1 if pos else -1)