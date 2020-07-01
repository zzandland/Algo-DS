from collections import defaultdict

class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2): return False
        adj = defaultdict(set)
        for u, v in pairs:
            adj[u].add(v)
            adj[v].add(u)
        for a, b in zip(words1, words2):
            if not (a == b or b in adj[a]): return False
        return True