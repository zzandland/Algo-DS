#  Given an undirected graph with n nodes labeled 1..n. Some of the nodes are already connected. The i-th edge connects nodes edges[i][0] and edges[i][1] together. Your task is to augment this set of edges with additional edges to connect all the nodes. Find the minimum cost to add new edges between the nodes such that all the nodes are accessible from each other.

#  Input:

#  n, an int representing the total number of nodes.
#  edges, a list of integer pair representing the nodes already connected by an edge.
#  newEdges, a list where each element is a triplet representing the pair of nodes between which an edge can be added and the cost of addition, respectively (e.g. [1, 2, 5] means to add an edge between node 1 and 2, the cost would be 5).

#  Example 1:

#  Input:
n = 6
edges = [[1, 4], [4, 5], [2, 3]]
newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
#  Output: 7
#  Explanation:
#  There are 3 connected components [1, 4, 5], [2, 3] and [6].
#  We can connect these components into a single component by connecting node 1 to node 2 and node 1 to node 6 at a minimum cost of 5 + 2 = 7.

from typing import List
from collections import defaultdict
from heapq import heapify, heappop, heappush
import operator

def prim(N: int, edges: List[List[int]], newEdges: List[List[int]]) -> int:
    '''
    >>> prim(n, edges, newEdges)
    7
    '''
    # prim's algorithm ((V+E) log V)

    # make adj list with existing edges with cost of 0 O(edges + newEdges)
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append((0, v))
        adj[v].append((0, u))

    for u, v, c in newEdges:
        adj[u].append((c, v))
        adj[v].append((c, u))

    # add edge of vertex 1 to priority queue and heapify
    pq = adj[1]
    seen = set([1])
    heapify(pq)
    cost = 0

    # until all nodes are visited keep adding edges with least cost O((V+E) log V)
    while pq:
        c, v = heappop(pq)
        if v in seen: continue
        seen.add(v)
        cost += c
        if len(seen) == N: return cost
        for nc, nv in adj[v]:
            heappush(pq, (nc, nv))

    # if not all vertices are visited after using all edges no minimum spanning tree can be made
    return -1

def kruskal(N: int, edges: List[List[int]], newEdges: List[List[int]]) -> int:
    '''
    >>> kruskal(n, edges, newEdges)
    7
    '''
    # kruskal's algorithm O(E log V)

    # combine edges with newEdges in a way that exisiting edges get 0 cost O(edges + newEdges)
    edgeList = [[u, v, 0] for u, v in edges] + newEdges

    # sort the edgeList O(e log e)
    edgeList.sort(key=operator.itemgetter(2))

    # disjoint set find with compaction O(log group) -> amortized O(1)
    parents = [u for u in range(N+1)]
    ranks = [1]*(N+1)

    def find(u: int) -> int:
        while parents[u] != u:
            parents[u] = parents[parents[u]]
            u = parents[u]
        return u

    # disjoint set union by rank O(1)
    def union(u: int, v: int) -> bool:
        pu, pv = find(u), find(v)
        if pu == pv: return False
        if ranks[pv] > ranks[pu]: pu, pv = pv, pu
        parents[pv] = pu
        ranks[pu] += ranks[pv]
        return True

    # iterate all edges while adding cost only if two disjoint sets are unioned O(e log group)
    cost = 0
    for u, v, c in edgeList:
        if union(u, v): cost += c

    # if there's more than one disjoint set no minimum spanning tree can be created
    return cost if len({find(u) for u in parents[1:]}) == 1 else -1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
