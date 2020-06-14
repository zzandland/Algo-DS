from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        t, res = Counter(chars), 0
        for w in words:
            x = Counter(w)
            for c in x:
                if x[c] > t[c]:
                    break
            else:
                res += len(w)
        return res