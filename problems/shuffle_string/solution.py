class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ['']*len(s)
        for i, c in zip(indices, s):
            res[i] = c
        return ''.join(res)