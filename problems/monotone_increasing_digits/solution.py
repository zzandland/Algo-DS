class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        s = str(N)
        h = 0
        for i in range(1, len(s)):
            if s[i] > s[i-1]: h = i
            if s[h] > s[i]:
                l = i
                break
        else: return N
        return int(s[:h] + str(int(s[h])-1) + '9'*(len(s)-h-1))