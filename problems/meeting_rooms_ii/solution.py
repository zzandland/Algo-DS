from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        q = [0]
        intervals.sort()
        for u, v in intervals:
            if q[0] <= u: heappop(q)
            heappush(q, v)
        return len(q)