class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        prev = [-1, -1]
        for u, v in intervals:
            if prev[1] > u: return False
            prev = [u, v]
        return True