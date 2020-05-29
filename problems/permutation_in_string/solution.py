from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        A, B = len(s1), len(s2)
        if A > B or not s1: return False
        ad, bd = Counter(s1), Counter(s2[:A])
        def compare() -> bool:
            for c, f in bd.items():
                if c not in ad or ad[c] != f: return False
            return True    
        for i in range(A, B):
            if compare(): return True
            bd[s2[i]] += 1
            p = s2[i-A]
            bd[p] -= 1
            if bd[p] == 0: del bd[p]
        return compare()        