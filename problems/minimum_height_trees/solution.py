from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        ind, adj, rem = [0]*n, defaultdict(set), set(range(n))
        for u, v in edges:
            ind[u] += 1
            ind[v] += 1
            adj[u].add(v)
            adj[v].add(u)
        q, nq = set([i for i in range(n) if ind[i] == 1]), set()
        while len(rem) > 2:
            rem -= q
            for i in q:
                for ni in list(adj[i]):
                    ind[ni] -= 1
                    if ind[ni] == 1:
                        nq.add(ni)
                        adj[i].remove(ni)
                        adj[ni].remove(i)
            q, nq = nq, set()
        return q    