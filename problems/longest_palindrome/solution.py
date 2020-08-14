class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        res = 0
        odd = False
        for f in freq.values():
            if f & 1 == 1: odd = True
            res += f&(~1)
        return res + int(odd)
    