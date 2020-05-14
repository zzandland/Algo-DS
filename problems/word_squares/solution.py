from collections import defaultdict

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        if not words: return []
        N, W, graph, output = len(words), len(words[0]), defaultdict(list), []
        for w in words:
            for i in range(1, W):
                graph[w[:i]].append(w)
        def fn(ws: List[str]) -> List[str]:
            if len(ws) == W: return [ws]
            key = ''.join([w[len(ws)] for w in ws])
            output = []
            for nw in graph[key]: output += fn(ws+[nw])
            return output    
        output = []
        for w in words: output += fn([w])
        return output