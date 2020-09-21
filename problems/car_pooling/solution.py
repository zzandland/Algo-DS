class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        intervals = []
        for cnt, s, e in trips:
            intervals.append((s, cnt))
            intervals.append((e, -cnt))
        intervals.sort()
        cnt = 0
        for _, change in intervals:
            cnt += change
            if cnt > capacity: return False
        return True