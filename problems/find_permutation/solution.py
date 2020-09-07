class Solution:
    def findPermutation(self, s: str) -> List[int]:
        s += 'I'
        prev = 1
        res = []
        for i, c in enumerate(s, 1):
            if c == 'I':
                j = i
                while j >= prev:
                    res.append(j)
                    j -= 1
                prev = i+1
        return res