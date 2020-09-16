from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        t = Counter(p)
        
        N = len(p)
        roll = Counter()
        res = []
        for i, c in enumerate(s):
            if i >= N:
                roll[s[i-N]] -= 1
                if not roll[s[i-N]]: del roll[s[i-N]]
            roll[s[i]] += 1
            if t == roll: res.append(i-N+1)
        return res