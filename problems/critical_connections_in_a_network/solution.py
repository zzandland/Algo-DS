from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        ids, lows, id_, graph = [None] * n, [None] * n, 0, defaultdict(list)
        for frm, to in connections:
            graph[frm].append(to)
            graph[to].append(frm)
        def dfs(cur: int, prev: int):
            nonlocal id_
            ids[cur] = lows[cur] = id_
            id_ += 1
            for to in graph[cur]:
                if lows[to] == None and to != prev: dfs(to, cur)
            lows[cur] = min([ids[cur]] + [lows[to] for to in graph[cur] if to != prev])
        dfs(0, -1)    
        return [[frm, to] for frm, to in connections if ids[frm] < lows[to] or ids[to] < lows[frm]]