from collections import defaultdict

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # adj list O(E)
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        res = [1]*n
        # dfs post order -> if child has same label as parent add total num of child O(V+E)
        seen = set([0])
        def dfs(i: int) -> List[int]:
            tmp = [0]*26
            for ni in adj[i]:
                if ni not in seen:
                    seen.add(ni)
                    tmp[ord(labels[ni]) - ord('a')] += 1
                    prev = dfs(ni)
                    for j in range(26):
                        tmp[j] += prev[j]
            res[i] += tmp[ord(labels[i]) - ord('a')]
            return tmp
        dfs(0)
        return res