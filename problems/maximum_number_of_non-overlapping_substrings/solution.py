from collections import defaultdict
import bisect

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        # get indexes of all characters O(n)
        dic = defaultdict(list)
        for i, c in enumerate(s):
            dic[c].append(i)
            
        if all(map(lambda x: len(x) == 1, dic.values())): return [c for c in s]
            
        S = len(s)
        substrs = []
        
        # greedily expand interval starting from each c O(n^2)
        for i in range(S):
            r = i
            for j in range(i, S):
                c = s[j]
                if i > dic[c][0]: break
                # greedily expand r
                r = max(r, dic[c][-1])
                if j == r: substrs.append((i, r))
                
        # 0/1 knapsack backtrack O(!intervals)
        tmp = []
        cnt = 0
        rescnt = float('inf')
        res = []
        def dfs(i: int) -> None:
            nonlocal tmp, cnt, res, rescnt
            if i == len(substrs):
                if len(res) <= len(tmp) and cnt < rescnt:
                    rescnt = cnt
                    res = tmp[:]
                return
            l, r = substrs[i]
            idx = bisect.bisect_left(tmp, (l,))
            if (not tmp or
                (tmp and idx == len(tmp) and tmp[idx-1][1] < l) or
                (idx < len(tmp)-1 and tmp[idx][1] < l and r < tmp[idx+1][0])):
                tmp.insert(idx, (l, r))
                cnt += (r-l+1)
                dfs(i+1)
                tmp.pop(idx)
                cnt -= (r-l+1)
            dfs(i+1)
        dfs(0)
        return map(lambda x: s[x[0]:x[1]+1], res)