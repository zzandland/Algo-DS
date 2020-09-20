class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        
        for i in range(n):
            adj[manager[i]].append(i)

        def dfs(n: int) -> int:
            return informTime[n] + max([dfs(nn) for nn in adj[n]] or [0])
        return dfs(headID)