import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda interval: interval[0])
        hp = []
        heapq.heappush(hp, intervals[0][1])
        for interval in intervals[1:]:
            if hp[0] <= interval[0]:
                heapq.heappop(hp)
            heapq.heappush(hp, (interval[1]))
        return len(hp)    