class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort()
        N, t, output = len(intervals), intervals[0], []
        for i in range(1, N):
            if intervals[i][0] > t[1]: 
                output.append(t)
                t = intervals[i]
            else: t = [min(t[0], intervals[i][0]), max(t[1], intervals[i][1])]
        return output + [t]        