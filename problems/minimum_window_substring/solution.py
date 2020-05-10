from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ''
        dic, zero, ts, mn, output = defaultdict(int), set(list(t)), set(list(t)), float('inf'), ''
        for tc in t:
            dic[tc] += 1
        j = 0
        for i, sc in enumerate(s):
            dic[sc] -= 1
            if dic[sc] == 0 and sc in zero: zero.remove(sc)
            while not zero:
                if i-j+1 < mn:
                    mn = i-j+1
                    output = s[j:i+1]
                dic[s[j]] += 1
                if s[j] in ts and dic[s[j]] > 0:
                    zero.add(s[j])
                j+=1    
        return output            