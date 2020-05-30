from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        ws = [float('inf')]*(N+1)
        ws[K] = 0
        for _ in range(N):
            change = False
            for u, v, w in times:
                if ws[v] > ws[u]+w:
                    change = True
                    ws[v] = ws[u]+w
            if not change: break    
        mx = max(ws[1:])
        return mx if mx != float('inf') else -1