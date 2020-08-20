from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        res = [float('inf')]*n
        radj, badj = defaultdict(set), defaultdict(set)
        for u, v in red_edges:
            radj[u].add(v)
        for u, v in blue_edges:
            badj[u].add(v)
        # node, red, dist
        q = deque([(0, True, 0), (0, False, 0)])
        while q:
            n, red, dist = q.popleft()
            res[n] = min(res[n], dist)
            if red:
                for nn in list(radj[n]):
                    q.append((nn, False, dist+1))
                    radj[n].remove(nn)
            else:
                for nn in list(badj[n]):
                    q.append((nn, True, dist+1))
                    badj[n].remove(nn)
        return [n if n != float('inf') else -1 for n in res]