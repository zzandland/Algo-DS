class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = Counter()
        res = 0
        for r, c in enumerate(s):
            seen[c] += 1
            while seen[c] > 1:
                seen[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res