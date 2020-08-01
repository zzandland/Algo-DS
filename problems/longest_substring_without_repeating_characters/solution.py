from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = Counter()
        l = 0
        res = 0
        for r, c in enumerate(s):
            seen[c] += 1
            while seen[c] > 1:
                seen[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res