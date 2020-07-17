from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for i, id_ in enumerate(manager):
            if id_ != -1:
                adj[id_].append(i)
        def dfs(n: int) -> int:
            nxt = 0
            for nn in adj[n]:
                nxt = max(nxt, dfs(nn))
            return informTime[n] + nxt
        return dfs(headID)