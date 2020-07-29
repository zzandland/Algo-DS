class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = (2 << 30) - 1
        INT_MIN = ~INT_MAX
        str = str.strip()
        if not str: return 0
        minus = False
        if str[0] == '-':
            minus = True
            str = str[1:]
        elif str[0] == '+':
            minus = False
            str = str[1:]
        res = 0
        for c in str:
            if not c.isdigit(): break
            res += int(c)
            res *= 10
        res //= 10
        if not minus: return min(INT_MAX, res)
        res *= -1
        return max(INT_MIN, res)