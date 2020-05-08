from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph, visited = defaultdict(list), set()
        for b, a in prerequisites:
            graph[a].append(b)
        def fn(n: int) -> bool:
            if n in loop: return False
            loop.add(n)
            for nxt in graph[n]:
                if nxt not in visited:
                    if not fn(nxt): return False
                    loop.remove(nxt)
            visited.add(n)
            return True    
        for i in range(numCourses):
            loop = set()
            if i not in visited and not fn(i): return False
        return True