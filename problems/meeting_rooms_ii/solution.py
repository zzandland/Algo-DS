class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        changes = []
        for i, j in intervals:
            changes.append((i, 1))
            changes.append((j, -1))
        changes.sort()
        curr = res = 0
        for _, change in changes:
            curr += change
            res = max(res, curr)
        return res