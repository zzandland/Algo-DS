import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x: x[0])
        q = [intervals[0][1]]
        for i in range(1, len(intervals)):
            s1, e1 = intervals[i]
            e2 = heapq.heappop(q)
            if e2 > s1: heapq.heappush(q, e2)
            heapq.heappush(q, e1)    
        return len(q)    