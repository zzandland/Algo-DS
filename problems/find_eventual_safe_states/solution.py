from collections import defaultdict, deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        outd, ind = [set(n) for n in graph], [[] for _ in range(N)]
        for i, n in enumerate(graph):
            for j in n:
                ind[j].append(i)
        q = deque([i for i, n in enumerate(graph) if not n])
        res = []
        while q:
            n = q.popleft()
            res.append(n)
            for nn in ind[n]:
                outd[nn].remove(n)
                if not outd[nn]:
                    q.append(nn)
        return sorted(res)