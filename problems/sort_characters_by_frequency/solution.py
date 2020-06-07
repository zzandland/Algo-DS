from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        c, res = Counter(s), ''
        for ch, f in sorted(c.items(), key=lambda x: -x[1]):
            res += ch*f
        return res