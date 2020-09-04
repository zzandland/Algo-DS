class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        idx = {s: i for i, s in enumerate(S)}
        l = r = 0
        res = []
        for i in range(len(S)):
            r = max(r, idx[S[i]])
            if i == r:
                res.append(r-l+1)
                l = i+1
        return res