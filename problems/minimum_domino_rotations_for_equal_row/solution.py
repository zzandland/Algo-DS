from collections import Counter

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        c = Counter()
        for a, b in zip(A, B):
            if a == b:
                c[a] += 1
            else:
                c[a] += 1
                c[b] += 1
        mx = max(c.items(), key=lambda x: x[1])        
        if mx[1] != len(A): return -1
        ca = cb = 0
        for a, b in zip(A, B):
            if a == b and a == mx[0]: continue
            if a == mx[0]: ca += 1
            elif b == mx[0]: cb += 1
        return min(ca, cb)