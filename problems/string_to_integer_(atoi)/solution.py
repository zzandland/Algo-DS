class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s: return 0
        if not s[0].isdigit() and s[0] not in ('+', '-'): return 0
        res = []
        for c in s:
            if res and not c.isdigit(): break
            res.append(c)
        if len(res) == 1 and res[0] in ('+', '-'): return 0
        res = int(''.join(res))
        if res > 0: return min(2**31-1, res)
        return max(-2**31, res)