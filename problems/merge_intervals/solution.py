class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            s1, e1 = res[-1]
            s2, e2 = intervals[i]
            if e1 >= s2: res[-1] = [min(s1, s2), max(e1, e2)]
            else: res.append([s2, e2])
        return res