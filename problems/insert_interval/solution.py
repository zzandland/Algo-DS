class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        N = len(intervals)
        def bs(t: int) -> int:
            l, r = 0, N-1
            while l < r:
                m = l + (r-l)//2
                if intervals[m][1] <= t < intervals[m+1][0]:
                    return m
                if t > intervals[m][1]:
                    l = m + 1
                else:
                    r = m
            return l
        a, b = bs(newInterval[0]), bs(newInterval[1])
        if a == b == 0 and newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        if a == b == N-1 and newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]
        if newInterval[0] > intervals[a][1]:
            a += 1
        merge = [min(intervals[a][0], newInterval[0]), max(intervals[b][1], newInterval[1])]
        return intervals[:a] + [merge] + intervals[b+1:]