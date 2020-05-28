import heapq

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        heapq.heapify(intervals)
        res = []
        while intervals:
            i, j = heapq.heappop(intervals)
            if not res:
                res.append([i, j])
            elif i <= res[-1][1]: res[-1][1] = max(j, res[-1][1])
            else: res.append([i, j])
        return res        