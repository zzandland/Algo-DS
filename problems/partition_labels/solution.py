class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic, res = {c: i for i, c in enumerate(S)}, []
        last = cut = -1
        for i, c in enumerate(S):
            last = max(last, dic[c])
            if i == last:
                res.append(i-cut)
                cut = i
        return res