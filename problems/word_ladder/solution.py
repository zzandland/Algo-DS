class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ws = set(wordList)
        ln = len(endWord)
        if endWord not in ws: return 0
        q = set([beginWord])
        res = 0
        while q:
            ws -= q
            res += 1
            nq = set()
            for w in q:
                if w == endWord: return res
                for i in range(ln):
                    for c in string.ascii_lowercase:
                        nw = w[:i] + c + w[i+1:]
                        if nw in ws:
                            nq.add(nw)
            q = nq
        return 0