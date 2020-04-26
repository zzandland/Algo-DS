from collections import defaultdict

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        stg, bg, visited, transfer, found = defaultdict(set), defaultdict(set), {S}, 0, False
        for bus, route in enumerate(routes):
            for st in route:
                stg[st].add(bus)
                bg[bus].add(st)
                if st == T: found = True
        if not found: return -1
        q, nq = {(S, b) for b in stg[S]}, set()
        while q:
            tmp = set()
            if T in [i[0] for i in q]: return transfer
            transfer += 1
            for st, b in q:
                if T in bg[b]: return transfer
                for nb in stg[st]:
                    for ns in bg[nb]:
                        if ns not in visited:
                            tmp.add(ns)
                            nq.add((ns, nb))
            q, nq = nq, set()                
            visited = visited.union(tmp)
        return -1    