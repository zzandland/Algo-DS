class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        st = set(map(tuple, points))
        res = float('inf')
        for i, (y1, x1) in enumerate(points):
            for j in range(i+1, len(points)):
                y2, x2 = points[j]
                if y1 == y2 or x1 == x2: continue
                if (y2, x1) in st and (y1, x2) in st:
                    res = min(res, abs(y2-y1)*abs(x2-x1))
        return res if res != float('inf') else 0