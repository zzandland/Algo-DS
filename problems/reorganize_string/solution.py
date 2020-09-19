from collections import Counter
from heapq import heapify, heappush, heappop

class Solution:
    def reorganizeString(self, S: str) -> str:
        freq = Counter(S)
        q = [(-cnt, c) for c, cnt in freq.items()]
        st = []
        heapify(q)
        res = []
        while q:
            if st and res[-1] != st[-1][1]: cnt, c = st.pop()
            else: cnt, c = heappop(q)
            res.append(c)
            if cnt < -1:
                if not st: st.append((cnt+1, c))
                else: heappush(q, (cnt+1, c))
        if st:
            cnt, c = st.pop()
            if cnt < -1: return ''
            else: res.append(c)
        return ''.join(res)