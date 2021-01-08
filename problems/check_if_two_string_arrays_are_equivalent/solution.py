class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def add(a, b):
            if a and b: return a + b
            return a or b
        return reduce(add, word1) == reduce(add, word2)