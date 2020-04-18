import heapq

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        heapq.heapify(intervals)
        output, cur = [], heapq.heappop(intervals)
        while intervals:
            nxt = heapq.heappop(intervals)
            if cur[1] >= nxt[0]:
                cur = [cur[0], nxt[1]] if cur[1] < nxt[1] else [cur[0], cur[1]]
            else:
                output.append(cur)    
                cur = nxt
        return output + [cur]     