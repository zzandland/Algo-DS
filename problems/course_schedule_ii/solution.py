from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res, out_seen = [], set()
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
        def dfs(n: int) -> bool:
            nonlocal res
            for nn in adj[n]:
                if nn in seen: return False
                if nn not in out_seen:
                    seen.add(nn)
                    if not dfs(nn): return False
                    seen.remove(nn)
            res.append(n)
            out_seen.add(n)
            return True
        for i in range(numCourses):
            seen = set([i])
            if i not in out_seen and not dfs(i): return []
        return res