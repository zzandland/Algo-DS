class Solution:
    def numDecodings(self, s: str) -> int:
        S = len(s)
        if not s or s[0] == '0': return 0
        if S < 2: return S
        c1, c2 = 1, 1
        for i in range(1, S):
            val = int(s[i-1]+s[i])
            if s[i] == '0':
                if val > 26: return 0
                else: c3, c2 = c1, 0
            elif val < 27: c3 = c1+c2
            else: c3 = c2    
            c1, c2 = c2, c3    
        return c3    