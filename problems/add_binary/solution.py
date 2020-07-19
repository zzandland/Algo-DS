class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j = len(a)-1, len(b)-1
        lft = 0
        while i >= 0 or j >= 0:
            ab = int(a[i]) if i >= 0 else 0
            bb = int(b[j]) if j >= 0 else 0
            val = ab + bb + lft
            if val >= 2:
                val -= 2
                lft = 1
            else: lft = 0
            res.append(str(val))
            i -= 1
            j -= 1
        if lft: res.append(str(lft))
        return ''.join(res[::-1])