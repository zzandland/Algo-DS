class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse=True)
        res = d = 0
        q = []
        while q or events:
            if not q: d = events[-1][0]
            while events and events[-1][0] <= d:
                heappush(q, events.pop()[1])
            heappop(q)
            res += 1
            d += 1
            while q and q[0] < d: heappop(q)
        return res