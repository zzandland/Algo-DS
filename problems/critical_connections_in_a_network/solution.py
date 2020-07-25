from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # adj list of edges O(connections)
        adj = defaultdict(set)
        for u, v in connections:
            adj[u].add(v)
            adj[v].add(u)
        
        # dfs to label group that each node belongs to O(V+E)
        label = [-1]*n
        group = [-1]*n
        cnt = 0
        res = []
        def dfs(i: int, p: int) -> None:
            nonlocal cnt
            label[i] = group[i] = cnt
            cnt += 1
            for ni in adj[i]:
                if ni != p:
                    if label[ni] == -1: dfs(ni, i)
                    group[i] = min(group[i], group[ni])
                    if label[i] < group[ni]: res.append([i, ni])
        dfs(0, -1)
        
        return res