from collections import deque

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        # create prefix of A n(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)
            
        # monotonically increasing deque
        res = float('inf')
        q = deque()
        for y, p in enumerate(P):
            # any prev left candidate whose prefix is greater than
            # cur prefix sum can be popped
            while q and p <= P[q[-1]]:
                q.pop()
                
            # if cur prefix - first prefix >= K, we don't need to consider
            # the first index again so popleft
            while q and p - P[q[0]] >= K:
                res = min(res, y-q.popleft())
                
            q.append(y)
            
        return res if res != float('inf') else -1