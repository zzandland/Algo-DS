class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, lft, res = len(a)-1, len(b)-1, 0, []
        while i >= 0 or j >= 0:
            av = int(a[i]) if i >= 0 else 0
            bv = int(b[j]) if j >= 0 else 0
            tmp = av + bv + lft
            lft = tmp // 2
            res.append(str(tmp % 2))
            i, j = i-1, j-1
        if lft == 1: res.append('1')
        return ''.join(res[::-1])