from typing import List
from collections import defaultdict

def critical_routers(numNodes: int, numEdges: int, edges: List[List[int]]) -> List[int]:
    """
    >>> critical_routers(7, 7, [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]])
    [2, 3, 5]
    """
    # make adj list O(numEdges)
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # dfs with tarjan to identify articulation points O(V+E)
    labels = [-1]*numNodes
    groups = [-1]*numNodes
    label = 0
    res = []
    def dfs(v: int, p: int) -> None:
        nonlocal label
        child = 0
        labels[v] = groups[v] = label
        label += 1
        for nv in adj[v]:
            if nv == p: continue
            child += 1
            if labels[nv] == -1: dfs(nv, v)
            groups[v] = min(groups[v], groups[nv])
            if p == -1 and child > 1: res.append(v)
            elif p != -1 and labels[v] <= groups[nv]: res.append(v)

    return res
