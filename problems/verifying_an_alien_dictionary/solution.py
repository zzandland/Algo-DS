class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx = {h: i for i, h in enumerate(order)}
        for a, b in zip(words, words[1:]):
            for ca, cb in zip(a, b):
                if idx[ca] > idx[cb]: return False
                if idx[ca] < idx[cb]: break
            else:
                if len(a) > len(b): return False
        return True