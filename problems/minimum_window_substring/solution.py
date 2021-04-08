class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = Counter()
        t_dic = Counter(t)
        required = len(t_dic)
        
        l = cnt = 0
        mn = float('inf')
        res = ''
        
        for r in range(len(s)):
            c = s[r]
            dic[c] += 1
            if c in t_dic and dic[c] == t_dic[c]:
                cnt += 1
            while required == cnt:
                if mn > r - l + 1:
                    mn = r - l + 1
                    res = s[l:r+1]
                c = s[l]
                dic[c] -= 1
                if c in t_dic and dic[c] < t_dic[c]:
                    cnt -= 1
                l += 1
                
        return res if mn != float('inf') else ''