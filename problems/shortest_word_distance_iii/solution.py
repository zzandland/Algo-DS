class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        a = b = float('-inf')
        res = float('inf')
        for i, w in enumerate(words):
            if w == word1:
                if word1 == word2: b = a
                a = i
            elif w == word2: b = i
            res = min(res, abs(a - b))
        return res