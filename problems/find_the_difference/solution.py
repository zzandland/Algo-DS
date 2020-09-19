from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sc, tc = Counter(s), Counter(t)
        for c in tc:
            if c not in sc or sc[c] != tc[c]: return c