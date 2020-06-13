from collections import defaultdict, deque, Counter

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]],
                                 blue_edges: List[List[int]]) -> List[int]:
        radj, badj = defaultdict(list), defaultdict(list)
        for u, v in red_edges:
            radj[u].append(v)
        for u,v in blue_edges:
            badj[u].append(v)
        def bfs(r: bool) -> None:
            nonlocal n
            q, step, res, seen = deque([0]), -1, [float('inf')]*n, Counter()
            while q:
                step += 1
                l = len(q)
                r = not r
                for _ in range(l):
                    v = q.popleft()
                    res[v] = min(res[v], step)
                    for nv in radj[v] if r else badj[v]:
                        if seen[v, nv] < 2:
                            seen[v, nv] += 1
                            q.append(nv)
            return res
        return [-1 if rn == float('inf') and bn == float('inf') else min(rn, bn) for rn, bn in zip(bfs(True), bfs(False))]