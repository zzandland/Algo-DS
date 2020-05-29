from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        S, P, res = len(s), len(p), []
        if S < P or not p: return res
        sd, pd = Counter(s[:P]), Counter(p)
        def compare() -> bool:
            for c, f in sd.items():
                if c not in pd or pd[c] != f: return False
            return True    
        if compare(): res.append(0)
        for i in range(P, S):
            sd[s[i]] += 1
            sd[s[i-P]] -= 1
            if sd[s[i-P]] == 0: del sd[s[i-P]]
            if compare(): res.append(i-P+1)
        return res