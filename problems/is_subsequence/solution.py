class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        res = 0
        for c in t:
            if res == len(s):
                return True
            elif s[res] == c:
                res += 1
        return res == len(s)