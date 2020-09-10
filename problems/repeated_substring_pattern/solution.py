class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        N = len(s)
        for i in range(N//2, 0, -1):
            if N % i == 0:
                t = hash(s[:i])
                tmp = [i]
                for j in range(i, N, i):
                    if t != hash(s[j:j+i]): break
                else: return True
        return False