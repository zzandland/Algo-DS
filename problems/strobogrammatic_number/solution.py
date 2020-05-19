class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if not num: return True
        l, r = 0, len(num)-1
        nt = ('2', '3', '4', '5', '7')
        while l < r:
            if num[l] in nt or num[r] in nt: return False
            if num[l] == '6' and num[r] != '9': return False
            if num[l] == '9' and num[r] != '6': return False
            if num[l] == '0' and num[r] != '0': return False
            if num[l] == '1' and num[r] != '1': return False
            if num[l] == '8' and num[r] != '8': return False
            l, r = l+1, r-1
        if l == r: return num[l] in ('0', '1', '8')    
        return True