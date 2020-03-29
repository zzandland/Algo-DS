from collections import defaultdict
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        for task in tasks:
            d[task] -= 1
        q = list(d.values())
        heapq.heapify(q)
        t = 0
        while q:
            tmp = []
            for i in range(n+1):
                t += 1
                if q:
                    j = heapq.heappop(q)
                    if j+1 < 0: tmp.append(j+1)
                if not tmp: break
            for task in tmp:
                heapq.heappush(q, task)    
        return t