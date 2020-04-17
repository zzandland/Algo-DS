import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        hp = []
        for start, end in sorted(intervals, key=lambda x: x[0]):
            if hp:
                minEnd = heapq.heappop(hp)
                if minEnd > start: heapq.heappush(hp, minEnd)
            heapq.heappush(hp, end)    
        return len(hp)        