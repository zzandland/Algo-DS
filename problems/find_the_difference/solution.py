from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = Counter(s)
        for c in t:
            freq[c] -= 1
            if freq[c] == 0: del freq[c]
        return list(freq.keys())[0]