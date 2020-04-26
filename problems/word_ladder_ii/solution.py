import collections

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        tree, words, found = collections.defaultdict(set), set(wordList), False
        if endWord not in wordList: return []
        q1, q2, nq, rev = {beginWord}, {endWord}, set(), False
        while q1 and not found:
            words -= q1
            for w in q1:
                for nw in [w[:i] + chr(j) + w[i+1:] for i in range(len(w)) for j in range(97, 123)]:
                    if nw in words:
                        if nw in q2: found = True
                        else: nq.add(nw)
                        tree[nw].add(w) if rev else tree[w].add(nw)
            q1, nq = nq, set()
            if len(q1) > len(q2): q2, q1, rev = q1, q2, not rev
        output = []    
        def dfs(x: List[int]) -> List[List[int]]:
            return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in dfs(y)]
        return dfs(beginWord)