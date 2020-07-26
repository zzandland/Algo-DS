from collections import defaultdict

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # get the lastest index of each character O(S)
        idx = {}
        for i, c in enumerate(S):
            idx[c] = i
            
        # greedily increase window until left pointer
        # catches up with right pointer O(S)
        res = []
        l = r = 0
        for i, c in enumerate(S):
            r = max(r, idx[c])
            if r == len(S)-1: return res + [r-l+1]
            if i == r:
                res.append(r-l+1)
                l = i+1