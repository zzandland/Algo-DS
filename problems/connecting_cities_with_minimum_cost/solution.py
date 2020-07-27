from heapq import heappush, heappop, heapify
from collections import defaultdict

class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        # kruskal's algorithm O(con log con) -> disjoint set operations
        # are mostly O(1) with compaction and union by rank
        parents = [n for n in range(N+1)]
        ranks = [1]*(N+1)
        
        # disjoint set find O(log biggest set -> amortized 1)
        def find(u: int) -> int:
            while u != parents[u]:
                parents[u] = parents[parents[u]]
                u = parents[u]
            return u
        
        # disjoint set union O(1)
        def union(u: int, v: int) -> bool:
            pu, pv = find(u), find(v)
            if pu == pv: return False
            if ranks[pv] > ranks[pu]: pu, pv = pv, pu
            parents[pv] = pu
            ranks[pu] += ranks[pv]
            return True
        
        # sort the connections by cost O(con log con)
        connections.sort(key=operator.itemgetter(2))
        
        # go through all connections while doing disjoing-set operations O(V log E)
        cost = 0
        for u, v, c in connections:
            # if union is successful, add the cost
            if union(u, v): cost += c
        
        # if there's only one group return cost
        return cost if len({find(n) for n in parents[1:]}) == 1 else -1