class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pos = {k: i for i, k in enumerate(keyboard)}
        cur = res = 0
        for c in word:
            res += abs(pos[c] - cur)
            cur = pos[c]
        return res