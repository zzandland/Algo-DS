from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # adj list O(con)
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        # strongly connected components O(V+E)
        id_ = 0
        A = [None]*n
        B = [0]*n
        def dfs(i: int, p: int) -> int:
            nonlocal id_
            if A[i] != None:
                B[i] = min(B[i], B[p])
                return B[i]
            A[i] = B[i] = id_
            id_ += 1
            for ni in adj[i]:
                if ni != p: 
                    bni = dfs(ni, i)
                    B[i] = min(B[i], bni)
            return B[i]
        dfs(0, -1)
        res = set()
        for i in range(n):
            for ni in adj[i]:
                if B[i] != B[ni]: res.add(tuple(sorted([i, ni])))
        return list(res)