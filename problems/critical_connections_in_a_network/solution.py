from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        ids, lows, graph, output, t = [None]*n, [None]*n, defaultdict(list), [], 0
        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)
        def dfs(cur: int, prev: int):
            nonlocal t
            ids[cur] = lows[cur] = t
            t += 1
            for nxt in graph[cur]:
                if lows[nxt] == None: dfs(nxt, cur)
            lows[cur] = min([t]+[lows[nxt_t] for nxt_t in graph[cur] if nxt_t != prev])        
        dfs(0, -1)
        for i, j in connections:
            if ids[i] < lows[j] or ids[j] < lows[i]: output.append([i, j])
                    
        return output