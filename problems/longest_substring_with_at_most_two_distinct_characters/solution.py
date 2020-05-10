from collections import Counter

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        c, j, mx = Counter(), 0, 0
        for i, sc in enumerate(s):
            c[sc] += 1
            while len(c) > 2:
                c[s[j]] -= 1
                if c[s[j]] == 0: del c[s[j]]
                j += 1
            mx = max(mx, i-j+1)
        return mx        