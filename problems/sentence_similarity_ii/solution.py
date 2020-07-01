from collections import defaultdict

class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2): return False
        adj = defaultdict(set)
        for u, v in pairs:
            adj[u].add(v)
            adj[v].add(u)
        def dfs(w: str, t: str) -> bool:
            if w == t: return True
            for nw in adj[w]:
                if nw not in seen:
                    seen.add(nw)
                    if dfs(nw, t): return True
            return False
        for a, b in zip(words1, words2):
            seen = set([a])
            if dfs(a, b):
                adj[a].add(b)
                adj[b].add(a)
            else:
                return False
        return True