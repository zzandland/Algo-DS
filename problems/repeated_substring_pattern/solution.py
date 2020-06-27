class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        N = len(s)
        for i in range(N//2, 0, -1):
            if N % i == 0:
                for j in range(i, N, i):
                    if s[j:j+i] != s[j-i:j]: break
                else:
                    return True
        return False