class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        ps = set([(y, x) for y, x in points])
        res = float('inf')
        for i, (y1, x1) in enumerate(points):
            for j in range(i):
                y2, x2 = points[j]
                if y1 != y2 and x1 != x2:
                    if (y2, x1) in ps and (y1, x2) in ps:
                        res = min(res, abs(y2-y1) * abs(x2-x1))
        return res if res != float('inf') else 0