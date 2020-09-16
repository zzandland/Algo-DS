from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = Counter()
        res = l = 0
        for r, c in enumerate(s):
            freq[c] += 1
            while freq[c] > 1:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l +1)
        return res