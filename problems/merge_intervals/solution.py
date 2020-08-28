class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort()
        res = [intervals[0]]
        for u, v in intervals[1:]:
            if res[-1][1] < u: res.append([u, v])
            else: res[-1][1] = max(res[-1][1], v)
        return res