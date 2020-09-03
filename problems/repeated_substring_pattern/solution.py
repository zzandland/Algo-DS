class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) < 2: return False
        N = len(s)
        for i in range(int(N**0.5), 0, -1):
            if N % i == 0:
                tmp = [i]
                if i != 1: tmp.append(N//i)
                for l in tmp:
                    t = hash(s[:l])
                    for j in range(l, N, l):
                        if t != hash(s[j:j+l]): break
                    else: return True
        return False