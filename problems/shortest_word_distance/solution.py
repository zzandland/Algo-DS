class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        idx1 = idx2 = float('-inf')
        res = float('inf')
        for i, word in enumerate(words):
            if word == word1: idx1 = i
            elif word == word2: idx2 = i
            res = min(res, abs(idx1 - idx2))
        return res