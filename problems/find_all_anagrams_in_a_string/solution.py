from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        t = Counter(p)
        run = Counter()
        N = len(p)
        res = []
        for i, c in enumerate(s):
            if i >= N:
                run[s[i-N]] -= 1
                if run[s[i-N]] == 0: del run[s[i-N]]
            run[c] += 1
            if run == t: res.append(i-N+1)
        return res