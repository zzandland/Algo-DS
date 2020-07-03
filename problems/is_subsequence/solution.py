class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in t:
            if i == len(s): return True
            if s[i] == c: i += 1
        return i == len(s)