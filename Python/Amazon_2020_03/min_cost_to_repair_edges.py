#  There's an undirected connected graph with n nodes labeled 1..n. But some of the edges has been broken disconnecting the graph. Find the minimum cost to repair the edges so that all the nodes are once again accessible from each other.

#  Input:

#  n, an int representing the total number of nodes.
#  edges, a list of integer pair representing the nodes connected by an edge.
#  edgesToRepair, a list where each element is a triplet representing the pair of nodes between which an edge is currently broken and the cost of repearing that edge, respectively (e.g. [1, 2, 12] means to repear an edge between nodes 1 and 2, the cost would be 12).

#  Example 1:

#  Input:
n1 = 5
edges1 = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
edgesToRepair1 = [[1, 2, 12], [3, 4, 30], [1, 5, 8]]
#  Output: 20
#  Explanation:
#  There are 3 connected components due to broken edges: [1], [2, 3] and [4, 5].
#  We can connect these components into a single component by repearing the edges between nodes 1 and 2, and nodes 1 and 5 at a minimum cost 12 + 8 = 20.

#  Example 2:

#  Input:
n2 = 6
edges2 = [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]]
edgesToRepair2 = [[1, 6, 410], [2, 4, 800]]
#  Output: 410

#  Example 3:

#  Input:
n3 = 6
edges3 = [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]]
edgesToRepair3 = [[1, 5, 110], [2, 4, 84], [3, 4, 79]]
#  Output: 79

#  import heapq

#  def minCostToRepair(n, edges, edgesToRepair):
    #  uf, hp, repairSet = [i for i in range(0, n+1)], [], {(a, b): cost for a, b, cost in edgesToRepair}
    #  output, setCnt = 0, n
    #  def find(x):
        #  if x != uf[x]: uf[x] = find(uf[x])
        #  return uf[x]
    #  def union(x, y):
        #  nonlocal setCnt
        #  ux, uy = find(x), find(y)
        #  if ux != uy:
            #  uf[ux] = uy
            #  setCnt -= 1
    #  for a, b in edges:
        #  if (a, b) in repairSet:
            #  heapq.heappush(hp, (repairSet[(a, b)], a, b))
        #  else:
            #  heapq.heappush(hp, (0, a, b))
            #  union(a, b)
    #  while setCnt > 1:
        #  cost, a, b = heapq.heappop(hp)
        #  if find(a) != find(b):
            #  print(uf, setCnt)
            #  output += cost
            #  union(a, b)
    #  return output

from typing import List
from collections import defaultdict
from heapq import heapify, heappush, heappop

def prim(N: int, edges: List[List[int]], edgesToRepair: List[List[int]]) -> int:
    '''
    >>> prim(n1, edges1, edgesToRepair1)
    20
    >>> prim(n2, edges2, edgesToRepair2)
    410
    >>> prim(n3, edges3, edgesToRepair3)
    79
    '''
    # prim's algorithm O((V+E) log V)

    # create adj list O(edges)
    adj = defaultdict(list)

    # for edges to repair add with the given costs
    # save visited edges to prevent redundancy in next step
    seenEdges = set()
    for u, v, c in edgesToRepair:
        adj[u].append((c, v))
        adj[v].append((c, u))
        seenEdges.add(tuple(sorted([u, v])))

    # for edges that don't need maintenance add with 0 cost
    for u, v in edges:
        if tuple(sorted([u, v])) not in seenEdges:
            adj[u].append((0, v))
            adj[v].append((0, u))

    # start from vertex 1, link vertices with min cost edges until all vertices
    # are connected O((V+1) log V)
    seen = set([1])
    pq = adj[1]
    heapify(pq)
    cost = 0

    while pq:
        c, n = heappop(pq)
        if n in seen: continue
        seen.add(n)
        cost += c
        if len(seen) == N: return cost
        for nc, nn in adj[n]:
            heappush(pq, (nc, nn))

    # if number of visited nodes never reached N, we could never connect all nodes
    return -1

def kruskal(N: int, edges: List[List[int]], edgesToRepair: List[List[int]]) -> int:
    '''
    >>> kruskal(n1, edges1, edgesToRepair1)
    20
    >>> kruskal(n2, edges2, edgesToRepair2)
    410
    >>> kruskal(n3, edges3, edgesToRepair3)
    79
    '''
    # kruskal's algorithm O(E log(V))

    # union edges with edgesToRepair in a way that edges don't need maintenance gets 0 cost
    # O(edges + edgesToRepair)
    repair_set = set()
    edge_union = []
    for u, v, c in edgesToRepair:
        edge_union.append([c, u, v])
        repair_set.add(tuple(sorted([u, v])))

    for u, v in edges:
        if tuple(sorted([u, v])) not in repair_set: edge_union.append([0, u, v])

    # sort the edges by cost O(edge log edge)
    edge_union.sort()

    parents = [i for i in range(N+1)]
    ranks = [1]*(N+1)

    # disjoint set find operation O(log biggest set) -> amortized O(1) due to compaction
    def find(u: int) -> int:
        while parents[u] != u:
            parents[u] = parents[parents[u]]
            u = parents[u]
        return u

    # disjoint union operation O(1) -> union by rank
    def union(u: int, v: int) -> bool:
        pu, pv = find(u), find(v)
        if pu == pv: return False
        if ranks[pv] > ranks[pu]: pu, pv = pv, pu
        parents[pv] = pu
        ranks[pu] += ranks[pv]
        return True

    # iterate through the edges and add costs when two disjoint sets are unioned O(edge)
    cost = 0
    for c, u, v in edge_union:
        if union(u, v): cost += c

    # only if there's one disjoint set at the end we could make a minimum spanning tree
    return cost if len({find(u) for u in parents[1:]}) == 1 else -1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
