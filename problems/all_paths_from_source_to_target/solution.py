class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        seen = set([0])
        def dfs(n: int, tmp: List[int]) -> List[List[int]]:
            if n == len(graph) - 1: return [tmp[:]]
            res = []
            for nn in graph[n]:
                if nn not in seen:
                    seen.add(nn)
                    tmp.append(nn)
                    res += dfs(nn, tmp)
                    tmp.pop()
                    seen.remove(nn)
            return res
        return dfs(0, [0])