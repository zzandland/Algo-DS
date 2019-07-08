class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        hp = [(intervals[0][1], intervals[0])]
        for i in range(1, len(intervals)):
            inter = intervals[i]
            end, curr = heapq.heappop(hp)
            if end <= inter[0]:
                curr[1] = inter[1]
            else:
                heapq.heappush(hp, (inter[1], inter))
            heapq.heappush(hp, (curr[1], curr))
        return len(hp)    