from typing import List
from collections import defaultdict

def critical_connections(n: int, edges: List[List[int]]) -> List[List[int]]:
    """
    >>> critical_connections(5, [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]
    [[1, 2], [4, 5]]
    >>> critical_connections(6, [[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [4, 6], [5, 6]]
    []
    >>> critical_connections(9, [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]])
    [[3, 4], [3, 6], [4, 5]]
    """
    # adj list O(edges)
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # modified tarjan's algorithm with label and group O(V+E)
    labels = [-1]*n
    groups = [-1]*n
    label = 0
    res = []
    def dfs(v: int, p: int) -> None:
        nonlocal label
        labels[v] = groups[v] = label
        label += 1
        for nv in adj[v]:
            if nv == p: continue
            if labels[nv] == -1: dfs(nv, v)
            groups[v] = min(groups[v], groups[nv])
            if labels[v] < groups[nv]: res.append([v, nv])

    return res
