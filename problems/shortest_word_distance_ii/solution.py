class WordDistance:

    def __init__(self, words: List[str]):
        self.word_idx = defaultdict(list)
        self.distances = {}
        for i, word in enumerate(words):
            self.word_idx[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        p = tuple(sorted([word1, word2]))
        if p not in self.distances:
            aidx, bidx = self.word_idx[word1], self.word_idx[word2]
            a = b = 0
            mn = float('inf')
            while a < len(aidx) and b < len(bidx):
                mn = min(mn, abs(aidx[a] - bidx[b]))
                if aidx[a] < bidx[b]: a += 1
                else: b += 1
            self.distances[p] = mn
        return self.distances[p]

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)