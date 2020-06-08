from collections import deque, defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words, N = set(wordList), len(beginWord)
        if endWord not in words: return []
        q1, q2, adj = set([beginWord]), set([endWord]), defaultdict(list)
        found, front = False, True
        while not found and q1:
            if len(q1) > len(q2):
                q1, q2 = q2, q1
                front = not front
            words -= q1
            nq = set()
            for w in q1:
                for i in range(N):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        nw = w[:i]+c+w[i+1:]
                        if nw in words:
                            nq.add(nw)
                            if front:
                                adj[w].append(nw)
                            else:
                                adj[nw].append(w)
                            if nw in q2:
                                found = True
            q1 = nq
        def dfs(w: str) -> List[List[str]]:
            if w == endWord:
                return [[w]]
            return [[w] + rest for nw in adj[w] for rest in dfs(nw)]
        return dfs(beginWord)