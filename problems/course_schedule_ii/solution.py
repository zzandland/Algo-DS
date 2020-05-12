class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, visited, st = [set() for _ in range(numCourses)], set(), []
        for b, a in prerequisites: graph[a].add(b)
        def dfs(n: int) -> bool:
            if n in visited: return True
            if n in tmp:  return False
            tmp.add(n)
            for nxt in graph[n]:
                if not dfs(nxt): return False
            st.append(n)
            tmp.remove(n)
            visited.add(n)
            return True
        for i in range(numCourses): 
            tmp = set()
            if not dfs(i): return []
        return st[::-1]    