class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res, a, b, lft = [], len(num1)-1, len(num2)-1, 0
        while a >= 0 or b >= 0:
            v1 = v2 = 0
            if a >= 0:
                v1 = int(num1[a])
                a -= 1
            if b >= 0:
                v2 = int(num2[b])
                b -= 1
            tmp = v1 + v2 + lft
            if tmp > 9:
                tmp -= 10
                lft = 1
            else:
                lft = 0
            res.append(str(tmp))
        if lft: res.append(str(lft))
        return ''.join(res[::-1])