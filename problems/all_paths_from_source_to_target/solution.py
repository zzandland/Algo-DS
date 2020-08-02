class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(n: int, tmp: List[int], seen: set) -> List[List[int]]:
            if n == len(graph)-1: return [tmp[:] + [n]]
            if n in seen: return []
            seen.add(n)
            tmp.append(n)
            res = []
            for nn in graph[n]:
                res += dfs(nn, tmp, seen)
            seen.remove(n)
            tmp.pop()
            return res
        return dfs(0, [], set())