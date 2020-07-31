from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen_c = Counter()
        c2idx = {}
        for i, c in enumerate(s):
            seen_c[c] += 1
            if seen_c[c] == 1: c2idx[c] = i
            elif seen_c[c] > 1 and c in c2idx: del c2idx[c]
        return min(c2idx.values()) if c2idx else -1