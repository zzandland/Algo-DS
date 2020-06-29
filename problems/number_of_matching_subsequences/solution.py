from collections import defaultdict
import bisect

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        dic, res = defaultdict(list), 0
        for i, c in enumerate(S):
            dic[c].append(i)
        for wd in words:
            j = -1
            for c in wd:
                if c not in dic: break
                k = bisect.bisect_left(dic[c], j+1)
                if k == len(dic[c]) or dic[c][k] < j: break
                j = dic[c][k]
            else:
                res += 1
        return res