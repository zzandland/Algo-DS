from collections import defaultdict

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        cols, lasty, mn = defaultdict(list), {}, float('inf')
        for y, x in points: cols[y].append(x)
        for y, row in sorted(cols.items()):
            row.sort()
            for i, x2 in enumerate(row):
                for j in range(i):
                    x1 = row[j]
                    if (x1, x2) in lasty: mn = min(mn, (x2-x1) * (y-lasty[(x1, x2)]))
                    lasty[(x1, x2)] = y    
        return mn if mn != float('inf') else 0