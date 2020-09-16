class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dp = [(1, 0)]
        exp = 1
        sign = not ((dividend > 0) ^ (divisor > 0))
        dividend, divisor = abs(dividend), abs(divisor)
        if dividend < divisor: return 0
        while divisor <= dividend:
            if divisor == dividend: return min((1 << 31) - 1, exp) if sign else (~exp) + 1
            dp.append((divisor, exp))
            divisor <<= 1
            exp <<= 1
        res = 0
        idx = len(dp)
        while dividend > 0:
            idx = bisect.bisect_left(dp, (dividend+1,), 0, idx) - 1
            if dividend < dp[idx][0]: break
            res += dp[idx][1]
            dividend -= dp[idx][0]
        return res if sign else (~res) + 1