class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort()
        s1, e1 = intervals[0]
        res = 0
        for s2, e2 in intervals[1:]:
            if e1 <= s2:
                s1, e1 = s2, e2
            elif e1 > e2:
                s1, e1 = s2, e2
                res += 1
            else:
                res += 1
        return res