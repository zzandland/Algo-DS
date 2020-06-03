from collections import defaultdict, Counter, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj, indegree = defaultdict(set), Counter({c: 0 for c in set(''.join(words))})
        for fw, sw in zip(words, words[1:]):
            for c, d in zip(fw, sw):
                if c != d:
                    if d not in adj[c]:
                        adj[c].add(d)
                        indegree[d] += 1
                    break
            else:
                if len(fw) > len(sw): return ''
        q, res = deque([c for c in indegree if indegree[c] == 0]), []        
        while q:
            c = q.popleft()
            res.append(c)
            for nc in adj[c]:
                indegree[nc] -= 1
                if indegree[nc] == 0:
                    q.append(nc)
        if len(res) != len(indegree): return ''            
        return ''.join(res)