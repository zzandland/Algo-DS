class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        stro = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        l, r = 0, len(num)-1
        while l <= r:
            lc, rc = num[l], num[r]
            if lc not in stro or rc not in stro: return False
            if stro[lc] != rc or stro[rc] != lc: return False
            l += 1
            r -= 1
        return True