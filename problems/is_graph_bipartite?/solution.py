class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        nums = {}
        def dfs(n: int, c: bool) -> bool:
            nums[n] = c
            print(n, nums)
            for nei in graph[n]:
                if nei in nums and nums[nei] == c: return False
                if nei not in nums and not dfs(nei, not c): return False
            return True    
        for i in range(len(graph)):
            if i not in nums and not dfs(i, True): return False
        return True                