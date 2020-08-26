class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        sy, sx = points[0]
        for ty, tx in points[1:]:
            y, x = abs(ty-sy), abs(tx-sx)
            diag = min(y, x)
            res += y + x - diag
            sy, sx = ty, tx
        return res