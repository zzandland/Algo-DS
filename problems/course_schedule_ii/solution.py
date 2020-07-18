from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adj list O(prereq)
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)
            
        # arr stores three states: unvisitied (0), visiting (1), visited (2)
        seen = [0]*numCourses
        res = []
        
        # helper dfs function
        def dfs(n: int) -> bool:
            if seen[n] == 2: return True
            if seen[n] == 1: return False
            seen[n] = 1
            for nn in adj[n]:
                if not dfs(nn): return False
            res.append(n)
            seen[n] = 2
            return True
            
        # for each course run dfs O(n) -> O(V + E)
        for n in range(numCourses):
            if not dfs(n): return []
        return res[::-1]