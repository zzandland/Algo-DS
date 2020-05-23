class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s != t:
            for i in range(max(len(s), len(t))):
                if s[:i]+s[i+1:] == t or s == t[:i]+t[i+1:] or s[:i]+s[i+1:] == t[:i]+t[i+1:]: return True
        return False    