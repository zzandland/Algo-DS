class Solution:
    def confusingNumber(self, N: int) -> bool:
        strom = {'0' : '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        s = str(N)
        if any([c not in strom for c in s]): return False
        l, r = 0, len(s)-1
        while l <= r:
            lc, rc = s[l], s[r]
            if strom[lc] != rc or strom[rc] != lc: return True
            l += 1
            r -= 1
        return False