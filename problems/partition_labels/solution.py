class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        idx = {}
        for i, c in enumerate(S): idx[c] = i
            
        l = r = 0
        res = []
        for i, c in enumerate(S):
            r = max(r, idx[c])
            if i == r:
                res.append(r-l+1)
                l = i+1
        return res