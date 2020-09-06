from collections import Counter

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        N = len(A)
        
        al, bl = [], []
        for y in range(N):
            for x in range(N):
                if A[y][x] == 1: al.append((y, x))
                if B[y][x] == 1: bl.append((y, x))
                    
        freq = Counter()
        for ay, ax in al:
            for by, bx in bl:
                freq['%d %d' % (ay-by, ax-bx)] += 1
        
        return max(freq.values() or [0])