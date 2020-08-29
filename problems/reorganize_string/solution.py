from collections import Counter
from heapq import heappush, heappop, heapify

class Solution:
    def reorganizeString(self, S: str) -> str:
        c = Counter(S)
        # make max heap
        q = [(-cnt, n) for n, cnt in c.items()]
        heapify(q)
        st = []
        res = []
        while q:
            while st and res[-1] != st[-1]:
                res.append(st.pop())
            cnt, n = heappop(q)
            if cnt < -1: heappush(q, (cnt+1, n))
            if not res or res[-1] != n: res.append(n)
            else: st.append(n)
        
        while st and res[-1] != st[-1]:
            res.append(st.pop())
        return ''.join(res) if not st else ''