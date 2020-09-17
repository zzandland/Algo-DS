from heapq import heappush, heappop

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ws = {*wordList}
        if endWord not in ws: return 0
        q1 = {beginWord}
        q2 = {endWord}
        res = 0
        while q1:
            if len(q1) > len(q2): q1, q2 = q2, q1
            res += 1
            ws -= q1
            nq = set()
            for word in q1:
                if word in q2: return res
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        tmp = word[:i] + c + word[i+1:]
                        if tmp in ws: nq.add(tmp)
            q1 = nq
        return 0