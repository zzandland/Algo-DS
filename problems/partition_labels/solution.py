class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last, out, end, start = {c: i for i, c in enumerate(S)}, [], 0, 0
        for i, c in enumerate(S):
            end = max(end, last[c])
            if i == end:
                out.append(i-start+1)
                start = i+1
        return out        