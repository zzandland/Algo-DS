from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph, cnt = defaultdict(list), 0
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        ids, crits = [i for i in range(n)], [None for i in range(n)]
        def fn(cur: int, prev: int) -> None:
            nonlocal cnt
            ids[cur] = crits[cur] = cnt
            cnt += 1
            for adj in graph[cur]:
                if adj != prev and crits[adj] == None: fn(adj, cur)
            crits[cur] = min([ids[cur]] + [crits[adj] for adj in graph[cur] if adj != prev])
        fn(0, -1)
        return [[a, b] for a, b in connections if ids[a] < crits[b] or ids[b] < crits[a]]
    