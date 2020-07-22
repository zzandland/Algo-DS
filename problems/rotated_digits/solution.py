from collections import Counter

class Solution:
    def rotatedDigits(self, N: int) -> int:
        res = 0
        for i in range(1, N+1):
            tmp = res
            c = set(list(str(i)))
            # 3, 4, 7 are invalid
            if '3' in c or '4' in c or '7' in c: continue
            # 2, 5 must be just by themselves
            if '2' in c and '6' not in c and '9' not in c: res += 1
            elif '5' in c and '6' not in c and '9' not in c: res += 1
            elif '6' in c or '9' in c: res += 1
        return res