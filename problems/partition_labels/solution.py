from collections import defaultdict 

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last, output = {c: i for i, c in enumerate(S)}, []
        delim = prev = 0
        for i, c in enumerate(S):
            delim = max(last[c], delim)
            if i == delim: 
                output.append(i-prev+1)
                prev = i+1
        return output        