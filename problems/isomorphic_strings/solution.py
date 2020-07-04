from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ad, seen = {}, set()
        for i, c in enumerate(s):
            if c not in ad:
                if t[i] in seen: return False
                ad[c] = t[i]
                seen.add(t[i])
            elif ad[c] != t[i]: return False
        return True