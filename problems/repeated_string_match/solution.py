class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        q = ceil(len(b) / len(a))
        for i in range(2):
            if b in a*(q + i): return q + i
        return -1