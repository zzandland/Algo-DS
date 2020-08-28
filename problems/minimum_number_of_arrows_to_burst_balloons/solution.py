class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort()
        res = [points[0]]
        for u, v in points[1:]:
            tu, tv = res[-1]
            if tv < u: res.append([u, v])
            else: res[-1] = [max(tu, u), min(tv, v)]
        return len(res)