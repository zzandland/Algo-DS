class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q1, q2, nq, words, cnt = set([beginWord]), set([endWord]), set(), set(wordList), 0
        if endWord not in wordList: return cnt
        while q1 and q2:
            words -= q1
            if len(q1) > len(q2): q1, q2 = q2, q1
            cnt += 1
            for w in q1:
                for i in range(len(beginWord)):
                    for c in 'qwertyuiopasdfghjklzxcvbnm':
                        comb = w[:i]+c+w[i+1:]
                        if comb in q2: return cnt+1
                        if comb in words: nq.add(comb)
            q1, nq = nq, set()
        return 0