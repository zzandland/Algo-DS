class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = res = mxcnt = 0
        c = Counter()
        for r in range(len(s)):
            c[s[r]] += 1
            mxcnt = max(mxcnt, c[s[r]])
            while r - l + 1 - mxcnt > k:
                c[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res