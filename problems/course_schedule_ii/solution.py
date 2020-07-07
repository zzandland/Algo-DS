from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj, in_degree = defaultdict(list), [0]*numCourses
        
        # make adj list & in_degree O(E)
        for u, v in prerequisites:
            adj[v].append(u)
            in_degree[u] += 1
            
        # put all nodes with 0 incoming edge to a queue O(V)
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        # BFS on the nodes with 0 incoming edge O(V+E)
        cnt, res = 0, []
        while q:
            n = q.popleft()
            res.append(n)
            for nn in adj[n]:
                in_degree[nn] -= 1
                if in_degree[nn] == 0: q.append(nn)
            cnt += 1
        if cnt != numCourses: return []
        return res