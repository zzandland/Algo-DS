from collections import defaultdict
import bisect

class Solution:
    def minWindow(self, S: str, T: str) -> str:
        idx = defaultdict(list)
        for i, c in enumerate(S):
            idx[c].append(i)
        res = ''
        for i in idx[T[0]]:
            j = i
            for c in T[1:]:
                if c not in idx: return ''
                k = bisect.bisect_left(idx[c], j+1)
                if k == len(idx[c]): break
                j = idx[c][k]
            else:
                if res == '': res = S[i:j+1]
                else: res = min(res, S[i:j+1], key=len)
                if res == T: return res
        return res