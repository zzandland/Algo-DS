from collections import defaultdict

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        idx = defaultdict(list)
        for i, c in enumerate(s):
            idx[c].append(i)
            
        substrs = []
        for i in range(len(s)):
            l, r = i, idx[s[i]][-1]
            while l < len(s):
                if idx[s[l]][0] < i: break
                r = max(r, idx[s[l]][-1])
                if l == r: substrs.append((i, r))
                l += 1
        
        res = [substrs[0]]
        for a, b in substrs[1:]:
            if res[-1][1] < a: res.append((a, b))
            elif res[-1][1] > b: res[-1] = (a, b)
                
        return [s[a:b+1] for a, b in res]