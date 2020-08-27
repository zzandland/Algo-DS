from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adj = defaultdict(list)
        for v, u in prerequisites:
            adj[u].append(v)
            indegree[v] += 1
        q = deque([i for i, n in enumerate(indegree) if n == 0])
        visited = 0
        while q:
            n = q.popleft()
            visited += 1
            for nn in adj[n]:
                indegree[nn] -= 1
                if indegree[nn] == 0: q.append(nn)
        return visited == numCourses